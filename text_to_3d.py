from visual import *
scene.background = color.white

pysource = materials.texture(data=materials.loadTGA("test/sample_script.tga"), mapping="sign")
b = box(axis = (0,0,1),
        size = (.01, 25, 50),
        material=pysource)
       
def zoom():
    for i in range(30,100):
        scene.range = i
        rate(30)
    
    for i in range(100,29,-1):
        scene.range = i
        rate(30)

def flat():
    scene.forward = (0,0,-1)


def wobble():
    for i in range(100):
        scene.forward = scene.forward.rotate(.1)
        rate(30)        

def swap():
    file1 = materials.texture(data=materials.loadTGA("test/portforward.tga"), mapping="sign")
    file2 = materials.texture(data=materials.loadTGA("test/main.tga"), mapping="sign")
    from time import sleep
    for i in range(10):
        b.material = file1
        sleep(.5)
        b.material = file2
        sleep(.5)


# Set up scene        
scene.autoscale = False
scene.scale = (.1,.1,.1)
scene.forward = (0,0,-1)
scene.range = (30,30,30)
#scene.ambient = (.7,.7,.7)
#scene.background = (.5,.5,.5)

zoom()
