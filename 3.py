
"""
TODO
"""

import sys

import direct.directbase.DirectStart

base.setBackgroundColor(0.0, 0.0, 0.0)
base.disableMouse()

camera.setPos(0.0, -20.0, 10.0)
camera.lookAt(0.0, 0.0, 0.0)

root = render.attachNewNode("Root")

modelCube = loader.loadModel("cube.egg")

cubes = []
for x in [-3.0, 0.0, 3.0]:
    cube = modelCube.copyTo(root)
    cube.setPos(x, 0.0, 0.0)
    cubes += [ cube ]

shader = loader.loadShader("3.sha")
root.setShader(shader)

base.accept("escape", sys.exit)
base.accept("o", base.oobe)

def move(x, y, z):
    root.setX(root.getX() + x)
    root.setY(root.getY() + y)
    root.setZ(root.getZ() + z)

base.accept("d", move, [1.0, 0.0, 0.0])
base.accept("a", move, [-1.0, 0.0, 0.0])
base.accept("w", move, [0.0, 1.0, 0.0])
base.accept("s", move, [0.0, -1.0, 0.0])
base.accept("e", move, [0.0, 0.0, 1.0])
base.accept("q", move, [0.0, 0.0, -1.0])

run()