import random
import simple_graphics as sg

# =====================================================================
# THE SAND FUNCTION (Using only your exact framework functions)
# =====================================================================
def draw_sand(y_position, height, num_dots=300):
    """
    Draws a sand-colored rectangle with scattered black dots to look like texture.
    
    Parameters:
    - y_position: Where the top of the sand rectangle starts vertically.
    - height: How tall the sand rectangle is.
    - num_dots: How many black sand specks to scatter around.
    """
    canvas_width = int(sg._canvas['width'])
    
    # Define sand colors
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


# =====================================================================
# EXECUTING BOTH TOGETHER IN THE RENDERING WORKSPACE
# =====================================================================
def student_rendering(width, height):
    """Main drawing workspace."""
    # Set background sky
    sg.fill_background("white")
    
    # 1. Draw the waves in the upper/middle section
    draw_ocean_waves(num_waves=7, wave_thickness=80)
    
    # 2. Draw the sand layer right below the wave base
    # We start it exactly where the wave base sits (height * 0.5) 
    # and make it fill up the rest of the bottom of the screen.
    sand_start_y = int(height * 0.5) + 80
    sand_height = height - sand_start_y
    
    # Call the sand function with 400 dots scattered around
    draw_sand(y_position=sand_start_y, height=sand_height, num_dots=400)


if __name__ == "__main__":
    sg.start(student_rendering, width=800, height=600)
