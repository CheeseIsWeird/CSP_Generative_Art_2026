import random
import simple_graphics as sg
import math
def draw_ocean_waves(num_waves, wave_thickness):
    canvas_width = int(sg._canvas['width'])
    canvas_height = int(sg._canvas['height'])
    
    colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    sky_color = "white"
    dark_blue = "#006ccf"
    light_blue = "#a6e3f9"
    sg.fill_background(sky_color)
    wave_step = canvas_width / max(1, num_waves)
    radius_main = wave_step * 0.5
    
    wave_base_y = canvas_height * 0.5
    
    for i in range(int(num_waves) + 1):
        x = i * wave_step
        
        # 1. Main Dark Blue Wave Hump (Large Circle)
        sg.set_fill_color(dark_blue)
        sg.set_outline_color(dark_blue)
        sg.fill_circle(center_x=x, center_y=wave_base_y, radius=radius_main)
        
        # 2. Light Blue Crest Cap (Medium Circle shifted up and left)
        sg.set_fill_color(light_blue)
        sg.set_outline_color(light_blue)
        sg.fill_circle(center_x=x - (radius_main * 0.15), center_y=wave_base_y - (radius_main * 0.25), radius=radius_main * 0.7)
        
        # 3. Inner Dark Blue Overlay (Brings back the main color under the cap)
        sg.set_fill_color(dark_blue)
        sg.set_outline_color(dark_blue)
        sg.fill_circle(center_x=x - (radius_main * 0.1), center_y=wave_base_y - (radius_main * 0.15), radius=radius_main * 0.65)
        
        # 4. The "Hook" Cutout (White Circle carving out the right side)
        sg.set_fill_color(sky_color)
        sg.set_outline_color(sky_color)
        sg.fill_circle(center_x=x + (radius_main * 0.85), center_y=wave_base_y - (radius_main * 0.1), radius=radius_main * 0.6)
        
        # 5. Little Water Droplets inside the curve hollow
        sg.set_fill_color(light_blue)
        sg.set_outline_color(light_blue)
        sg.fill_circle(center_x=x + (radius_main * 0.1), center_y=wave_base_y - (radius_main * 0.2), radius=3)
        sg.fill_circle(center_x=x + (radius_main * 0.3), center_y=wave_base_y - (radius_main * 0.45), radius=2)
        sg.fill_circle(center_x=x + (radius_main * 0.45), center_y=wave_base_y - (radius_main * 0.15), radius=3)
        
    sg.set_fill_color(dark_blue)
    sg.set_outline_color(dark_blue)
    sg.fill_rectangle(0, wave_base_y, canvas_width, wave_thickness)

    
def draw_ocean(width, height):
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
    pass
    
    
def draw_top(width, height):
    # 1. Initialize the background to white
    sg.fill_background("white")
    
    # 2. Baseline and existing elements (using width and height variables to prevent warnings)
    sg.set_outline_color("black")
    sg.set_line_thickness(1)
    # Adjust the ground height slightly to 400 to match the resized roof
    ground_y = int(height * 0.66) # Around 400
    sg.draw_line(0, ground_y, width, ground_y) 

    chimney_x = 460
    chimney_y = 205
    chimney_w = 45
    chimney_h = 140
    
    # Chimney base body (red brick background color)
    sg.set_fill_color("#b33c24") 
    sg.set_outline_color("#5c1d10")
    sg.set_line_thickness(1)
    
    for i in range(chimney_h):
        sg.draw_line(chimney_x, chimney_y + i, chimney_x + chimney_w, chimney_y + i)
        
    # Add brick patterns to the chimney
    sg.set_outline_color("#dfa396") # Mortar color between bricks
    row_height = 10
    for y in range(chimney_y, chimney_y + chimney_h, row_height):
        sg.draw_line(chimney_x, y, chimney_x + chimney_w, y)
        
    shift = False
    for y in range(chimney_y, chimney_y + chimney_h, row_height):
        start_x = chimney_x + (6 if shift else 0)
        for x in range(start_x, chimney_x + chimney_w, 15):
            sg.draw_line(x, y, x, y + row_height)
        shift = not shift
        
    # Chimney Cap
    sg.set_outline_color("black")
    sg.set_line_thickness(1)
    for i in range(8): 
        sg.draw_line(chimney_x - 4, chimney_y + i, chimney_x + chimney_w + 4, chimney_y + i)
    sg.set_fill_color("#e5e5e5")
    sg.set_outline_color("#d0d0d0")
    sg.set_line_thickness(1)
    
    # Center coordinates of the chimney opening
    smoke_base_x = chimney_x + (chimney_w // 2)
    smoke_base_y = chimney_y - 2
    
    # Overlap multiple circles of increasing size to represent puffy rising smoke
    # (x_offset, y_offset, radius)
    smoke_circles = [
        (0, -8, 9),
        (-5, -18, 13),
        (7, -27, 15),
        (-4, -40, 19),
        (10, -53, 22),
        (-8, -70, 26),
        (12, -88, 28)
    ]
    
    for offset_x, offset_y, radius in smoke_circles:
        sg.fill_circle(smoke_base_x + offset_x, smoke_base_y + offset_y, radius)

    roof_left_x, roof_left_y = 260, 400
    roof_top_x,  roof_top_y  = 410, 240
    roof_right_x, roof_right_y = 560, 400
    
    # Bright red settings
    sg.set_fill_color("red") 
    sg.set_outline_color("black")
    sg.set_line_thickness(3)
    
    # Draw the triangular roof
    sg.fill_triangle(roof_left_x, roof_left_y, roof_top_x, roof_top_y, roof_right_x, roof_right_y)

def draw_sand(y_position, height, num_dots=300):
    canvas_width = int(sg._canvas['width']) 
    sand_color = "#eab308"  # A nice warm sandy yellow/gold hex
    dot_color = "black"
    
    # 1. Draw the solid sand rectangle base
    sg.set_fill_color(sand_color)
    sg.set_outline_color(sand_color)
    sg.fill_rectangle(0, y_position, canvas_width, height)
    
    # 2. Scatter the black textured specks randomly within the rectangle
    sg.set_fill_color(dot_color)
    sg.set_outline_color(dot_color)
    
    for _ in range(num_dots):
        # Pick a random coordinate inside the boundaries of the sand rectangle
        rand_x = random.randint(0, canvas_width)
        rand_y = random.randint(y_position, y_position + height)
        
        # Pick a random tiny radius (1 or 2 pixels) so the dots vary in size
        dot_radius = random.randint(1, 2)
        
        # Stamp the dot
        sg.fill_circle(center_x=rand_x, center_y=rand_y, radius=dot_radius)
        
def draw_bot(width, height):
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


def student_rendering(width, height):
    draw_ocean_waves(num_waves=7, wave_thickness=50)
    sand_start_y = int(height * 0.5) + 80
    sand_height = height - sand_start_y
    draw_sand(y_position=sand_start_y, height=sand_height, num_dots=400)


if __name__ == "__main__":
    sg.start(draw_ocean, 600, 400)
    sg.start(draw_top)
    sg.start(student_rendering, width=800, height=600)
    sg.start(draw_bot, width=800, height =600)
    
    

