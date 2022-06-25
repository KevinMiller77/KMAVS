import imgui
from algos.algos import algos_map
from imgui_helpers import centered_text

class SorterWidget:
    def __init__(self):
        self.sort_name = None
        self.sorter = None

    def draw_selection(self):
        message = "Please select an algorithm below for a visualizer!"
        centered_text(message)

        for algo_type in algos_map:
            if imgui.button(algo_type):
                self.sort_name = algo_type
                self.sorter = algos_map[algo_type]()
                return

    def draw(self, dt):
        if self.sorter is None:
            self.draw_selection()
            return
        
        centered_text(self.sort_name + " Visualizer")

        if imgui.button("Return"):
            self.sorter = None
            return
        imgui.same_line()

        self.sorter.draw(dt)



