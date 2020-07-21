# Laboratorio 3 Tests.py

#Import our gl library
import math
from gl import Render,colorScale
from obj import Obj

#We draw our Raptor
mainGl=Render(1400,1400)
mainGl.loadObjModel('raptor.obj',700,500)
mainGl.glFinish('graphic.bmp')

#We draw our Dinosaur
mainGl2=Render(1400,1400)
mainGl2.loadObjModel('dinosaur.obj',700,700,5,5)
mainGl2.glFinish('graphic2.bmp')

#We draw our Trex
mainGl3=Render(1400,1400)
mainGl3.loadObjModel('trex.obj',700,500,3,3)
mainGl3.glFinish('graphic3.bmp')

#We draw our Laptop
mainGl4=Render(1400,1400)
mainGl4.loadObjModel('laptop.obj',700,500,25,25)
mainGl4.glFinish('graphic4.bmp')

#We draw our Roulette
mainGl5=Render(5000,5000)
mainGl5.loadObjModel('roulette.obj',2500,500,1,1)
mainGl5.glFinish('graphic5.bmp')
