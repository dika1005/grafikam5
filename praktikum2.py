import matplotlib.pyplot as plt
import numpy as np


def gambar_segitiga(titik, warna='b', label=None):
    """Gambar segitiga dari daftar titik (x,y)."""
    segitiga = np.array(titik)
    segitiga = np.vstack([segitiga, segitiga[0]])
    plt.plot(segitiga[:, 0], segitiga[:, 1], color=warna, label=label)


def translasi(titik, vektor):
    """Translasi semua titik dengan vektor (dx, dy)."""
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
    """Baca vektor translasi dari input pengguna dalam format 'dx,dy'."""
    return input_point(prompt)


def main():
    print("Masukkan koordinat segitiga (dalam format x,y):")
    x1, y1 = input_point("Titik 1 (x1, y1): ")
    x2, y2 = input_point("Titik 2 (x2, y2): ")
    x3, y3 = input_point("Titik 3 (x3, y3): ")

    segitiga_awal = [(x1, y1), (x2, y2), (x3, y3)]

    dx, dy = input_vector("Masukkan vektor translasi (dalam format dx, dy): ")

    segitiga_tertranslasi = translasi(segitiga_awal, (dx, dy))

    # Plot segitiga sebelum dan setelah translasi
    plt.figure()
    gambar_segitiga(segitiga_awal, warna='b', label='Segitiga Awal')
    gambar_segitiga(segitiga_tertranslasi, warna='r', label='Segitiga Setelah Translasi')

    # Menentukan batas sumbu (memperhitungkan kedua set titik)
    semua_titik = segitiga_awal + segitiga_tertranslasi
    xs = [p[0] for p in semua_titik]
    ys = [p[1] for p in semua_titik]
    margin = 10
    plt.grid(True)
    plt.xlim(min(xs) - margin, max(xs) + margin)
    plt.ylim(min(ys) - margin, max(ys) + margin)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title('Translasi 2D Segitiga')
    plt.show()


if __name__ == '__main__':
    main()
