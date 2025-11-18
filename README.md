# Praktikum M5 — Translasi Objek 2D

Folder ini berisi skrip Python sederhana untuk memvisualisasikan translasi objek 2D (segitiga, persegi panjang, lingkaran).

Files:
- `praktikum1.py` — contoh menggambar dan translasi segitiga (non-interaktif example).
- `praktikum2.py` — translasi segitiga dengan input dinamis (interaktif via terminal).
- `praktikum3.py` — translasi persegi panjang dengan input dinamis dan opsi demo (`--demo`).
- `praktikum4.py` — translasi lingkaran dengan input dinamis dan opsi demo (`--demo`).
- `requirements.txt` — dependensi Python (matplotlib, numpy).

Cara instalasi (PowerShell):
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Cara menjalankan:
- Demo cepat (tanpa input):
```
python "praktikum3.py" --demo
python "praktikum4.py" --demo
```
- Interaktif (terminal akan meminta input):
```
python "praktikum2.py"
python "praktikum3.py"
python "praktikum4.py"
```
Masukkan koordinat dalam format `x,y` (contoh `1,2`) ketika diminta.

Contoh input untuk `praktikum4.py`:
- `Pusat lingkaran (x,y): 1,2`
- `Radius lingkaran: 3`
- `Vektor translasi (dx,dy): 2,-1`

Opsional yang bisa saya tambahkan jika Anda mau:
- Simpan hasil plot ke file PNG (opsi `--output out.png`).
- Validasi input lebih ketat (cek radius > 0, cek 4 titik membentuk persegi panjang).
- Commit perubahan ke git dan buat branch/commit message.
