import matplotlib.pyplot as plt
import numpy as np


def gambar_segitiga(titik, warna='b', label=None):
    segitiga = np.array(titik)
    segitiga = np.vstack([segitiga, segitiga[0]])
    plt.plot(segitiga[:, 0], segitiga[:, 1], color=warna, label=label)


def translasi(titik, vektor):
    titik_baru = [(x + vektor[0], y + vektor[1]) for x, y in titik]
    return titik_baru


if __name__ == '__main__':
    # Titik-titik awal segitiga
    segitiga_awal = [(1, 2), (3, 5), (6, 2)]
    vektor_translasi = (2, 3)

    # Translasi segitiga
    segitiga_setelah_translasi = translasi(segitiga_awal, vektor_translasi)

    # Plot segitiga sebelum dan sesudah translasi
    plt.figure()
    gambar_segitiga(segitiga_awal, warna='b', label='Segitiga Awal')
    gambar_segitiga(segitiga_setelah_translasi, warna='r', label='Segitiga Setelah Translasi')

    # Mengatur grid dan setting sumbu
    plt.grid(True)
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title('Translasi 2D Segitiga')

    # Tampilkan plot
    plt.show()
