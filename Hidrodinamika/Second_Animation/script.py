from manim import *

class InertialFrame(Scene):
    def construct(self):
        # Membuat sistem koordinat
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Menambahkan partikel di posisi tertentu
        particle = Dot(point=axes.coords_to_point(2, 2), color=RED)
        particle_label = Text("Partikel", font_size=24).next_to(particle, LEFT)


        # Menampilkan sistem koordinat dan partikel awal
        self.play(Create(axes), Write(labels))
        self.play(FadeIn(particle), Write(particle_label))
        self.wait(1)
        
        # Menambahkan gaya eksternal yang bekerja pada partikel
        force_arrow = Arrow(
            start=particle.get_center(),
            end=particle.get_center() + RIGHT * 2,
            buff=0,
            color=YELLOW
        )
        force_label = Text("Gaya Eksternal", font_size=24, color=YELLOW).next_to(force_arrow, UP)
        
        # Tampilkan gaya yang bekerja
        self.play(FadeOut(particle_label))
        self.wait(1)

        # Tampilkan gaya yang bekerja
        self.play(GrowArrow(force_arrow), Write(force_label))
        self.wait(1)
        
        # Partikel bergerak karena gaya eksternal
        self.play(particle.animate.shift(RIGHT * 2), run_time=2)
        self.wait(1)
        
        # Menghilangkan gaya setelah partikel bergerak
        self.play(FadeOut(force_arrow), FadeOut(force_label))
        self.wait(1)

        # Kesimpulan: Partikel kembali diam tanpa gaya
        no_force_label = Text("Tidak ada gaya, Partikel tetap diam", font_size=24, color=GREEN).next_to(particle, DOWN)
        self.play(Write(no_force_label))
        self.wait(2)