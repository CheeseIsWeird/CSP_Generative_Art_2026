import simple_graphics as sg

def draw_picture(width, height):

    # Wall
    sg.set_fill_color("lightgray")
    sg.fill_rectangle(100, 100, 600, 350)

    # Door
    sg.set_fill_color("brown")
    sg.fill_rectangle(350, 250, 120, 200)

    # Door Handle
    sg.set_fill_color("gold")
    sg.fill_circle(450, 350, 7)

    # Window
    sg.set_fill_color("")
    sg.fill_rectangle(170, 170, 140, 120)

    # Window frame
    sg.set_outline_color("black")
    sg.set_line_thickness(3)

    sg.draw_line(240, 170, 240, 290)
    sg.draw_line(170, 230, 310, 230)

# Start drawing
sg.start(draw_picture)
