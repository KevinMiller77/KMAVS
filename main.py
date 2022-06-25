import glfw
import OpenGL.GL as gl
import imgui
from imgui.integrations.glfw import GlfwRenderer

from widgets.sorter import SorterWidget

def main():
    imgui.create_context()
    window = glfw_init()
    impl = GlfwRenderer(window)
    lastFrameTime = glfw.get_time()

    sorter = SorterWidget()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        impl.process_inputs()

        now = glfw.get_time()
        dt = glfw.get_time() - lastFrameTime
        lastFrameTime = now

        imgui.new_frame()

        window_size = glfw.get_window_size(window)
        win_w, win_h = window_size[0], window_size[1]

        imgui.set_next_window_position(0, 0)
        imgui.set_next_window_size(win_w, win_h)
        imgui.begin("Viewport", False, imgui.WINDOW_NO_TITLE_BAR)

        sorter.draw(dt)
        
        imgui.end()

        gl.glClearColor(.3, .3, .3, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.render()
        impl.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    impl.shutdown()
    glfw.terminate()


def glfw_init():
    if not glfw.init():
        print('Could not initialize OpenGl context')
        exit(1)

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window_name = 'Visualizer - Made by Kevin Miller'
    
    window = glfw.create_window(
        1288, 720, window_name, None, None 
    )
    glfw.make_context_current(window)

    if not window:
        glfw.terminate()
        print('Could not initialize glfw')
        exit(1)

    return window



if __name__ == "__main__":
    main()