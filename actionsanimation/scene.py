from manim import *

class MoveLeftToRightAndBack(Scene):
    def construct(self):
        # Buat lingkaran untuk mewakili objek
        man = Circle().set_color(YELLOW).set_fill(YELLOW, opacity=1.0)  # Lingkaran dengan warna biru dan isi kuning
        
        # Tempatkan objek di tepi kiri
        man.to_edge(LEFT)
        
        # Animasi gerak dari kiri ke kanan
        self.play(man.animate.shift(RIGHT * 11), run_time=4)
        
        # Tunggu sebentar
        self.wait(1)
        
        # Animasi gerak dari kanan ke kiri (kembali)
        self.play(man.animate.shift(LEFT * 11), run_time=4)
        
        # Tetap tampilkan di layar setelah gerakan
        self.wait(1)

class TypingActionEquation(Scene):
    def construct(self):
        # Buat persamaan aksi dengan Tex
        action_equation = MathTex(
            "S = \\int_{t_1}^{t_2} L(q, \\dot{q}, t) \\, dt"
        )
        
        # Tampilkan persamaan satu per satu dengan efek typing
        for i in range(len(action_equation)):
            self.play(Write(action_equation[:i + 1]), run_time=1.25)
        
        # Tetap tampilkan persamaan selama 2 detik setelah selesai diketik
        self.wait(2)

class TypingAnimation(Scene):
    def construct(self):
        # Membuat teks yang ingin ditampilkan
        text = Text("Persamaan Variasi Aksi")
        
        # Menambahkan persamaan variasi aksi
        equation = MathTex(r"S = \int_{t_0}^{t_1} L(q, \dot{q}, t) dt")
        
        # Menampilkan persamaan dengan animasi mengetik
        self.play(Write(equation))
        
        # Menunggu beberapa saat untuk menampilkan persamaan
        self.wait(2)

        # Menghapus persamaan
        self.play(FadeOut(equation))

class TypingAnimation2(Scene):
    def construct(self):
        # Definisikan persamaan yang ingin ditampilkan
        equation1 = "\delta S = \int_{t_1}^{t_2} \left( \frac{\partial q}{\partial L} \delta q + \frac{\partial \dot{q}}{\partial L} \delta \dot{q} \right) dt"
        equation2 = "\delta S = \int_{t_1}^{t_2} \left( \frac{\partial q}{\partial L} - \frac{d}{dt} \left( \frac{\partial \dot{q}}{\partial L} \right) \right) \delta q \, dt + \left[ \frac{\partial \dot{q}}{\partial L} \delta q \right]_{t_1}^{t_2}"
        
        # Menampilkan persamaan pertama dengan animasi mengetik
        self.type_equation(equation1, position=UP)
        self.wait(2)
        
        # Menghapus persamaan pertama
        self.clear()
        
        # Menampilkan persamaan kedua dengan animasi mengetik
        self.type_equation(equation2, position=DOWN)
        self.wait(2)

    def type_equation(self, equation, position):
        # Membuat teks dengan efek mengetik
        equation_text = MathTex(equation).move_to(position)
        self.play(Write(equation_text))
        self.wait(1)
