import imgui
from algos.algos import algos_map
from imgui_helpers import centered_float_slider, centered_text

class SorterWidget:
    def __init__(self):
        self.sort_name = None
        self.sorter = None

        # Time step info
        self.step = 0.5
        self.time_since_step = 0

    def draw_selection(self):
        message = "Please select an algorithm below for a visualizer!"
        centered_text(message)

        but_size = imgui.get_window_size().x / 4
        imgui.columns(4)
        for algo_type in algos_map:
            if imgui.button(algo_type, but_size, but_size):
                self.sort_name = algo_type
                self.sorter = algos_map[algo_type]()
                return
            imgui.spacing()
            
            imgui.next_column()


    def draw(self, dt):
        if self.sorter is None:
            self.draw_selection()
            return
        
        centered_text(self.sort_name + " Visualizer")

        if imgui.button("Return"):
            self.sorter = None
            return
        imgui.same_line()


        self.time_since_step = self.time_since_step + dt

        if(self.step != 0 and self.time_since_step >  1 / self.step):
            self.sorter.frame_step()
            self.time_since_step = 0

        
        self.step = centered_float_slider(self.step, 0, 1000)
        imgui.same_line()

        # Buttons next to each other
        if imgui.button("Step"):
            self.sorter.frame_step()
        imgui.same_line()

        if imgui.button("Reset"):
            self.sorter.reset()
        imgui.same_line()

        if imgui.button("New/Clear"):
            self.sorter.new_set()
        imgui.spacing()

        self.sorter.draw(dt)



