from manim import *
import numpy as np

class OceanCurrentSimulation(Scene):
    def construct(self):
        # Membuat partikel sebagai lingkaran kecil
        num_particles = 50  # Jumlah partikel
        particles = VGroup(*[Dot(radius=0.05, color=BLUE) for _ in range(num_particles)])

        # Posisi awal partikel
        for particle in particles:
            particle.move_to(self.random_point_in_circle(radius=3))  # Sebar di area lingkaran

        # Tambahkan updater untuk gerakan partikel
        for particle in particles:
            start_pos = particle.get_center()
            particle.add_updater(self.create_updater(start_pos))

        # Tambahkan partikel ke scene dan jalankan animasi
        self.add(particles)
        self.wait(10)  # Durasi animasi
        # Hapus updater setelah selesai
        for particle in particles:
            particle.clear_updaters()

    def random_point_in_circle(self, radius):
        """Menghasilkan titik acak dalam lingkaran"""
        angle = np.random.uniform(0, 2 * np.pi)
        r = radius * np.sqrt(np.random.uniform(0, 1))
        return np.array([r * np.cos(angle), r * np.sin(angle), 0])

    def create_updater(self, start_point):
        """Mengembalikan fungsi updater untuk pola arus laut"""
        def updater(mob, dt):
            time = self.time_tracker.increment_value(dt)  # Waktu dihitung dengan tracker
            x, y, z = start_point
            # Pola arus laut: kombinasi sinusoidal + gerakan melingkar
            new_pos = np.array([
                x + 0.5 * np.sin(time + y),  # Gerakan horizontal sinusoidal
                y + 0.3 * np.cos(time + x),  # Gerakan vertikal sinusoidal
                z
            ])
            mob.move_to(new_pos)
        return updater

    def setup(self):
        """Persiapan tracker waktu"""
        self.time_tracker = ValueTracker(0)  # Inisialisasi waktu
