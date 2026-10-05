from pyblockworld import World

from class_wall import WallWithDoor, WallWithWindow


def b_pressed(bw: World) -> None:

    # Fetch player position
    x, y, z = bw.player_position(as_int=True)

    # Player position reports one block too high for placement
    y -= 1

    # Offset x so builds don't spawn inside the player
    x += 2

    # Window walls: one unrotated, one rotated
    window_straight = WallWithWindow((x, y, z), bw)

    # x + 7 = wall width (6) plus a one-block gap
    window_rotated = WallWithWindow((x + 7, y, z), bw)
    window_rotated.rotated = True

    # Door walls: one unrotated, one rotated
    # x + 10 = rotated wall width in x (1) plus a two-block gap
    door_straight = WallWithDoor((x + 10, y, z), bw)

    # x + 17 = wall width (6) plus a one-block gap
    door_rotated = WallWithDoor((x + 17, y, z), bw)
    door_rotated.rotated = True

    # Place all four walls
    window_straight.build()
    window_rotated.build()
    door_straight.build()
    door_rotated.build()


# Create world and assign b key as the build key
bw = World()
bw.build_key_pressed = b_pressed

# Run world
bw.run()
