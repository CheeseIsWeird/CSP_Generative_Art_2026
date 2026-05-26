import simple_graphics as sg

def draw_picture(width, height):
# SKY
    sky_height = height * 3/8

    sg.set_fill_color("skyblue")
    sg.fill_rectangle(0, 0, width, sky_height)

#OCEAN
    ocean_y = sky_height
    ocean_height = height - ocean_y

    sg.set_fill_color("deepskyblue")
    sg.fill_rectangle(0, ocean_y, width, ocean_height)

#SUN
    sun_radius = height / 4

    sun_center_x = width / 2
    sun_center_y = sky_height

    sg.set_fill_color("yellow")

#Draw top half of circle
    sg.fill_arc(
        sun_center_x - sun_radius,
        sun_center_y - sun_radius,
        sun_radius * 2,
        sun_radius * 2,
        0,
        180
    )

#CLOUDS
    
    sg.set_fill_color("white")

    #Cloud 1
    sg.fill_circle(120, 80, 25)
    sg.fill_circle(150, 70, 30)
    sg.fill_circle(180, 80, 25)

    #Cloud 2
    sg.fill_circle(420, 100, 20)
    sg.fill_circle(445, 90, 28)
    sg.fill_circle(475, 100, 20)

#BIRDS
    sg.set_outline_color("black")
    sg.set_line_thickness(2)

    #Bird 1
    sg.draw_line(250, 70, 260, 60)
    sg.draw_line(260, 60, 270, 70)

    #Bird 2
    sg.draw_line(320, 90, 330, 80)
    sg.draw_line(330, 80, 340, 90)

    #Bird 3
    sg.draw_line(500, 60, 510, 50)
    sg.draw_line(510, 50, 520, 60)


if __name__ == "__main__":
    sg.start(draw_picture, 600, 400)
