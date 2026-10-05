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
        # setBlocks bounds are inclusive, so end coordinates need width/height minus one
        if self.rotated:
            # Rotated wall spans z-axis
            x2, z2 = x, z + self.width - 1
        else:
            # Unrotated wall spans x-axis
            x2, z2 = x + self.width - 1, z
        self.bw.setBlocks(x, y, z, x2, y + self.height - 1, z2, self.material_id)
