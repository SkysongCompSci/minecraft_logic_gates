from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

# set block types to represent on and off
blockOn = 41
blockOff = 1
andGate = 45
orGate = 57
xorGate = 22
nandGate = 5
norGate = 80

# function to toggle A and B blocks
def toggleBlock (pos):
    if mc.getBlock(pos) == blockOn:
        mc.setBlock(pos, blockOff)
    elif mc.getBlock(pos) == blockOff:
        mc.setBlock(pos, blockOn)

# function to toggle gate
def toggleGate (pos):
    if mc.getBlock(pos) == andGate:
        mc.setBlock(pos, orGate)
        mc.postToChat("You are using an OR gate")
    elif mc.getBlock(pos) == orGate:
        mc.setBlock(pos, xorGate)
        mc.postToChat("You are using an XOR gate")
    elif mc.getBlock(pos) == xorGate:
        mc.setBlock(pos, nandGate)
        mc.postToChat("You are using a NAND gate")
    elif mc.getBlock(pos) == nandGate:
        mc.setBlock(pos, norGate)
        mc.postToChat("You are using a NOR gate")
    elif mc.getBlock(pos) == norGate:
        mc.setBlock(pos, andGate)
        mc.postToChat("You are using an AND gate") 

# get position of player
px, py, pz = mc.player.getPos()

# assign block locations for A, B, gate & Q
A = (px+3, py, pz+1)
B = (px+3, py, pz+2)
gate = (px+3, py, pz+3)
Q = (px+3, py, pz+4)

# set inital blocks    
mc.setBlock(A, blockOff)
mc.setBlock(B, blockOff)
mc.setBlock(gate, andGate)

# output inital setup
mc.postToChat("Stone is OFF")
mc.postToChat("Gold is ON")
mc.postToChat("You are using and AND gate")

while True:  
    # returns list of blocks hit
    # (x,y,z,face,player)
    blockEvent = mc.events.pollBlockHits()
    
    # if list is not empty - get position of block hit
    if len(blockEvent) != 0:
        blockEventPos = blockEvent[0].pos
        toggleBlock(blockEventPos)
        toggleGate(blockEventPos)


    # chnge Q based on A, B and gate
    if mc.getBlock(gate) == andGate:
        # AND gate
        if mc.getBlock(A) == blockOn and mc.getBlock(B) == blockOn:
            mc.setBlock(Q, blockOn)
        else:
            mc.setBlock(Q, blockOff)
    elif mc.getBlock(gate) == orGate:
        # OR gate
        if mc.getBlock(A) == blockOn or mc.getBlock(B) == blockOn:
            mc.setBlock(Q, blockOn)
        else:
            mc.setBlock(Q, blockOff)
    elif mc.getBlock(gate) == xorGate:
        # XOR gate
        if mc.getBlock(A) == blockOn and mc.getBlock(B) == blockOn:
            mc.setBlock(Q, blockOff)
        elif mc.getBlock(A) == blockOff and mc.getBlock(B) == blockOff:
            mc.setBlock(Q, blockOff)
        else:
            mc.setBlock(Q, blockOn)
    elif mc.getBlock(gate) == nandGate:
        # NAND gate
        if mc.getBlock(A) == blockOn and mc.getBlock(B) == blockOn:
            mc.setBlock(Q, blockOff)
        else:
            mc.setBlock(Q, blockOn)        
    elif mc.getBlock(gate) == norGate:
        # NOR gate
        if mc.getBlock(A) == blockOn or mc.getBlock(B) == blockOn:
            mc.setBlock(Q, blockOff)
        else:
            mc.setBlock(Q, blockOn)
