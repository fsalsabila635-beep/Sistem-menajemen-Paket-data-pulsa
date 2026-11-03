# Sistem-menajemen-Paket-data-pulsa

# Anggota & Peran
1. Muhammad Azzam Juhdi(Program)
2. Keyrani Alexa Putri(Laporan bab 2 & bab 3)
3. Celsines Rante Tasak(Laporan bab 2 & bab 3)
4. Fina Salsabila Prasetyo(Laporan bab 1 & Flowchart)

# Deskripsi & Tujuan


Deskripsi

Sistem Manajemen Paket Internet & Pulsa merupakan program berbasis bahasa pemrograman Python yang dirancang untuk membantu proses pengelolaan dan transaksi produk digital, khususnya paket internet dan pulsa. Program ini dibuat untuk mempermudah pengelolaan data produk, proses pembelian, serta pemantauan transaksi agar lebih terstruktur dan efisien. Dalam sistem ini terdapat dua jenis pengguna, yaitu Admin dan User, yang memiliki hak akses berbeda sesuai dengan tugas masing-masing.

Admin bertugas mengelola seluruh data paket internet dan pulsa melalui fitur CRUD (Create, Read, Update, Delete), yang meliputi menambahkan paket baru, melihat daftar paket, mengubah informasi paket, serta menghapus paket yang sudah tidak tersedia. Selain itu, Admin juga dapat melihat seluruh riwayat transaksi dan laporan ringkas yang berisi total pendapatan, jumlah transaksi, serta produk terlaris.

Sementara itu, User dapat melakukan registrasi dan login untuk masuk ke dalam sistem. Setelah berhasil login, User dapat melihat daftar paket yang tersedia, melakukan pengisian saldo (top up), membeli paket internet atau pulsa sesuai kebutuhan, serta melihat riwayat transaksi pribadi. Setiap transaksi pembelian yang berhasil akan menghasilkan invoice sebagai bukti pembelian.

Untuk menjaga pengelolaan data, program ini menggunakan file JSON (data_pulsa.json) sebagai media penyimpanan data akun, produk, dan transaksi. Dengan demikian, data yang telah dimasukkan tidak hanya tersimpan selama program berjalan, tetapi juga dapat digunakan kembali ketika program dijalankan pada kesempatan berikutnya.

Program ini dijalankan melalui terminal atau console tanpa menggunakan tampilan grafis (GUI). Tampilan informasi seperti daftar paket, invoice, dan riwayat transaksi disusun menggunakan PrettyTable agar lebih rapi dan mudah dibaca.

Tujuan

1. Mempermudah pengelolaan data paket internet dan pulsa.
2. Menyediakan fitur transaksi pembelian secara terstruktur.
3. Menerapkan pembagian hak akses Admin dan User.
4. Memudahkan penyimpanan dan pengelolaan data menggunakan JSON.
5. Menerapkan materi dasar pemrograman Python dalam sebuah proyek.

# Flowchart

Menu Utama
<img width="5928" height="5128" alt="image" src="https://github.com/user-attachments/assets/17676dee-23ac-46a5-bdc3-ee1e869dc3ea" />

Menu Admin
<img width="6808" height="5728" alt="image" src="https://github.com/user-attachments/assets/6747561b-a6d0-44a1-89d8-33e5bf5e0d02" />

Menu User
<img width="5376" height="8008" alt="image" src="https://github.com/user-attachments/assets/803dc4d5-4617-4854-bf5c-4f1f68c17298" />


**Daftar Fitur Berdasarkan Role**

Pada program Sistem Manajemen Paket Internet dan Pulsa, terdapat dua jenis pengguna, yaitu Admin dan User. Setiap role memiliki fitur dan hak akses yang berbeda sesuai dengan fungsinya.

1. Admin

Admin memiliki akses untuk mengelola data paket internet dan pulsa serta memantau seluruh transaksi yang dilakukan oleh pengguna. Fitur yang tersedia untuk Admin meliputi:

1. **Lihat Paket**  
   Menampilkan seluruh paket internet dan pulsa yang tersedia, termasuk nama paket, jenis, harga, dan stok.

2. **Tambah Paket**  
   Menambahkan paket baru dengan mengisi jenis paket, nama, harga jual, dan stok awal.

3. **Ubah Paket**  
   Mengubah informasi paket seperti nama, jenis, dan harga. Admin juga dapat mengatur stok dengan menambah, mengurangi, atau mengganti jumlah stok.

4. **Hapus Paket**  
   Menghapus paket yang sudah tidak digunakan dari daftar paket setelah melakukan konfirmasi.

5. **Semua Transaksi dan Laporan Ringkas**  
   Menampilkan seluruh transaksi pengguna serta ringkasan berupa total pendapatan, jumlah transaksi, dan produk terlaris.

6. **Logout**  
   Mengakhiri sesi penggunaan akun Admin dan kembali ke menu utama.

2. User

User merupakan pengguna yang dapat melakukan pembelian paket internet dan pulsa melalui program. Fitur yang tersedia untuk User meliputi:

1. **Lihat Paket**  
   Melihat daftar paket internet dan pulsa beserta nama, jenis, dan harga yang tersedia.

2. **Top Up Saldo**  
   Menambahkan saldo akun dengan memasukkan nominal yang diinginkan. Saldo tersebut digunakan untuk melakukan pembelian.

3. **Beli Paket/Pulsa**  
   Melakukan pembelian paket internet atau pulsa dengan ketentuan satu produk untuk setiap transaksi. Pembelian akan diproses setelah saldo mencukupi dan pengguna melakukan konfirmasi.

4. **Invoice Pembelian**  
   Menampilkan bukti transaksi yang berisi ID transaksi, username, nama paket, jumlah pembelian, total pembayaran, bonus, dan waktu transaksi.

5. **Riwayat Transaksi**  
   Melihat daftar transaksi yang pernah dilakukan oleh akun pengguna tersebut.

6. **Bonus Pembelian**  
   Mendapatkan bonus berdasarkan jumlah pembelian yang telah dilakukan, baik berupa tambahan kuota internet maupun poin pelanggan.

7. **Logout**  
   Mengakhiri sesi penggunaan akun User dan kembali ke menu utama.

 3. Fitur Umum

Selain fitur berdasarkan role, program juga menyediakan beberapa fitur umum yang dapat digunakan sebelum pengguna masuk ke dalam sistem, yaitu:

1. **Login**, untuk masuk menggunakan username dan password yang telah terdaftar.
2. **Registrasi**, untuk membuat akun baru sebagai User.
3. **Keluar**, untuk mengakhiri program.

4. 
