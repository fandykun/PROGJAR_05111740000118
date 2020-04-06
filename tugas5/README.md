**Nama: Fandy Kuncoro Adianto**
**NRP: 05111740000118**
**Kelas: Progjar-C**

## *Dokumentasi Protokol Simple Chat via Terminal*

### DESKRIPSI
> Chat adalah salah satu metode untuk pertukaran informasi berupa pesan dengan pengguna lain dalam jaringan komputer yang terhubung dalam suatu jaringan. Sistem ini memudahkan pengguna pertukaran pesan jarak jauh dengan aman. Sistem ini memiliki beberapa fitur diantaranya autentifikasi user, pengiriman pesan, melihat inbox, melihat siapa saja pengguna yang sedang online, dan logout dari sistem. Sistem ini dibangun menggunakan bahasa python3 dengan memanfaatkan socket.

### FORMAT DATA
```shell
[COMMAND] [PARAMETER1] [PARAMETER2]
```

### DAFTAR FITUR
#### Autentifikasi User
- **Deskripsi dan Tujuan**
> Autentifikasi user adalah suatu proses untuk melakukan validasi user agar dapat memasuki sistem dan mengakses fitur-fitur lain yang ada di dalam sistem. Dalam sistem ini, user akan melakukan autentikasi dengan input username dan password. Apabila nilainya sesuai dengan yang tersimpan di sistem, maka user dapat Login ke Sistem Layanan Chatting ini. Sedangkan jika nilainya tidak sesuai user bisa mencoba log in kembali. 

> Tujuan dari adanya autentifikasi user untuk memverifikasi atau memvalidasi identitas user yang akan masuk ke dalam sistem serta Melindungi data dari user, yang tidak berhak untuk mengakses 

- **Input Parameter**
```shell
auth [username] [password]
```

- **Output**
    - Jika Berhasil
    ```python
    "username {} logged in, token {}" . format(username, self.tokenid)
    ```
    - Jika gagal
    ```python
    "Error, User Tidak Ada" # Jika User tidak ditemukan
    "Error, password salah" # Jika password salah
    ```
    Contoh:
    ```shell
    # input: auth henderson surabaya
    username henderson logged in, token 9abf3546-137d-4fd7-9d18-1f33e82acf8d
    ```
#### Send Message
- **Deskripsi dan Tujuan**
> Send Message adalah proses mengirimkan pesan dari satu user ke user yang lain. Inti dari aplikasi chatting ini adalah fitur ini. User dapat saling bertukar pesan dalam sistem layanan chatting tersebut ke satu user atau mengirim ke banyak user sekaligus. Namun, untuk melakukan pengiriman pesan ini, user harus log in terlebih dahulu.

> Tujuan dari adanya fitur ini agar user dapat berkomunikasi dengan user lain melalui sebuah jaringan. 

- **Input Parameter**
```shell
send [username_to] [messages]
```

- **Output**
    - Jika user belum melakukan autentifikasi 
    ```shell
        "Error, not authorized"
    ```
    - Jika user tidak ada
    ```shell
        "Error, User Tidak Ditemukan"
    ```
    - Jika berhasil
    ```python
        "message sent to {}" . format(usernameto)
    ```
    - Contoh:
    ```shell
    # Input
    "send messi hello gimana kabarnya mess"
    # Output
    "message send to messi"
    ```

#### Melihat Inbox User
- **Deskripsi dan Tujuan**
> Inbox sering diartikan sebagai kotak masuk. Inbox dapat dibuka oleh penerima pesan da akan berisi daftar pesan-pesan yang masuk ke dalam akunnya untuk dibaca dan dibalas. Urutan daftar dalam inbox ini menurut tanggal dan waktu pesan tersebut diterima. 

> Tujuan dari adanya inbox untuk melihat riwayat pesan yang diterima user sehingga pesan tersebut dapat dibaca atau dibalas. 

- **Input Parameter**
```shell
inbox
```

- **Output**
```python
{"username":[isi pesan]}
```
Contoh:
```shell
{"messi": [], "henderson": [{"msg_from": "Jordan Henderson", "msg_to": "Jordan Henderson", "msg": "  lohe lohe gara2 corona aku gakiso latian \r\n"}]}
```

#### Melihat User Online
- **Deskripsi dan Tujuan**
> Melihat daftar user yang online adalah salah satu fitur dalam Sistem Layanan chatting ini untuk memperlihatkan user lain yang sedang membuka sistem tersebut pada satu waktu yang sama.

> Tujuan dari adanya fitur ini agar ketika user ingin berkomunikasi dengan user lain, user mengetahui siapa saja user lain yang sedang membuka Sistem Layanan chatting tersebut, user dapat mengirim pesan kepada user lain dengan harapan agar mendapat respon yang cepat

- **Input Parameter**
```shell
show
```

- **Output**
    - Jika berhasil
    ```shell
    [{"username": "messi", "nama": "Lionel Messi", "negara": "Argentina"}, {"username": "henderson", "nama": "Jordan Henderson", "negara": "Inggris"}]
    ```
    - Jika user belum melakukan autentifikasi
    ```shell
    "Error, not authorized"
    ```

#### Logout
- **Deskripsi dan Tujuan**
> Logout adalah suatu proses keluar dari sistem jaringan, setelah sebelumnya melakukan log in pada sebuah akun. Ketika user akan melakukan logout, sistem akan menghapus session id pada data yang tersimpan.

> Tujuan dari adanya logout ini menjaga keamanan sebuah akun agar tidak digunakan orang lain.

- **Input Parameter**
```shell
logout
```

- **Output**
    - Jika berhasil
    ```python
    "{}" . format(sessionid)
    ```
    - Jika user belum melakukan autentifikasi
    ```shell
    "Error, not authorized"
    ```
    - Contoh
    ```shell
    "11ba4593-bcf5-44cd-a98c-90ce57a39c77"
    ```