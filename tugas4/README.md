# Tugas 4

## How to Use?
- Jalankan `server.py` terlebih dahulu. atur konfigurasi IP Address dan PORT
- Terdapat 3 fitur yang sudah terbagi dalam masing-masing file.
- Fitur untuk **melihat isi file**:
    - jalankan `client_list.py` terlebih dahulu. Pastikan konfigurasi IP address dan PORT sesuai dengan yang telah disepakati dengan server
    - inputkan `list` pada terminal dan tunggu response dari server.
    - Hasilnya berupa daftar file pada direktori uploads (milik server)
- Fitur untuk **Meletakkan file**:
    - jalankan `client_upload.py` terlebih dahulu. Pastikan konfigurasi IP address dan PORT sesuai dengan yang telah disepakati dengan server
    - inputkan `upload [nama_file.ext]` pada terminal, pastikan file yang diupload berada pada direktori assets (milik client)
    - Hasil yang telah diupload dapat dilihat di direktori uploads
- Fitur untuk **Mengambil file**:
    - jalankan `client_download.py` terlebih dahulu. Pastikan konfigurasi IP address dan PORT sesuai dengan yang telah disepakati dengan server
    - inputkan `download [nama_file.ext]` pada terminal, pastikan file yang ingin didownload berada pada direktori uploads (milik server)
    - Hasil download dapat dilihat di direktori downloads

### Bukti berupa screenshot dapat dilihat di folder doc

## Dokumentasi

### a. Ketentuan Membaca Format
String terbagi menjadi 3 bagian berformat json
`[header]` `[content]` `[status]` sebagai key-nya.
`header` untuk command -> upload, list, download
`content` merupakan filename
`status` sebagai penanda pengiriman. value berupa OK

### b. Daftar Fitur, Request, Respon
- Masing-masing fitur terbagi menjadi 3 buah file client yang berbeda
- UPLOAD : untuk membuat file dari client agar dikirim ke server dan menyimpannya ke direktori uploads, file client terdapat di assets
    - request: `upload`
    - parameter: `nama file.ext`
    - response: jika berhasil -> `upl`, jika gagal maka error
- LIST : melakukan query pada database server, isi query berupa file yang terdapat pada direktori uploads
    - request: `list`
    - parameter: `null`
    - response: daftar file
- DOWNLOAD : untuk mengambil file dari server agar disimpan di client dan menyimpannya ke direktori downloads
    - request: `download`
    - parameter: `nama file.ext`
    - response: berupa bytes file yang dikirim dengan transmit TCP Socket.
