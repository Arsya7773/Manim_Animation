from manim import *
import numpy as np

class WavySurfaceWithParticles(ThreeDScene):
    def construct(self):
        resolution_fa = 24
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        # Fungsi gelombang dengan efek sinusoidal berdasarkan waktu
        def wavy_surface(u, v, t=0):
            x = u
            y = v
            sigma, mu = 0.4, [0.0, 0.0]
            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = np.exp(-(d ** 2 / (2.0 * sigma ** 2))) * np.sin(2 * np.pi * d - t)
            return np.array([x, y, z])

        # Membuat permukaan yang diperbarui setiap frame
        surface = Surface(
            lambda u, v: wavy_surface(u, v, t=0),
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2],
        )
        surface.scale(2, about_point=ORIGIN)
        surface.set_style(fill_opacity=1, stroke_color=GREEN)
        surface.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)

        # Menambahkan partikel
        particle = Sphere(radius=0.1, color=RED)
        particle.move_to([0, 0, 0.5])  # Awal posisi partikel

        axes = ThreeDAxes()
        self.add(axes, surface, particle)

        # Animasi
        def update_surface(obj, dt):
            t = self.renderer.time  # Menggunakan waktu dari renderer
            obj.become(
                Surface(
                    lambda u, v: wavy_surface(u, v, t=t),
                    resolution=(resolution_fa, resolution_fa),
                    v_range=[-2, +2],
                    u_range=[-2, +2],
                ).set_style(fill_opacity=1, stroke_color=GREEN).set_fill_by_checkerboard(
                    ORANGE, BLUE, opacity=0.5
                )
            )

        def update_particle(obj, dt):
            # Mendapatkan posisi partikel berdasarkan gelombang
            t = self.renderer.time
            u, v = obj.get_center()[:2]
            new_z = wavy_surface(u, v, t=t)[2]
            obj.move_to([u, v, new_z + 0.2])  # Menggeser partikel sedikit di atas permukaan

        surface.add_updater(update_surface)
        particle.add_updater(update_particle)

        self.play(Create(axes), Create(surface), Create(particle))
        self.wait(10)
