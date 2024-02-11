from manim import *

class Heart(Scene):
    def construct(self):
        # Parametric function for the heart shape
        def heart_curve(t):
            x = 16 * (np.sin(t) ** 3)
            y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
            return np.array([x, y, 0])

        # Create ParametricFunction object using the heart curve function
        heart_curve_obj = ParametricFunction(heart_curve, t_range=[0, TAU], color=RED)

        # Create a smaller heart
        def smaller_heart_curve(t):
            x = 8 * (np.sin(t) ** 3)
            y = 6.5 * np.cos(t) - 2.5 * np.cos(2*t) - np.cos(3*t) - 0.5 * np.cos(4*t)
            return np.array([x, y, 0])

        smaller_heart_curve_obj = ParametricFunction(smaller_heart_curve, t_range=[0, TAU], color=PINK)

        # Display the heart shapes
        self.play(Create(heart_curve_obj))
        self.wait()

        # Color the larger heart red
        heart_curve_obj.set_color(RED)

        # Draw the smaller heart and color it darker red
        self.play(Create(smaller_heart_curve_obj))
        self.wait()
        smaller_heart_curve_obj.set_color(PINK)

# Render the scene
# if __name__ == "__main__":
#     renderer = "opengl" # Use "cairo" if you encounter issues with opengl
#     resolution = (800, 600)
#     file_name = "heart_shapes"
#     scene = Heart()
#  
#manim -pql heart.py Heart