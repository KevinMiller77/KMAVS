import random
import imgui
from array import array
from algos.algo_base import AlgoBase

from utils.imgui_helpers import *

class QuickSorter(AlgoBase):
    def __init__(self, items = []):
         # Keyframe/Ani info 
        self.keyframes = []
        self.cur_frame = 0

        # List items info
        l = items
        if(len(l) == 0):
            l = [random.randint(0, 1000) for i in range(0, 100)]

        self.original = l.copy()
        self.sorted = l.copy()
        self.display = array("f", l)

        # Perform sort so we have keys
        self.__begin()
    
    def frame_step(self):
        for i in range(0, 2):
            if(self.cur_frame >= len(self.keyframes)):
                return

            frame = self.keyframes[self.cur_frame]
            l, r = frame[0], frame[1]

            self.display[l] = float(r)

            self.cur_frame = self.cur_frame + 1
    
    def reset(self):
        self.display = array("f", self.original)
        self.cur_frame = 0

    def new_set(self):
        self.__init__()

    def draw(self, dt):
        cr = imgui.core.get_window_content_region_max()
        h = cr.y - imgui.core.get_cursor_pos().y - 15 # 15 is nice breathe room

        imgui.plot_histogram("", self.display, graph_size = (cr.x, h))  

    # Algorithm things here
    def __begin(self):
        self.__do_sort(self.sorted, 0, len(self.sorted) - 1)
    
    def __do_sort(self, arr: list, l: int, r: int):
        if len(arr) == 1:
            return
        
        if l < r:
            p = self.__partition(arr, l, r)
            self.__do_sort(arr, l, p - 1)
            self.__do_sort(arr, p + 1, r)


    def __partition(self, arr: list, l: int, r:int):
        piv, p = arr[r], l
        for i in range(l, r):
            if arr[i] <= piv:
                # Swap
                self.keyframes.append([i, arr[p]])
                self.keyframes.append([p, arr[i]])
                arr[i], arr[p] = arr[p], arr[i]
                p = p + 1
        
        # Swap the last
        self.keyframes.append([p, arr[r]])
        self.keyframes.append([r, arr[p]])

        arr[p], arr[r] = arr[r], arr[p]
        return p
    