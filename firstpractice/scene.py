from manim import *

class FirstExample(Scene):
    def construct(self):
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        green_square = Square(color=GREEN, fill_opacity=0.8)
        green_square.next_to(blue_circle, RIGHT)
        self.add(green_square, blue_circle)

class SecondExample(Scene):
    def construct(self):
        ax = Axes(x_range=(-5, 5), y_range=(-5, 5))
        curve = ax.plot(lambda x: (x+2)*x*(x-2)/2, color=RED)
        area = ax.get_area(curve, x_range=(-2,0))
        self.play(Create(ax), Create(curve), run_time=3)
        self.play(FadeIn(area))
        self.wait(2)