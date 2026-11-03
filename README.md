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
