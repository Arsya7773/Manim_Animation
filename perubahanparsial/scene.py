from manim import *

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