import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Generateur.map import Map

class Render:
    def __init__(self, Map, options):
        self.map = Map
        self.options = options

    
    def render_map(self, Map, options):
        pass