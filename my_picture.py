import simple_graphics as sg

def draw_picture(width, height):

    # Wall
    sg.set_fill_color("lightgray")
    sg.fill_rectangle(100, 100, 600, 350)

    # Door
    sg.set_fill_color("brown")
    sg.fill_rectangle(350, 250, 120, 200)

# Start drawing
sg.start(draw_picture)
