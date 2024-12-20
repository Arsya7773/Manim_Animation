from manim import *

class SimpleEulerLagrange(Scene):
    def construct(self):
        # Tampilkan judul
        title = Tex(r"Persamaan Euler-Lagrange").scale(1.5).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Persamaan Euler-Lagrange
        equation = MathTex(
            r"\frac{\partial L}{\partial q}",
            r"-",
            r"\frac{d}{dt}",
            r"\left( \frac{\partial L}{\partial \dot{q}} \right)",
            r"= 0"
        ).scale(1.5)

        # Tampilkan persamaan Euler-Lagrange
        self.play(Write(equation))
        self.wait(2)

        # Sorot bagian-bagian persamaan dengan animasi .animate
        self.play(equation[0].animate.set_color(BLUE))  # Highlight ∂L/∂q
        self.wait(1)
        self.play(equation[2].animate.set_color(GREEN))  # Highlight d/dt
        self.wait(1)
        self.play(equation[3].animate.set_color(YELLOW))  # Highlight ∂L/∂q̇
        self.wait(2)

        # Fade out semua
        self.play(FadeOut(VGroup(equation, title)))
        self.wait(1)
