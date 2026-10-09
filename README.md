# pyblockworld-demo

Requires [Nix](https://nixos.org) with flakes enabled.

```sh
nix develop                      # shell with python, pyblockworld and ruff
python demo_3_wall_variants.py
nix fmt                          # format Nix and Python, apply ruff lint fixes
nix flake check                  # fail on unformatted code or lint errors
```

In-game, press `b` to build at the player's position.
