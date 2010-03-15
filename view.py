from visual import box
from visual import color
from visual import materials
from visual import scene

def set_scene():
    scene.background = color.white
    scene.autoscale = False
    scene.scale = (.1,.1,.1)
    scene.forward = (0,0,-1)
    scene.range = (30,30,30)

def draw_source(texture):
    rendered_source = box(axis = (0,0,1),
    	                  size = (.01, 25, 50),
    	                  material=texture)
    return rendered_source 
