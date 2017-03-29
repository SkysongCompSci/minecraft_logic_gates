from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

# set block types to represent on and off
blockOn = 41
blockOff = 1

# function to toggle blocks
def toggleBlock (pos):
    if mc.getBlock(pos) == blockOn:
        mc.setBlock(pos, blockOff)
    else:
        mc.setBlock(pos, blockOn)


# get position of player
px, py, pz = mc.player.getPos()

# assign block locations for A, B & Q
A = (px+3, py, pz+1)
B = (px+3, py, pz+2)
Q = (px+3, py, pz+3)

# set blocks    
mc.setBlock(A, blockOff)
mc.setBlock(B, blockOff)


while True:  
    # returns list of blocks hit
    # (x,y,z,face,player)
    blockEvent = mc.events.pollBlockHits()
    
    # if list is not empty - get position of block hit
    if len(blockEvent) != 0:
        blockEventPos = blockEvent[0].pos
        toggleBlock(blockEventPos)


    # AND gate
    if mc.getBlock(A) == blockOn and mc.getBlock(B) == blockOn:
        mc.setBlock(Q, blockOn)
    else:
        mc.setBlock(Q, blockOff)
        

