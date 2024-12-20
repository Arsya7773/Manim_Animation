from manim import *
import numpy as np

class RotatingVsFixed(Scene):
    def construct(self):
        # Sistem koordinat tetap
        fixed_axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE},
        ).shift(LEFT * 3.5)

        # Sistem koordinat berotasi
        rotating_axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE},
        ).shift(RIGHT * 3.5)

        # Label
        fixed_label = Text("Sistem Koordinat Tetap", font_size=24).next_to(fixed_axes, UP)
        rotating_label = Text("Sistem Koordinat Berotasi", font_size=24).next_to(rotating_axes, UP)

        # Partikel
        fixed_particle = Dot(color=YELLOW).move_to(fixed_axes.c2p(-4, 0))
        rotating_particle = Dot(color=RED).move_to(rotating_axes.c2p(-4, 0))

        # Lintasan lurus dalam sistem tetap
        fixed_path = Line(fixed_axes.c2p(-4, 0), fixed_axes.c2p(4, 0), color=YELLOW)

        # Lintasan melengkung dalam sistem berotasi (efek Coriolis)
        def coriolis_path(t):
            x = -4 + 8 * t  # Gerakan ke kanan
            y = 0.5 * np.sin(4 * np.pi * t)  # Lintasan melengkung untuk simulasi gaya Coriolis
            return rotating_axes.c2p(x, y)

        rotating_path = ParametricFunction(coriolis_path, t_range=[0, 1], color=RED)

        # Animasikan lintasan partikel
        self.play(Create(fixed_axes), Create(rotating_axes))
        self.play(Write(fixed_label), Write(rotating_label))

        # Partikel bergerak dalam lintasan tetap (lurus)
        self.play(Create(fixed_path), MoveAlongPath(fixed_particle, fixed_path), run_time=4)

        # Partikel bergerak dalam lintasan berotasi (melengkung)
        self.play(Create(rotating_path), MoveAlongPath(rotating_particle, rotating_path), run_time=4)

        # Tunggu sejenak untuk menunjukkan perbedaan
        self.wait(2)
