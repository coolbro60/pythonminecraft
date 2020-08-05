# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(20):
    mc.setBlock(x+i, y-1, z+i,1)
    mc.setBlock(x+i, y-1, z+i,1)
    mc.setBlock(x+i, y-1, z+i+2,1)
    time.sleep(1)