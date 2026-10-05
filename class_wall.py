from pyblockworld import World


class Wall:
    def __init__(self, pos: tuple[int, int, int], bw: World) -> None:
        self.pos = pos
        self.width = 6
        self.height = 5
        self.rotated = False
        self.material_id = "default:stone"
        self.bw = bw

    def build(self) -> None:
        x, y, z = self.pos
        if self.rotated:
            # Rotated wall spans z-axis instead of x-axis
            self.bw.setBlocks(
                x,
                y,
                z,
                x,
                y + self.height,
                z + self.width,
                self.material_id,
            )
        else:
            # Unrotated wall spans x-axis
            self.bw.setBlocks(
                x,
                y,
                z,
                x + self.width,
                y + self.height,
                z,
                self.material_id,
            )
