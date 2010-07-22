from time import sleep
from detour.view import load_from_file, focus, set_scene
from visual import scene, rate

set_scene()
card1 = load_from_file("test/main.c",
                 pos = (0,0,0))
card2 = load_from_file("test/sample_script.py",
                 pos = (60,0,0))

focus(card2)
focus(card1)
