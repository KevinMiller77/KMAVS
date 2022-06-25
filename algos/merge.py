import random
import imgui
from array import array

from imgui_helpers import *

class MergeSorter:
    def __init__(self, items: list = []):
        
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

    # Should actually perform two steps, each step is only one swap
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
        if l < r:

            m = (l + (r - 1)) // 2

            self.__do_sort(arr, l, m)
            self.__do_sort(arr, m + 1, r)

            self.__merge(arr, l, m, r)

    def __merge(self, arr: list, l: int, m: int, r: int):
        _s = m + 1

        # If the merge is already done
        if(arr[m] <= m and _s <= r):
            return
        
        # Two indices pointing to respective arrays
        while (l <= m and _s <= r):
            #  If element 1 was correct
            if(arr[l] <= arr[_s]):
                l = l+1
            else:
                val = arr[_s]
                i = _s

                while (i != l):
                    arr[i] = arr[i - 1]
                    self.keyframes.append([i, arr[i - 1]])
                    i = i - 1

                arr[l] = val
                self.keyframes.append([l, val])

                # Update ptrs
                l = l + 1
                m = m + 1
                _s = _s + 1
    