from time import sleep
from colorzero import Color
from .tree import RGBXmasTree
from random import seed, random

class NewTree:
    seed(1)
    topLed = 3
    tree = RGBXmasTree(brightness = 0.05)
    colors = [
        Color('cyan'), 
        Color('yellow'), 
        Color('purple'), 
        Color('red'), 
        Color('green'),
        Color('blue')
    ]
    seconds = 0
    def __init__(self, seconds):
        self.seconds = seconds
        
    def StartTree(self):
        for i in range(self.seconds): 
            for color in self.colors:
                self.tree.color = color
                self.tree[self.topLed].color = (1, 1, 1)
                val = random()/10
                sleep(val)
        self.SwitchOff()

    def SwitchOff(self):
        self.tree.off()
