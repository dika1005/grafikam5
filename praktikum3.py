import argparse
import matplotlib.pyplot as plt
import numpy as np


def gambar_persegi_panjang(titik, warna='b', label=None):
    """Gambar persegi panjang (4 titik) dan tutup poligon otomatis."""
    arr = np.array(titik)
    arr = np.vstack([arr, arr[0]])
    plt.plot(arr[:, 0], arr[:, 1], color=warna, label=label)


def translasi(titik, vektor):
    """Tambahkan vektor (dx, dy) ke semua titik."""
    return [(x + vektor[0], y + vektor[1]) for x, y in titik]


def input_point(prompt):
    """Baca satu titik dari input pengguna dalam format 'x,y'."""
    while True:
        try:
            s = input(prompt)
            x, y = map(float, s.split(','))
            return (x, y)
        except Exception:
            print("Format salah. Masukkan dalam format x,y (contoh: 1,2)")


def input_vector(prompt):
    return input_point(prompt)


def plot_persegi_panjang_awal_dan_translasi(persegi_awal, persegi_trans, margin=2):
    plt.figure()
    gambar_persegi_panjang(persegi_awal, warna='b', label='Persegi Panjang Awal')
    gambar_persegi_panjang(persegi_trans, warna='r', label='Persegi Panjang Setelah Translasi')

    semua = persegi_awal + persegi_trans
    xs = [p[0] for p in semua]
    ys = [p[1] for p in semua]

    plt.grid(True)
    plt.xlim(min(xs) - margin, max(xs) + margin)
    plt.ylim(min(ys) - margin, max(ys) + margin)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title('Translasi 2D Persegi Panjang')
    plt.show()


def main(args=None):
    parser = argparse.ArgumentParser(description='Translasi Objek Persegi Panjang dengan Input Dinamis')
    parser.add_argument('--demo', action='store_true', help='Jalankan demo tanpa input interaktif')
    ns = parser.parse_args(args=args)

    if ns.demo:
        # Contoh data demo
        persegi_awal = [(1, 1), (4, 1), (4, 3), (1, 3)]
        vektor = (2, 3)
        persegi_trans = translasi(persegi_awal, vektor)
        plot_persegi_panjang_awal_dan_translasi(persegi_awal, persegi_trans)
        return

    print('Masukkan koordinat persegi panjang (4 titik) dalam format x,y (urut searah/berlawanan jarum jam)')
    p1 = input_point('Titik 1 (x1,y1): ')
    p2 = input_point('Titik 2 (x2,y2): ')
    p3 = input_point('Titik 3 (x3,y3): ')
    p4 = input_point('Titik 4 (x4,y4): ')

    persegi_awal = [p1, p2, p3, p4]

    dx, dy = input_vector('Masukkan vektor translasi (dx,dy): ')

    persegi_trans = translasi(persegi_awal, (dx, dy))
    plot_persegi_panjang_awal_dan_translasi(persegi_awal, persegi_trans)


if __name__ == '__main__':
    main()
