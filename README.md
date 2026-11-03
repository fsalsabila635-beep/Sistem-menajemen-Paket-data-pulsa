# Sistem-menajemen-Paket-data-pulsa

# Anggota & Peran
1. Muhammad Azzam Juhdi(Program) 2609116089
2. Keyrani Alexa Putri(Laporan bab 2 & bab 3) 2609116093
3. Celsines Rante Tasak(Laporan bab 2 & bab 3)2609116094
4. Fina Salsabila Prasetyo(Laporan bab 1 & Flowchart) 2609116097

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

Pada flowchart menu utama, program dimulai dengan menjalankan program kemudian menampilkan tiga pilihan menu, yaitu login, registrasi, dan keluar. Jika pengguna memilih login, pengguna diminta memasukkan username dan password. Sistem akan mengecek apakah data yang dimasukkan sudah sesuai. Jika sesuai, sistem akan mengecek role pengguna untuk menentukan apakah pengguna masuk ke menu admin atau menu user. Jika username atau password salah, pengguna diberikan kesempatan untuk mencoba kembali dengan batas maksimal tiga kali percobaan.

Jika pengguna memilih registrasi, pengguna diminta memasukkan username dan password baru. Sistem akan melakukan pengecekan seperti panjang username minimal 4 karakter, username belum digunakan, dan password minimal 6 karakter. Jika semua data sudah sesuai, akun baru akan disimpan dan program menampilkan bahwa registrasi berhasil. Sedangkan jika pengguna memilih keluar, program akan menampilkan ucapan terima kasih dan program selesai.



Menu Admin
<img width="6808" height="5728" alt="image" src="https://github.com/user-attachments/assets/6747561b-a6d0-44a1-89d8-33e5bf5e0d02" />

Pada flowchart menu admin, setelah berhasil login sebagai admin, sistem akan menampilkan beberapa pilihan menu. Admin dapat melihat paket, menambah paket, mengubah paket, menghapus paket, melihat transaksi dan laporan ringkasan, serta logout.

Pada menu lihat paket, sistem akan mengambil data paket dari file JSON kemudian menampilkan daftar paket. Pada menu tambah paket, admin memasukkan ID, jenis, harga, dan stok paket kemudian data akan disimpan. Untuk mengubah atau menghapus paket, sistem akan mencari ID paket terlebih dahulu. Jika ID ditemukan, admin dapat melanjutkan proses perubahan atau penghapusan data. Admin juga dapat melihat riwayat transaksi dan laporan ringkasan yang berisi informasi transaksi, pendapatan, serta data paket dan stok. Setelah selesai menggunakan menu admin, admin dapat memilih logout untuk kembali ke menu utama.




Menu User
<img width="5376" height="8008" alt="image" src="https://github.com/user-attachments/assets/803dc4d5-4617-4854-bf5c-4f1f68c17298" />

Flowchart Menu User menggambarkan alur penggunaan fitur pada Sistem Manajemen Paket Internet & Pulsa. Pengguna dapat memilih lima menu, yaitu Lihat Paket, Top Up Saldo, Beli Paket/Pulsa, Riwayat Transaksi, dan Logout.Pada menu Lihat Paket, sistem membaca data JSON dan menampilkan daftar paket yang tersedia. Pada menu Top Up Saldo, pengguna memasukkan nominal saldo yang ingin ditambahkan, kemudian sistem menyimpan perubahan dan menampilkan saldo terbaru.

Pada menu Beli Paket/Pulsa, pengguna memilih paket dan memasukkan jumlah pembelian. Sistem memvalidasi ID paket, jumlah pembelian, saldo, serta ketersediaan stok. Jika semua persyaratan terpenuhi, transaksi disimpan ke JSON, saldo dan stok diperbarui, kemudian sistem menghitung bonus kuota berdasarkan jumlah pembelian yang berhasil. Bonus yang diberikan adalah 1 GB pada pembelian ke-3, 2 GB pada pembelian ke-5, 5 GB pada pembelian ke-10, serta 1 GB untuk setiap pembelian mulai ke-15.

Pada menu Riwayat Transaksi, sistem menampilkan riwayat pembelian pengguna jika tersedia. Sementara itu, menu Logout digunakan untuk mengakhiri sesi dan kembali ke Menu Utama. Jika pengguna memasukkan pilihan yang tidak tersedia, sistem menampilkan pesan kesalahan dan kembali ke Menu User.



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

# Terminal (output) Login admin

<img width="816" height="194" alt="image" src="https://github.com/user-attachments/assets/c315dbe0-26f1-41cf-b5a7-6287da26ff26" />

Admin bawaan sistem dapat memilih opsi 1 (Login) pada menu utama dan menginputkan username admin serta password admin123. Sistem menggunakan fungsi login() yang dilengkapi batas percobaan maksimal 3 kali. Jika login berhasil, sistem akan mengarahkan pengguna ke Menu Admin.

# Terminal (output) menu admin dan pemilihan menunya dan juga login berhasil

<img width="1599" height="899" alt="image" src="https://github.com/user-attachments/assets/75b572aa-8c2f-4040-9fc3-fe98656f8d91" />

Bagi pengguna yang login sebagai Admin, sistem menampilkan menu khusus untuk manajemen data produk (CRUD) serta pemantauan seluruh transaksi. Menu Admin terdiri dari: 
1.	Lihat paket 
2.	Tambah paket 
3.	Ubah paket 
4.	Hapus paket 
5.	Semua transaksi & laporan ringkas 
6.	Logout


# Terminal (output) menu admin bagian paket 

<img width="373" height="192" alt="image" src="https://github.com/user-attachments/assets/f5a89b25-436a-46ce-a23b-2a5b5ec1fbae" />

Menampilkan daftar seluruh paket pulsa dan internet yang dikelola Admin secara rapi dalam bentuk tabel menggunakan modul PrettyTable melalui fungsi tampilkan_paket(). 

# Terminal (output) menu admin bagian tambah paket

<img width="552" height="157" alt="image" src="https://github.com/user-attachments/assets/64f0fa7b-5845-4228-9a11-4403fa131244" />

Output Lihat Paket
Admin dapat menambahkan produk paket internet atau pulsa baru ke dalam file JSON melalui fungsi

# Terminal (output) menu admin bagian ubah paket

<img width="429" height="142" alt="image" src="https://github.com/user-attachments/assets/7154bf1c-d3fb-4dcd-a6bb-2e8c804261fc" />

Admin dapat mengubah informasi nama, jenis, harga, maupun stok paket berdasarkan ID paket melalui fungsi ubah_paket().

# Terminal (output) menu admin bagian hapus paket

<img width="546" height="121" alt="image" src="https://github.com/user-attachments/assets/dae2ff01-9977-4b36-ba64-d3dbf53a7fa8" />

Admin dapat menghapus data paket dari file JSON melalui fungsi hapus_paket() dengan memilih ID paket dan mengonfirmasi tindakan (y/n).

# Terminal (output) bagian Semua Transaksi & Laporan Ringkas
<img width="819" height="397" alt="image" src="https://github.com/user-attachments/assets/7e974ac1-ce7f-42de-92f4-98e4c633b569" />

Menampilkan tabel seluruh transaksi yang dilakukan oleh seluruh User sekaligus menyajikan laporan ringkas berupa total pendapatan, jumlah transaksi, dan produk terlaris melalui fungsi laporan_transaksi(). 

# Terminal (output)  bagian Proses Registrasi User Baru 
<img width="762" height="156" alt="image" src="https://github.com/user-attachments/assets/cfb2a9d5-9b11-4dd8-b0c7-2d39a552b5a0" />

Jika calon pembeli/pengguna memilih opsi 2 (Registrasi) pada menu utama, sistem akan mengarahkan ke fungsi registrasi(). Pengguna diminta menginputkan username (minimal 4 karakter) dan password tersembunyi (minimal 6 karakter). Akun baru akan disimpan ke data_pulsa.json secara otomatis dengan role user dan saldo awal Rp0.

# Terminal (output) bagian login User
<img width="534" height="252" alt="image" src="https://github.com/user-attachments/assets/10dea87b-af8a-4fb0-b599-71a16ce7e281" />

jika user sudah registrasi maka akan di loginkan agar ketika login atau password
sudah benar jika benar akan masuk ke tampilan menu jika salah akan bisa login kembali tapi ada batasnya hanya 3 kali saja 

# Terminal (output) bagian menu User
<img width="400" height="175" alt="image" src="https://github.com/user-attachments/assets/77491d49-719e-492c-9eef-e73165c0ba2f" />

Bagi pengguna yang login sebagai User, sistem menampilkan menu transaksi digital sebagai berikut:
1.	Lihat paket 
2.	Top up saldo 
3.	Beli paket/pulsa 
4.	Riwayat transaksi 
5.	Logout

# Terminal (output) bagian user Top up saldo 
<img width="391" height="60" alt="image" src="https://github.com/user-attachments/assets/cdfa54c2-ad5b-4a92-aa26-b15112a576f4" />

User memasukkan nominal uang yang ingin ditambahkan ke akunnya. Saldo akun akan 

# Terminal (output) bagian user Beli Paket / Pulsa
<img width="574" height="188" alt="image" src="https://github.com/user-attachments/assets/d9a0f3c9-d22d-4cdc-92fd-d49286fdcacd" />

User memilih ID paket dan memasukkan jumlah yang ingin dibeli. Sistem memverifikasi ketersediaan stok dan kecukupan saldo. Jika memenuhi kriteria, saldo dikurangi, stok diperbarui, transaksi dicatat, dan sistem menerbitkan Invoice Pembelian.

# Terminal (output) bagian Riwayat Transaksi User
<img width="841" height="181" alt="image" src="https://github.com/user-attachments/assets/56e25665-0348-4d22-a8fb-3be8f02f6c6d" />

Menampilkan riwayat belanja personal yang hanya berisi transaksi milik pengguna yang sedang login tersebut.

# Terminal (output) bagian User Proses Keluar Program
<img width="573" height="192" alt="image" src="https://github.com/user-attachments/assets/546dc8b2-ad68-447a-a03c-9e623a443d0d" />

Jika pengguna memilih opsi 3 pada Menu Utama atau menu Logout dari perannya masing-masing, sistem menghentikan perulangan utama dan menampilkan pesan penutup sebelum program berhenti sepenuhnya.


