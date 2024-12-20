from manim import *
import numpy as np

class TidalCurrentSimulation(Scene):
    def construct(self):
        # Buat latar belakang sederhana dengan garis pantai
        coastline = Line(start=LEFT*5, end=RIGHT*5, color=WHITE).shift(DOWN*2)
        coastline_label = Text("Garis Pantai", font_size=24).next_to(coastline, DOWN)
        self.play(Create(coastline), Write(coastline_label))
        
        # Fungsi untuk pola pergerakan partikel dengan arus pasang surut
        def tidal_motion(t):
            return np.sin(2 * PI * t) * RIGHT  # gerakan bolak-balik

        # Partikel-partikel di dekat pantai
        particles = VGroup(*[
            Dot(point=coastline.get_start() + RIGHT * (i * 1), color=BLUE)
            for i in range(10)
        ])

        # Tambahkan partikel ke layar
        self.play(FadeIn(particles))
        
        # Animasikan pergerakan partikel mengikuti pola arus pasang surut
        self.play(
            particles.animate.apply_complex_function(lambda x: np.exp(1j * np.pi / 6) * x),
            run_time=5,
            rate_func=there_and_back
        )
        
        # Animasi periodik untuk mensimulasikan arus pasang surut
        for _ in range(3):  # Ulangi beberapa kali untuk simulasi pergerakan
            self.play(
                particles.animate.apply_function(lambda p: p + tidal_motion(np.sin(PI))),
                run_time=2, rate_func=there_and_back
            )
        
        # Memberi jeda di akhir
        self.wait(2)
