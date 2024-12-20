from manim import *

class LocalVsConvectiveAcceleration(Scene):
    def construct(self):
        # Membuat grid atau latar belakang aliran fluida
        flow_field = VGroup()
        for x in range(-12, 7):
            for y in range(-12, 4):
                # Membuat panah kecepatan yang berubah seiring posisi x (gradien kecepatan)
                arrow = Arrow(
                    start=[x, y, 0], 
                    end=[x + 0.5 + 0.05 * x, y, 0],  # gradien kecepatan sesuai posisi x
                    buff=0, 
                    color=BLUE
                )
                flow_field.add(arrow)
        
        # Menampilkan medan aliran fluida
        self.play(Create(flow_field))
        
        # Menambahkan partikel
        particle = Dot(point=[-4, 0, 0], color=YELLOW)
        particle_label = Text("Partikel", font_size=24).next_to(particle, UP)
        self.play(FadeIn(particle, particle_label))

        # Teks untuk menjelaskan percepatan lokal dan konvektif
        explanation_text = Text(
            "Percepatan Lokal & Konvektif",
            font_size=30
        ).to_edge(UP)
        self.play(Write(explanation_text))

        # Membuat percepatan lokal (partikel diam tetapi medan aliran berubah)
        local_acceleration_text = Text("Percepatan Lokal", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Write(local_acceleration_text))
        
        # Tampilkan gaya yang bekerja
        self.play(FadeOut(particle_label))
        self.wait(1)

        # Mengubah arah panah untuk menunjukkan perubahan kecepatan di posisi tetap
        self.play(*[arrow.animate.shift(RIGHT * 0.4) for arrow in flow_field], run_time=4)
        self.wait(1)
        
        # Hapus teks percepatan lokal
        self.play(FadeOut(local_acceleration_text))
        
        # Membuat percepatan konvektif (partikel bergerak melewati gradien kecepatan)
        convective_acceleration_text = Text("Percepatan Konvektif", font_size=24, color=RED).to_edge(DOWN)
        self.play(Write(convective_acceleration_text))
        
        # Gerakkan partikel ke kanan melintasi gradien kecepatan
        self.play(particle.animate.shift(RIGHT * 8), run_time=4)
        
        # Diamkan partikel setelah bergerak
        self.wait(1)
        
        # Menghilangkan semuanya
        self.play(FadeOut(convective_acceleration_text), FadeOut(particle), FadeOut(flow_field), FadeOut(explanation_text))
