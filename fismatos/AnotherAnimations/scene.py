from manim import *

class BoundaryTerms(Scene):
    def construct(self):
        # Titles
        title = Text("Suku Batas Menghilang Ketika δq(t1) = δq(t2) = 0").scale(0.8)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        
        # Axes for graph
        axes = Axes(
            x_range=[0, 10, 1], y_range=[-2, 2, 1],
            axis_config={"include_tip": True},
            x_length=7, y_length=3
        )
        axes_labels = axes.get_axis_labels(x_label="t", y_label="q")
        
        # Time points t1 and t2
        t1_label = MathTex("t_1").next_to(axes.c2p(1, 0), DOWN)
        t2_label = MathTex("t_2").next_to(axes.c2p(9, 0), DOWN)
        
        # Dots for t1 and t2
        t1_dot = Dot(axes.c2p(1, 0), color=RED)
        t2_dot = Dot(axes.c2p(9, 0), color=RED)
        
        # Dashed lines to t-axis
        t1_dashed_line = DashedLine(axes.c2p(1, -2), axes.c2p(1, 2), color=YELLOW)
        t2_dashed_line = DashedLine(axes.c2p(9, -2), axes.c2p(9, 2), color=YELLOW)
        
        # Plot the function delta q(t) vanishing at t1 and t2
        delta_q_graph = axes.plot(lambda t: 0.5 * (t - 1) * (9 - t) / 10, color=BLUE)
        
        # Labels for δq(t1) = 0 and δq(t2) = 0
        delta_q_t1_label = MathTex("\\delta q(t_1) = 0", color=YELLOW).next_to(t1_dot, LEFT)
        delta_q_t2_label = MathTex("\\delta q(t_2) = 0", color=YELLOW).next_to(t2_dot, RIGHT)
        
        # Animate graph setup
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(t1_dashed_line), Create(t2_dashed_line))
        self.play(FadeIn(t1_dot, t2_dot))
        self.play(Write(t1_label), Write(t2_label))
        self.play(Create(delta_q_graph))
        self.play(Write(delta_q_t1_label), Write(delta_q_t2_label))
        
        # Show how boundary terms vanish
        boundary_term = MathTex("\\left[ \\frac{\\partial L}{\\partial \\dot{q}} \\delta q \\right]_{t_1}^{t_2} = 0").to_edge(DOWN)
        self.play(Write(boundary_term))
        
        self.wait(3)

class TTR(Scene):
    def construct(self):
        # Persamaan yang ingin dianimasikan
        equation = Tex(
            r"$\delta S = \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) \right) \delta q \, dt$"
        ).scale(1.2)

        # Animasi mengetik persamaan
        self.play(Write(equation))

        # Tunggu 2 detik untuk menampilkan hasil
        self.wait(2)

        # Menghilangkan persamaan
        self.play(FadeOut(equation))
