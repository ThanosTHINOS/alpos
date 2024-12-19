# CLI Application in Python

## Deskripsi
Aplikasi ini adalah simulator CLI (Command Line Interface) yang meniru fungsi dasar dari shell/terminal pada sistem Linux. Anda dapat menjalankan berbagai perintah untuk berinteraksi dengan sistem file.

## Daftar Perintah
- `ls`: Menampilkan daftar file dan folder di direktori saat ini.
- `pwd`: Menampilkan direktori kerja saat ini.
- `cd <dir>`: Mengubah direktori kerja.
- `mkdir <dir>`: Membuat direktori baru.
- `rmdir <dir>`: Menghapus direktori (jika kosong).
- `touch <file>`: Membuat file kosong baru.
- `rm <file>`: Menghapus file.
- `cp <src> <dest>`: Menyalin file dari satu lokasi ke lokasi lain.
- `mv <src> <dest>`: Memindahkan atau mengganti nama file/direktori.
- `help`: Menampilkan list perintah yang ada dan fungsinya.
- `clear`: Membersihkan layar terminal.
- `exit`: Keluar dari CLI.
- `search <pattern>`: Mencari file atau direktori berdasarkan nama.
- `tree`: Menampilkan struktur direktori dalam bentuk pohon.
- `find_large <size>`: Menampilkan file yang lebih besar dari ukuran tertentu.
- `log <command>`: Menyimpan riwayat penggunaan command ke file log.
- `joke`: Menampilkan lelucon acak untuk hiburan.

## Contoh Penggunaan
1. Menampilkan daftar file:

2. Mengubah direktori:

3. Membuat direktori baru:


4. Menampilkan lelucon:





## Cara Menjalankan
1. Pastikan Anda memiliki Python 3 terinstal di sistem Anda.
2. Jalankan aplikasi dengan perintah:



## Catatan
- Semua perintah yang tidak dikenal akan memberikan pesan kesalahan yang sesuai.
- Riwayat penggunaan perintah akan disimpan dalam file `command_log.txt`.
