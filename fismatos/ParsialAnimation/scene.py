from manim import *

class WriteEquation(Scene):
    def construct(self):
        # Persamaan pertama
        equation_1 = MathTex(
            r"S[q(t)] = \int_{t_1}^{t_2} L(q(t), \dot{q}(t), t) \, dt"
        ).shift(UP * 2)
        # Persamaan kedua
        equation_2 = MathTex(
            r"\delta S = \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} \delta q + \frac{\partial L}{\partial \dot{q}} \delta \dot{q} \right) dt"
        ).next_to(equation_1, DOWN, buff=2)

        # Buat panah di antara kedua persamaan
        arrow = Arrow(
            equation_1.get_bottom(),  # Titik awal panah dari bawah persamaan pertama
            equation_2.get_top(),     # Titik akhir panah ke atas persamaan kedua
            buff=0.3  # Memberikan sedikit jarak antara panah dan persamaan
        )

        # Animasi mengetik persamaan pertama
        self.play(Write(equation_1))
        self.wait(0.5)

        # Animasi menampilkan panah di antara persamaan
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Animasi mengetik persamaan kedua
        self.play(Write(equation_2))
        self.wait(2)

class TypingEquation(Scene):
    def construct(self):
        # Persamaan yang ingin dianimasikan
        equation = MathTex(
            r"\delta \dot{q}(t) = \frac{d}{dt} (\delta q(t))"
        )

        # Animasi mengetik persamaan
        self.play(Write(equation))

        # Waktu tunggu agar persamaan tetap di layar sebelum animasi selesai
        self.wait(2)
