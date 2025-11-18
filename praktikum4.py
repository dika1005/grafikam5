
import matplotlib.pyplot as plt
import numpy as np
import argparse


def gambar_lingkaran(pusat, radius, warna='b', label=None, n=200):
    theta = np.linspace(0, 2 * np.pi, n)
    x = pusat[0] + radius * np.cos(theta)
    y = pusat[1] + radius * np.sin(theta)
    plt.plot(x, y, color=warna, label=label)
    plt.scatter([pusat[0]], [pusat[1]], color=warna, s=20)


def translasi(pusat, vektor):
    return (pusat[0] + vektor[0], pusat[1] + vektor[1])


def input_point(prompt):
    while True:
        try:
            s = input(prompt)
            x, y = map(float, s.split(','))
            return (x, y)
        except Exception:
            print("Format salah. Masukkan dalam format x,y (contoh: 1,2)")


def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except Exception:
            print("Format salah. Masukkan angka (contoh: 3.5)")


def plot_lingkaran_awal_dan_trans(pusat_awal, r, pusat_trans, warna_awal='b', warna_trans='r'):
    plt.figure()
    gambar_lingkaran(pusat_awal, r, warna=warna_awal, label='Lingkaran Awal')
    gambar_lingkaran(pusat_trans, r, warna=warna_trans, label='Lingkaran Setelah Translasi')

    xs = [pusat_awal[0], pusat_trans[0]]
    ys = [pusat_awal[1], pusat_trans[1]]
    margin = max(1.0, r * 0.5)
    plt.grid(True)
    plt.xlim(min(xs) - r - margin, max(xs) + r + margin)
    plt.ylim(min(ys) - r - margin, max(ys) + r + margin)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title('Translasi 2D Lingkaran')
    plt.show()


def main(args=None):
    parser = argparse.ArgumentParser(description='Translasi Objek Lingkaran dengan Input Dinamis')
    parser.add_argument('--demo', action='store_true', help='Jalankan demo tanpa input interaktif')
    ns = parser.parse_args(args=args)

    if ns.demo:
        pusat_awal = (2, 2)
        radius = 3
        vektor = (4, -1)
        pusat_trans = translasi(pusat_awal, vektor)
        plot_lingkaran_awal_dan_trans(pusat_awal, radius, pusat_trans)
        return

    print('Masukkan koordinat pusat lingkaran dalam format x,y')
    pusat = input_point('Pusat lingkaran (x,y): ')
    radius = input_float('Radius lingkaran: ')
    print('Masukkan vektor translasi dalam format dx,dy')
    dx, dy = input_point('Vektor translasi (dx,dy): ')
    pusat_trans = translasi(pusat, (dx, dy))
    plot_lingkaran_awal_dan_trans(pusat, radius, pusat_trans)


if __name__ == '__main__':
    main()
