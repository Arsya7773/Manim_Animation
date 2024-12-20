from manim import *

class ZoomInWithParameters(Scene):
    def construct(self):
        # Membuat partikel (sebuah titik kecil)
        particle = Dot(color=BLUE)
        
        # Menambahkan label pada partikel
        label = Text("Partikel", font_size=24).next_to(particle, DOWN)
        
        # Menambahkan teks parameter suhu, kecepatan, dan salinitas (belum muncul)
        temperature_text = Text("Suhu", font_size=24).shift(UP * 2 + LEFT * 2)
        velocity_text = Text("Kecepatan", font_size=24).shift(UP * 2 + RIGHT * 2)
        salinity_text = Text("Salinitas", font_size=24).shift(DOWN * 2)

        # Membuat tanda panah yang mengarah ke partikel
        temperature_arrow = Arrow(start=temperature_text.shift(DOWN * 2), end=particle.shift(LEFT * 2), color=YELLOW)
        velocity_arrow = Arrow(start=RIGHT, end=particle.get_center(), color=RED)
        salinity_arrow = Arrow(start=DOWN, end=particle.get_center(), color=GREEN)
        
        # Menambahkan partikel dan label ke dalam scene
        self.play(FadeIn(particle), Write(label))
        
        # Animasi penghilangan label
        self.play(FadeOut(label), run_time=1)
        
        # Animasi Zoom In (partikel diperbesar)
        self.play(particle.animate.scale(10), run_time=3)
        
        # Setelah partikel diperbesar, munculkan teks dan panah
        self.play(Write(temperature_text), Write(velocity_text), Write(salinity_text))
        self.play(GrowArrow(temperature_arrow), GrowArrow(velocity_arrow), GrowArrow(salinity_arrow))
        
        # Menunggu beberapa detik setelah semua selesai
        self.wait(2)
