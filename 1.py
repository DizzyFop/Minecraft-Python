# Import the api
from mcpi_addons.minecraft import Minecraft
# Initialize the api (MCPI must be open and in a world at this time)
mc = Minecraft.create()
mc.postToChat("Hello World!")

x = input("X Coordinate: ")
y = input("Y Coordinate: ")
z = input("Z Coordinate: ")


x = int(x)
y = int(y)
z = int(z)


#mc.player.setTilePos(x,y,z)

length = 20
width = 20
height = 20


mc.setBlocks(x, y, z, x + width, y + height, z + length, 12)
