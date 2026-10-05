from pyblockworld import World


def b_pressed(bw: World) -> None:

    # Fetch player position
    x, y, z = bw.player_position(as_int=True)

    # Player position reports one block too high for placement
    y -= 1

    # Offset x so builds don't spawn inside the player
    x += 2

    # 3 Brick along x-axis
    bw.setBlocks(x, y, z, x + 3, y, z, "default:brick")

    # 4 Stone along y-axis
    bw.setBlocks(x, y, z, x, y + 4, z, "default:stone")

    # 5 Sand along z-axis
    bw.setBlocks(x, y, z, x, y, z + 4, "default:sand")


# Create world and assign b key as the build key
bw = World()
bw.build_key_pressed = b_pressed

# Run world
bw.run()
