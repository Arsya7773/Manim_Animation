from manim import *

'''class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fillx(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation
'''
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()

class CreateTriangle(Scene):
    def construct(self):
        triangle = Triangle()
        triangle.set_fill(RED, opacity=0.5)
        self.play(Create(triangle))

if __name__ == "__main__":
    scene = CreateTriangle()
    scene.render()

class AnimationText(Scene):
    def construct(self):

        teks1 = Text("I'm unbeatable")
        teks1.set_color(BLUE).shift(UR*3)

        teks2 = Text("WDYM").set_color(GREY)
        teks2.next_to(teks1, DOWN)


        self.add(teks1, teks2)