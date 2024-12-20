from manim import *

class EulerLagrangeAnimation(Scene):
    def construct(self):
        # Membuat dua persegi di kiri dan kanan
        square_left = Square(side_length=2).to_edge(LEFT, buff=2)
        square_right = Square(side_length=2).to_edge(RIGHT, buff=2)
        
        # Label Euler dan Lagrange
        euler_label = Text("Euler").next_to(square_left, UP)
        lagrange_label = Text("Lagrange").next_to(square_right, UP)
        
        # Teks "VS" di tengah
        vs_label = Text("VS").scale(1.5).move_to(ORIGIN)
        
        # Membuat partikel di kiri yang bergerak dari kiri ke kanan (Euler)
        particle_left = Dot(color=BLUE).move_to(square_left.get_left())
        particle_left_path = Line(square_left.get_left(), square_left.get_right())

        # Membuat partikel di kanan (Lagrange), yang akan mengikuti persegi di kanan
        particle_right = Dot(color=RED).move_to(square_right.get_center())
        
        # Menambahkan semua objek ke scene
        self.play(Create(square_left), Create(square_right))
        self.play(Write(euler_label), Write(lagrange_label), Write(vs_label))
        self.add(particle_left, particle_right)

        # Animasi pergerakan partikel dari kiri ke kanan, dan persegi kanan bergerak
        self.play(
            MoveAlongPath(particle_left, particle_left_path, rate_func=linear),
            # Persegi kanan dan partikel kanan bergerak bersama
            square_right.animate(rate_func=linear).shift(RIGHT*2),
            particle_right.animate(rate_func=linear).shift(RIGHT*2),
            run_time=4
        )
        
        # Memberikan sedikit jeda sebelum animasi selesai
        self.wait()

class IntegralEquation(Scene):
    def construct(self):
        # Menampilkan persamaan awal (integral pertama)
        integral_left = MathTex(r"\int_{\text{CV}} \rho \, dV")
        integral_right = MathTex(r"= \int_{\text{CV}} \frac{\partial \rho}{\partial t} \, dV + \int_{\text{CS}} \rho (\mathbf{v} \cdot \hat{n}) \, dA")
        
        # Gabungkan kedua bagian persamaan
        full_equation = VGroup(integral_left, integral_right).arrange(RIGHT)  # Menggabungkan kedua bagian
        
        # Posisikan di tengah layar
        full_equation.move_to(ORIGIN)

        # Animasikan persamaan
        self.play(Write(full_equation))