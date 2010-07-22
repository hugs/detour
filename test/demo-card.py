
from visual import color
from visual import box

from detour.view import set_scene
from detour.view import wobble
set_scene()



def highlight():
    b = box()
    b.color = color.yellow
    b.pos = (0,0,0)
    b.size = (50,1,.1)
    b.opacity = .5

from detour.view import Card
c1 = Card('test/sample_script.py')
c2 = Card("test/sample_script.py", pos = (60,0,0))

