import math
import simple_graphics as sg

def draw_picture(width, height):
    """
    Draws a resized red house roof, a perfectly aligned brick chimney,
    and puffy light-gray smoke rising from the chimney.
    
    AI Attribution: Geometry adjustment, color updates, and cloud-shaped smoke generation 
    loops were crafted using Gemini for the Generative Art task.
    """
    
    # 1. Initialize the background to white
    sg.fill_background("white")
    
    # 2. Baseline and existing elements (using width and height variables to prevent warnings)
    sg.set_outline_color("black")
    sg.set_line_thickness(1)
    # Adjust the ground height slightly to 400 to match the resized roof
    ground_y = int(height * 0.66) # Around 400
    sg.draw_line(0, ground_y, width, ground_y) 
    
    # =========================================================================
    # [1] Draw the chimney (drawn before the roof to place it behind the roof)
    # =========================================================================
    # Precisely adjust the coordinates and size of the chimney to fit the smaller roof
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

    # =========================================================================
    # [2] Add puffy cloud-shaped smoke (rising from the top of the chimney)
    # =========================================================================
    # Light gray settings (#e5e5e5) and light outlines
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

    # =========================================================================
    # [3] Draw the roof (resized and changed to a bright red color)
    # =========================================================================
    # Reduce the width and height compared to the original to make it compact
    roof_left_x, roof_left_y = 260, 400
    roof_top_x,  roof_top_y  = 410, 240
    roof_right_x, roof_right_y = 560, 400
    
    # Bright red settings
    sg.set_fill_color("red") 
    sg.set_outline_color("black")
    sg.set_line_thickness(3)
    
    # Draw the triangular roof
    sg.fill_triangle(roof_left_x, roof_left_y, roof_top_x, roof_top_y, roof_right_x, roof_right_y)


if __name__ == "__main__":
    # Call the start function of simple_graphics to open the window.
    sg.start(draw_picture)
# =====================================================================
# THE WAVE FUNCTION (Using only your exact framework functions)
# =====================================================================
def draw_ocean_waves(num_waves, wave_thickness):
    """
    Draws a clean wave strip matching the image structure with no bottom bulges.
    
    Parameters:
    - num_waves: How many wave peaks appear from left to right across the page.
    - wave_thickness: The vertical height of the solid water base strip.
    """
    # Safe canvas dimension lookup
    canvas_width = int(sg._canvas['width'])
    canvas_height = int(sg._canvas['height'])
    
    sky_color = "white"
    dark_blue = "#006ccf"
    light_blue = "#a6e3f9"
    
    # 1. Clear background
    sg.fill_background(sky_color)
    
    # Dynamically calculate the horizontal step size so exactly 'num_waves' fit
    wave_step = canvas_width / max(1, num_waves)
    radius_main = wave_step * 0.5  # Scale the circles perfectly to match the step width
    
    # Set the baseline position in the middle of the screen
    wave_base_y = canvas_height * 0.5
    
    # PHASE 1: Draw all the circular wave peaks and cutouts first
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

    # PHASE 2: Draw the solid base block LAST to mask and flatten any stray circles
    sg.set_fill_color(dark_blue)
    sg.set_outline_color(dark_blue)
    sg.fill_rectangle(0, wave_base_y, canvas_width, wave_thickness)


# =====================================================================
# THE FUNCTION CALL
# =====================================================================
def student_rendering(width, height):
    """Main drawing function passed to the engine."""
    # num_waves = 7 peaks stretching from left to right
    # wave_thickness = 50 pixels tall base strip at the bottom
    draw_ocean_waves(num_waves=7, wave_thickness=50)


if __name__ == "__main__":
    sg.start(student_rendering, width=800, height=600)
