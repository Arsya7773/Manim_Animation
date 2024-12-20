from manim import *

class InertiaDemo(Scene):
    def construct(self):
        # Buat sistem koordinat tetap
        axes = Axes(
            x_range=[-5, 5, 1], 
            y_range=[-3, 3, 1], 
            axis_config={"include_numbers": True}
        )
        self.play(Create(axes))
        
        # Buat partikel di pusat koordinat
        particle = Dot(point=axes.c2p(0, 0), color=BLUE)
        particle_label = Text("Partikel", font_size=24).next_to(particle, UP)
        self.play(FadeIn(particle, particle_label))
        
        # Teks untuk menjelaskan inersia
        inertia_text = Text(
            "Inersia: Partikel tetap diam hingga gaya bekerja padanya",
            font_size=24
        ).to_edge(UP)
        self.play(Write(inertia_text))

        # Partikel diam selama beberapa waktu
        self.wait(2)
        
        # Menambahkan vektor gaya untuk menunjukkan gaya eksternal
        force_arrow = Arrow(
            start=particle.get_center(),
            end=particle.get_center() + RIGHT,
            buff=0,
            color=RED
        )
        force_text = Text("Gaya", font_size=24, color=RED).next_to(force_arrow, UP)
        
        # Menampilkan gaya
        self.play(GrowArrow(force_arrow), FadeIn(force_text))
        self.wait(1)
        
        # Gerakkan partikel akibat gaya
        self.play(particle.animate.shift(RIGHT * 3), run_time=2)
        
        # Hapus gaya setelah bekerja
        self.play(FadeOut(force_arrow), FadeOut(force_text))
        
        # Diamkan partikel di posisi barunya
        self.wait(2)

        # Animasi selesai
        self.play(FadeOut(particle), FadeOut(particle_label), FadeOut(inertia_text), FadeOut(axes))
