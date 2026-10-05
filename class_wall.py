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


class WallWithWindow(Wall):
    def __init__(self, pos: tuple[int, int, int], bw: World) -> None:
        super().__init__(pos, bw)
        self.window_material_id = "air"

    def build(self) -> None:
        super().build()
        # Window hole: two blocks wide and high, centered in the wall plane
        x, y, z = self.pos
        if self.rotated:
            self.bw.setBlocks(x, y + 1, z + 2, x, y + 2, z + 3, self.window_material_id)
        else:
            self.bw.setBlocks(x + 2, y + 1, z, x + 3, y + 2, z, self.window_material_id)


class WallWithDoor(Wall):
    def __init__(self, pos: tuple[int, int, int], bw: World) -> None:
        super().__init__(pos, bw)
        self.door_material_id = "air"

    def build(self) -> None:
        super().build()
        # Door hole: two blocks wide and high, centered at ground level
        x, y, z = self.pos
        if self.rotated:
            self.bw.setBlocks(x, y, z + 2, x, y + 1, z + 3, self.door_material_id)
        else:
            self.bw.setBlocks(x + 2, y, z, x + 3, y + 1, z, self.door_material_id)
