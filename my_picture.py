import simple_graphics as sg

def draw_picture(width, height):

    # Wall
    sg.set_fill_color("lightgray")
    sg.fill_rectangle(100, 100, 600, 350)


# Start drawing
sg.start(draw_picture)
