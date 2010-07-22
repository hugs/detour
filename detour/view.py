from visual import box
from visual import color
from visual import materials
from visual import scene
from visual import rate
from converters import file_to_texture

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
    
def fade_in(card):
    for i in range (100):
        card.opacity = i/100.
        rate(50)
        
def zoom_in():
    for i in range(40,29,-1):
        scene.range = i
        rate(30)
        
def zoom_out():
    for i in range(30,41):
        scene.range = i
        rate(30)
 
def flat():
    scene.forward = (0,0,-1)
    
def wobble():
    for i in range(100):
        scene.forward = scene.forward.rotate(.1)
        rate(30)        
             
def focus(card):
    zoom_out()
    origin = int(scene.center.x)
    destination = int(card.pos.x)
    if (destination - origin < 0):
        direction = -1    # Scrollin' left
    elif (destination - origin > 0):
        direction = 1     # Scrollin' right
    else:
        direction = 1     # Not goin' anywhere
    for i in range(origin,destination,direction):
        scene.center = (i,0,0)
        rate(100) 
    zoom_in()



def load_from_file(filepath, pos=(0,0,0), effect=fade_in):
    texture = file_to_texture(filepath) 
    card = box(axis = (0,0,1),
                      size = (.01, 25, 50),
                      pos = pos,
                      opacity = 0,
                      material=texture)
    effect(card)
    return card
    

class Card:
    def __init__(self, filepath, pos=(0,0,0), effect=fade_in):
        texture = file_to_texture(filepath) 
        self.card = box(axis = (0,0,1),
                          size = (.01, 25, 50),
                          pos = pos,
                          opacity = 0,
                          material=texture)
        effect(self.card)
 
    def focus(self):
        zoom_out()
        origin = int(scene.center.x)
        destination = int(self.card.pos.x)
        if (destination - origin < 0):
            direction = -1    # Scrollin' left
        elif (destination - origin > 0):
            direction = 1     # Scrollin' right
        else:
            direction = 1     # Not goin' anywhere
        for i in range(origin,destination,direction):
            scene.center = (i,0,0)
            rate(100) 
        zoom_in()

