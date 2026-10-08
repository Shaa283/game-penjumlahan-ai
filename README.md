# Game Penjumlahan - Seret Jawaban dengan Tangan (CNN)

Tugas mata kuliah **Kecerdasan Buatan**.

## Cara menjalankan lewat Terminal VS Code

1. Ekstrak ZIP.
2. Buka folder **`game-penjumlahan`** di VS Code.
3. Buka **Terminal > New Terminal**.
4. Jalankan:

```powershell
python run.py
```

Jika perintah `python` tidak tersedia, gunakan:

```powershell
py run.py
```

5. Jika muncul:

```text
Server aktif di: http://localhost:8000
```

berarti server sudah berjalan.
6. **Terminal tidak membuka game secara otomatis.** Buka Chrome/Edge secara manual, lalu masuk ke:

```text
http://localhost:8000
```

7. Izinkan akses kamera.
8. Untuk menghentikan server, kembali ke terminal dan tekan **CTRL+C**.

> Game harus dijalankan melalui `localhost`, bukan dengan membuka `index.html` menggunakan double-click, agar kamera dan model MediaPipe dapat bekerja dengan benar.

## Alternatif tanpa `run.py`

Dari folder `game-penjumlahan`, jalankan:

```powershell
python -m http.server 8000
```

Kemudian buka `http://localhost:8000` secara manual.

## Cara bermain

- Kamera menampilkan tangan dan 21 titik sendi.
- Cubit ujung jempol dan telunjuk di atas kartu angka jawaban.
- Saat masih mencubit, seret kartu ke kotak `?` pada soal.
- Lepaskan cubitan.
- Jika kamera tidak tersedia, game tetap dapat dicoba dengan mouse.

## Struktur

- `index.html` - tampilan halaman
- `style.css` - gaya tampilan
- `game.js` - logika game dan deteksi tangan
- `run.py` - server lokal untuk menjalankan game dari Terminal VS Code
- `mediapipe/` - library dan model MediaPipe Hands


## Responsif
Game dirancang responsif untuk desktop, laptop, tablet, dan smartphone. Untuk kamera di HP, gunakan browser dengan HTTPS (misalnya GitHub Pages) dan izinkan akses kamera.
