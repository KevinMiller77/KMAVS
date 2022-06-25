import imgui

def centered_text(text: str):
    winW = imgui.get_window_size().x
    textW = imgui.calc_text_size(text).x

    imgui.set_cursor_pos_x((winW - textW) * 0.5)
    imgui.text(text)


def centered_float_slider(val: float, min: float, max: float, precision: str = "%.2f") -> float:
    """ Only works if the slider is the only thing on the line and has no label"""
    winW = imgui.get_window_size().x
    
    # if (winW < )
    # print(winW)

    imgui.set_cursor_pos_x(float(winW) * 0.35 * 0.5)
    # imgui.push_item_width(float(winW) * 0.45)
    c, v = imgui.slider_float("", val, min, max, precision)

    return v
