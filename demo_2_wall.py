from pyblockworld import World

from class_wall import Wall


def b_pressed(bw: World) -> None:

    # Fetch player position
    x, y, z = bw.player_position(as_int=True)

    # Player position reports one block too high for placement
    y -= 1

    # Offset x so builds don't spawn inside the player
    x += 2

    # Unrotated wall in front of the player
    wall_front = Wall((x, y, z), bw)

    # Rotated wall to the side so both are visible
    # x + 8 = first wall width (6) plus a two-block gap
    wall_side = Wall((x + 8, y, z), bw)
    wall_side.rotated = True

    # Place both walls
    wall_front.build()
    wall_side.build()


# Create world and assign b key as the build key
bw = World()
bw.build_key_pressed = b_pressed

# Run world
bw.run()
