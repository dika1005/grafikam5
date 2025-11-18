import matplotlib.pyplot as plt
import numpy as np

# --- 1. Definisi Vertices (Titik Sudut) ---
# Koordinat vertikal seluruh jajaran genjang yang terlihat di grafik:
# V1: (10, 10) - Titik Kiri Bawah (Persegi Panjang Awal)
# V2: (40, 8) - Titik Kanan Bawah (Persegi Panjang Awal - perkiraan)
# V3: (60, 28) - Titik Kanan Atas (Persegi Panjang Setelah Translasi)
# V4: (30, 30) - Titik Kiri Atas (Persegi Panjang Setelah Translasi)

# Outline (Garis Luar)
vertices_x = [10, 40, 60, 30, 10]
# Pastikan garis bawah lurus pada y=10 dan garis atas lurus pada y=30
vertices_y = [10, 10, 30, 30, 10]

# Garis Pembatas (garis tengah horizontal pada y=20 seperti pada gambar tugas)
mid_y = 20

# Hitung titik potong garis horizontal y=mid_y dengan sisi-sisi polygon
xs_intersect = []
verts = list(zip(vertices_x, vertices_y))
for i in range(len(verts) - 1):
	x1, y1 = verts[i]
	x2, y2 = verts[i+1]
	# Cek apakah segmen (x1,y1)-(x2,y2) memotong garis y=mid_y
	if (y1 - mid_y) * (y2 - mid_y) <= 0 and (y1 != y2):
		# linear interpolation untuk x
		t = (mid_y - y1) / (y2 - y1)
		xi = x1 + t * (x2 - x1)
		xs_intersect.append(xi)

# Ambil dua potongan terurut (jika ada lebih dari 2, pilih dua tengah)
xs_intersect = sorted(xs_intersect)
if len(xs_intersect) >= 2:
	# pilih dua titik yang membentuk segmen di dalam polygon
	dividing_line_x = [xs_intersect[0], xs_intersect[-1]]
	dividing_line_y = [mid_y, mid_y]
else:
	# fallback: jika tidak ada potong (tidak seharusnya), gunakan rentang lebar
	dividing_line_x = [10, 50]
	dividing_line_y = [mid_y, mid_y]


# --- 2. Pembuatan Plot ---
fig, ax = plt.subplots(figsize=(8, 6))

# Plot garis luar jajaran genjang
ax.plot(vertices_x, vertices_y, color='black', linewidth=2)

# Plot garis pemisah
ax.plot(dividing_line_x, dividing_line_y, color='black', linewidth=1.5)

# --- 3. Pengaturan Grid dan Sumbu ---
# Atur tanda centang sumbu x (0, 10, 20, ...)
ax.set_xticks(np.arange(0, 61, 10))
# Atur tanda centang sumbu y (0, 5, 10, ...)
ax.set_yticks(np.arange(0, 31, 5))
# Tampilkan grid
ax.grid(True, linestyle='-', alpha=0.6)

# Batasan Sumbu
ax.set_xlim(0, 60)
ax.set_ylim(0, 30)
ax.set_aspect('equal', adjustable='box')

# --- 4. Legend (Keterangan) ---
# Membuat keterangan yang meniru gaya kotak keterangan di gambar asli
# Plot segmen dummy untuk label keterangan
ax.plot([0, 0], [0, 0], color='black', linewidth=2, label='Persegi Panjang Awal')
ax.plot([0, 0], [0, 0], color='black', linewidth=2, label='Persegi Panjang Setelah Translasi')

# Tampilkan keterangan di sudut kiri bawah
ax.legend(loc='lower left', bbox_to_anchor=(0.05, 0.15), framealpha=0.8, fontsize=10)

# Judul Plot
ax.set_title('Translasi Persegi Panjang', fontsize=14)
# --- 5. Tampilkan / Simpan Gambar ---
# Jika ingin menyimpan hasil, aktifkan baris savefig di bawah.
# plt.savefig('translasi_persegi_panjang.png', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()