from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
number = 1
for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
    mc.postToChat("you spawned"+str(number)+"silverfish")
    number*=2
