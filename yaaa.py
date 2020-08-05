# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:52:45 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
print (mc.player.getTilePos())