{
  description = "pyblockworld demos";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs =
    { self, nixpkgs }:
    let
      inherit (nixpkgs) lib;

      systems = [
        "x86_64-linux"
        "aarch64-linux"
      ];
      forAllSystems = f: lib.genAttrs systems (system: f nixpkgs.legacyPackages.${system});

      mkPython =
        pkgs:
        let
          python = pkgs.python3.override {
            self = python;
            packageOverrides = final: prev: {
              pyglet = prev.pyglet.overridePythonAttrs rec {
                version = "1.5.31";
                src = final.fetchPypi {
                  pname = "pyglet";
                  inherit version;
                  extension = "zip";
                  hash = "sha256-peQitMJ7D8mekhA79JMQnMpcGBQ1g7hos7RjGpiulBc=";
                };
                build-system = [ final.setuptools ];
              };

              pyblockworld = final.buildPythonPackage rec {
                pname = "pyblockworld";
                version = "0.3.10";
                pyproject = true;
                src = final.fetchPypi {
                  inherit pname version;
                  hash = "sha256-7PhQZmpmxdobbFizMLcUTACmU4k6M0PMby7bwF5H0xE=";
                };
                build-system = [ final.poetry-core ];
                dependencies = [ final.pyglet ];
              };
            };
          };
        in
        python.withPackages (ps: [ ps.pyblockworld ]);

      mkFormatter =
        pkgs:
        pkgs.treefmt.withConfig {
          runtimeInputs = [
            pkgs.nixfmt
            pkgs.ruff
          ];
          settings = {
            on-unmatched = "info";
            formatter = {
              nixfmt = {
                command = "nixfmt";
                includes = [ "*.nix" ];
              };
              ruff-check = {
                command = "ruff";
                options = [
                  "check"
                  "--fix"
                ];
                includes = [ "*.py" ];
                priority = 0;
              };
              ruff-format = {
                command = "ruff";
                options = [ "format" ];
                includes = [ "*.py" ];
                priority = 1;
              };
            };
          };
        };
    in
    {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          packages = [
            (mkPython pkgs)
            pkgs.ruff
            (pkgs.writeShellScriptBin "p" ''exec python "$@"'')
          ];
        };
      });

      formatter = forAllSystems mkFormatter;

      checks = forAllSystems (pkgs: {
        formatting = (mkFormatter pkgs).check self;
      });
    };
}
