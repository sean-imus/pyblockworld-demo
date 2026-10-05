from pyblockworld import World

from class_wall import Wall


def b_pressed(bw: World) -> None:

    # Fetch player position
    x, y, z = bw.player_position(as_int=True)

    # Player position reports one block too high for placement
    y -= 1

    # Unrotated wall in front of the player
    wall_front = Wall((x + 2, y, z), bw)

    # Rotated wall to the side so both are visible
    wall_side = Wall((x + 10, y, z), bw)
    wall_side.rotated = True

    # Place both walls
    wall_front.build()
    wall_side.build()


# Create world and assign b key as the build key
bw = World()
bw.build_key_pressed = b_pressed

# Run world
bw.run()
