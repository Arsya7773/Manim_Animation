from manim import *

class LineIntegrationWithPartitions(Scene):
    def construct(self):
        # Membuat sumbu koordinat kartesius
        axes = Axes(
            x_range=[-1, 5, 1],  # Rentang sumbu x dari -1 sampai 5
            y_range=[-1, 5, 1],  # Rentang sumbu y dari -1 sampai 5
            axis_config={"color": BLUE}
        )

        # Label sumbu x dan y
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Membuat grafik dari garis y = x
        graph = axes.plot(lambda x: x, color=YELLOW)

        # Menambahkan label persamaan pada grafik
        graph_label = MathTex("y = x").next_to(graph, UP, buff=0.01)

        # Parameter untuk area kecil
        num_partitions = 10  # Jumlah partisi
        width = 4 / num_partitions  # Lebar setiap partisi

        # Animasi
        self.play(Create(axes), Write(labels))  # Membuat sumbu kartesius dan label
        self.wait(1)

        # Animasi menggambar grafik
        self.play(Create(graph), Write(graph_label))
        self.wait(1)

        # Menggambar area di bawah kurva secara berpartisi
        for i in range(num_partitions):
            # Koordinat persegi panjang
            x_left = i * width
            x_right = (i + 1) * width
            rectangle = Rectangle(
                width=width,
                height=x_right,
                color=GREEN,
                fill_opacity=0.5
            ).move_to(axes.c2p((x_left + x_right) / 2, x_right / 2))

            # Animasi menampilkan setiap partisi
            self.play(FadeIn(rectangle))
            self.wait(0.001)

        # Mengakhiri animasi
        self.wait(2)
        self.play(FadeOut(graph), FadeOut(axes), FadeOut(labels), FadeOut(graph_label), FadeOut(rectangle))

class TypingIntegrationEquation(Scene):
    def construct(self):
        # Persamaan yang ingin dianimasikan
        equation = MathTex(
            r"\int u \, dv = uv \bigg|_{t_1}^{t_2} - \int v \, du"
        )

        # Animasi mengetik persamaan
        self.play(Write(equation))

        # Tunggu 2 detik untuk menampilkan hasil
        self.wait(2)

        # Menghilangkan persamaan
        self.play(FadeOut(equation))

class TypingComplexEquation(Scene):
    def construct(self):
        # Persamaan yang ingin dianimasikan
        equation = MathTex(
            r"""\int_{t_1}^{t_2} \frac{\partial L}{\partial \dot{q}} \, \frac{d}{dt} (\delta q) \, dt = \left[ \frac{\partial L}{\partial \dot{q}} \delta q \right]_{t_1}^{t_2} - \int_{t_1}^{t_2} \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) \delta q \, dt"""
        )

        # Animasi mengetik persamaan
        self.play(Write(equation))

        # Waktu tunggu agar persamaan tetap di layar sebelum animasi selesai
        self.wait(2)

        # Menghilangkan persamaan
        self.play(FadeOut(equation))
