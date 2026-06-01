import math
import simple_graphics as sg

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
