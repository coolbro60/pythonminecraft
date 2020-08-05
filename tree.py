# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 09:26:09 2020

@author: SCE
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
def plantatree(x,y,z):
    mc.setBlocks(x+3,y+3,z+3,x-3,y+6,z-3,48)
    mc.setBlocks(x,y,z,x,y+4,z,15)
for i in range(100):
    for j in range(20):
        plantatree(x+i*9,y+3,z+j*9)
    