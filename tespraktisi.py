import json
import os
import time
import random
# Dependensi dibuat opsional agar program tetap bisa berjalan jika library
# belum terpasang. Jika tersedia, gunakan library aslinya.
try:
    import pwinput
    input_password = pwinput.pwinput
except ImportError:
    import getpass
    input_password = getpass.getpass

try:
    from prettytable import PrettyTable
except ImportError:
    class PrettyTable:
        def __init__(self):
            self.field_names = []
            self.rows = []

        def add_row(self, row):
            self.rows.append(row)

        def __str__(self):
            rows = [self.field_names] + self.rows
            widths = [
                max(len(str(row[i])) for row in rows)
                for i in range(len(self.field_names))
            ]
            garis = "+-" + "-+-".join("-" * w for w in widths) + "-+"
            hasil = [garis]
            for indeks, row in enumerate(rows):
                hasil.append("| " + " | ".join(
                    str(row[i]).ljust(widths[i])
                    for i in range(len(widths))
                ) + " |")
                if indeks == 0:
                    hasil.append(garis)
            hasil.append(garis)
            return "\\n".join(hasil)

FILE = "data_pulsa.json"

# Paket awal dikosongkan; admin menambahkan paket sendiri.
PAKET_AWAL = ()

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def muat_data():
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not all(k in data for k in
                    ("akun", "paket", "transaksi")):
                raise ValueError("Struktur file tidak valid.")
            # Migrasi data lama: tambahkan stok tanpa menghapus produk/transaksi.
            for paket in data["paket"]:
                paket.setdefault("stok", 0)
            for akun in data["akun"].values():
                akun.setdefault("saldo", 0)
                akun.setdefault("role", "user")
            simpan_data(data)
            return data
    except FileNotFoundError:
        data = {
            "akun": {
                "admin": {
                    "password": "admin123",
                    "role": "admin",
                    "saldo": 0
                }
            },
            "paket": [dict(p) for p in PAKET_AWAL],
            "transaksi": []
        }
        simpan_data(data)
        return data
    except (json.JSONDecodeError, ValueError):
        print("File data rusak atau formatnya salah.")
        print("Program dihentikan agar data tidak tertimpa.")
        raise SystemExit


def simpan_data(data):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def input_angka(pesan, minimum=0):
    while True:
        try:
            angka = int(input(pesan))
            if angka < minimum:
                print(f"Angka minimal {minimum}.")
                continue
            return angka
        except ValueError:
            print("Input harus berupa angka bulat.")


def registrasi(data):
    print("\n=== REGISTRASI USER ===")
    username = input("Username: ").strip()

    if len(username) < 4:
        print("Username minimal 4 karakter.")
        return False

    if username in data["akun"]:
        print("Username sudah digunakan.")
        return False

    password = input_password("Password: ")
    if len(password) < 6:
        print("Password minimal 6 karakter.")
        return False

    data["akun"][username] = {
        "password": password,
        "role": "user",
        "saldo": 0
    }
    simpan_data(data)
    print("Registrasi berhasil!")
    return True


def login(data):
    print("\n=== LOGIN ===")
    for percobaan in range(3):
        username = input("Username: ").strip()
        password = input_password("Password: ")
        akun = data["akun"].get(username)

        if akun and akun["password"] == password:
            print("Login berhasil!")
            return username

        sisa = 2 - percobaan
        if sisa > 0:
            print(f"Username atau password salah. Sisa percobaan: {sisa}")
        else:
            print("Login gagal 3 kali. Silakan coba lagi dari menu utama.")
    return None


def tampilkan_paket(data, tampil_stok=True):
    tabel = PrettyTable()
    if tampil_stok:
        tabel.field_names = ["No.", "Nama Paket", "Jenis", "Harga", "Stok"]
    else:
        tabel.field_names = ["No.", "Nama Paket", "Jenis", "Harga"]

    for nomor, paket in enumerate(data["paket"], start=1):
        baris = [
            nomor, paket["nama"], paket["jenis"],
            f"Rp{paket['harga']:,}"
        ]
        if tampil_stok:
            baris.append(paket.get("stok", 0))
        tabel.add_row(baris)

    if data["paket"]:
        print(tabel)
    else:
        print("Belum ada paket. Silakan tunggu admin menambahkan paket.")


def tambah_paket(data):
    print("\n=== TAMBAH PAKET ===")
    print("1. Internet")
    print("2. Pulsa")
    pilihan = input("Pilih jenis paket (1/2): ").strip()

    if pilihan == "1":
        jenis = "Internet"
    elif pilihan == "2":
        jenis = "Pulsa"
    else:
        print("Pilihan hanya 1 atau 2.")
        return False

    nama = input("Nama paket: ").strip()
    if not nama:
        print("Nama paket tidak boleh kosong.")
        return False

    harga = input_angka("Harga jual: Rp", 1)
    stok = input_angka("Stok awal: ", 0)
    data["paket"].append({
        "nama": nama,
        "jenis": jenis,
        "harga": harga,
        "stok": stok
    })
    simpan_data(data)
    print("Paket berhasil ditambahkan.")
    return True


def ubah_paket(data):
    tampilkan_paket(data)
    if not data["paket"]:
        return False
    nomor = input_angka("Pilih nomor paket yang diubah: ", 1)
    if nomor > len(data["paket"]):
        print("Nomor paket tidak ditemukan.")
        return False

    paket = data["paket"][nomor - 1]
    nama = input(f"Nama [{paket['nama']}]: ").strip()
    if nama:
        paket["nama"] = nama
    print("1. Internet")
    print("2. Pulsa")
    jenis = input("Jenis baru (Enter jika tidak diubah, 1/2): ").strip()
    if jenis == "1":
        paket["jenis"] = "Internet"
    elif jenis == "2":
        paket["jenis"] = "Pulsa"
    elif jenis:
        print("Pilihan jenis tidak valid.")
        return False
    harga_baru = input(f"Harga baru [Rp{paket['harga']:,}] (Enter untuk tetap): ").strip()
    if harga_baru:
        try:
            harga_baru = int(harga_baru)
            if harga_baru < 1:
                print("Harga harus lebih dari 0.")
                return False
            paket["harga"] = harga_baru
        except ValueError:
            print("Harga harus berupa angka bulat.")
            return False

    print(f"Stok saat ini: {paket.get('stok', 0)}")
    print("1. Atur stok menjadi jumlah tertentu")
    print("2. Tambahkan stok")
    print("3. Kurangi stok")
    print("4. Jangan ubah stok")
    aksi_stok = input("Pilih pengaturan stok: ").strip()
    stok_sekarang = paket.get("stok", 0)
    if aksi_stok == "1":
        paket["stok"] = input_angka("Stok baru: ", 0)
    elif aksi_stok == "2":
        paket["stok"] = stok_sekarang + input_angka("Jumlah stok tambahan: ", 1)
    elif aksi_stok == "3":
        pengurangan = input_angka("Jumlah stok yang dikurangi: ", 1)
        if pengurangan > stok_sekarang:
            print("Pengurangan melebihi stok yang tersedia.")
            return False
        paket["stok"] = stok_sekarang - pengurangan
    elif aksi_stok not in ("4", ""):
        print("Pilihan pengaturan stok tidak valid.")
        return False
    simpan_data(data)
    print("Paket berhasil diubah.")
    return True


def hapus_paket(data):
    tampilkan_paket(data)
    if not data["paket"]:
        return False
    nomor = input_angka("Pilih nomor paket yang dihapus: ", 1)
    if nomor > len(data["paket"]):
        print("Nomor paket tidak ditemukan.")
        return False

    paket = data["paket"][nomor - 1]
    konfirmasi = input(f"Hapus {paket['nama']}? (y/n): ").strip().lower()
    if konfirmasi == "y":
        data["paket"].pop(nomor - 1)
        simpan_data(data)
        print("Paket berhasil dihapus.")
        return True
    print("Penghapusan dibatalkan.")
    return False


def top_up(data, username):
    saldo = input_angka("Nominal top up: Rp", 1)
    data["akun"][username]["saldo"] += saldo
    simpan_data(data)
    print(f"Top up berhasil. Saldo: "
    f"Rp{data['akun'][username]['saldo']:,}")
    return saldo


def hitung_bonus(username, jenis, jumlah_pembelian):
    """Bonus hanya diberikan pada pencapaian pembelian tertentu."""
    if jumlah_pembelian == 3:
        return "Bonus kuota 1 GB" if jenis == "Internet" else "Bonus 10 poin pelanggan"
    if jumlah_pembelian == 5:
        return "Bonus kuota 2 GB" if jenis == "Internet" else "Bonus 25 poin pelanggan"
    if jumlah_pembelian == 10:
        return "Bonus kuota 5 GB" if jenis == "Internet" else "Bonus 50 poin pelanggan"
    if jumlah_pembelian > 10 and jumlah_pembelian % 3 == 0:
        return "Bonus kuota 1 GB" if jenis == "Internet" else "Bonus 10 poin pelanggan"
    return "Tidak ada bonus"


def beli_paket(data, username):
    akun = data["akun"][username]
    print("\\n=== PEMBERITAHUAN PEMBELIAN ===")
    print("Setiap transaksi hanya boleh membeli 1 paket internet atau 1 pulsa.")
    print("Pembelian 2 atau lebih sekaligus tidak diperbolehkan.")
    print("Jika ingin membeli lagi, selesaikan pembelian ini lalu lakukan transaksi baru.")
    tampilkan_paket(data, tampil_stok=False)
    if not data["paket"]:
        return False

    nomor = input_angka("Pilih nomor paket: ", 1)
    if nomor > len(data["paket"]):
        print("Nomor paket tidak ditemukan.")
        return False

    paket = data["paket"][nomor - 1]
    # Aturan sistem: satu transaksi hanya dapat membeli tepat satu paket/pulsa.
    # Tidak ada input jumlah; pembelian berikutnya harus melalui transaksi baru.
    jumlah = 1
    total = paket["harga"] * jumlah
    stok = paket.get("stok", 0)

    if stok < jumlah:
        print("Stok produk habis. Silakan pilih produk lain.")
        return False
    if akun["saldo"] < total:
        print("Saldo tidak mencukupi. Silakan top up.")
        return False

    print("\\n=== KONFIRMASI PEMBELIAN ===")
    print(f"Paket/pulsa : {paket['nama']}")
    print("Jumlah      : 1")
    print(f"Total       : Rp{total:,}")
    konfirmasi = input("Lanjutkan pembelian? (y/n): ").strip().lower()
    if konfirmasi != "y":
        print("Pembelian dibatalkan. Saldo dan stok tidak berubah.")
        return False

    pembelian_sebelumnya = sum(
        1 for item in data["transaksi"]
        if item.get("username") == username
    )
    jumlah_pembelian = pembelian_sebelumnya + 1
    bonus = hitung_bonus(username, paket["jenis"], jumlah_pembelian)

    akun["saldo"] -= total
    paket["stok"] = stok - jumlah

    transaksi = {
        "invoice": f"INV{int(time.time())}{random.randint(100, 999)}",
        "username": username,
        "nama_paket": paket["nama"],
        "jumlah": jumlah,
        "total": total,
        "bonus": bonus,
        "jumlah_pembelian_user": jumlah_pembelian,
        "stok_setelah_beli": paket["stok"],
        "waktu": time.strftime("%d-%m-%Y %H:%M:%S")
    }
    data["transaksi"].append(transaksi)
    simpan_data(data)
    cetak_invoice(transaksi)
    print(f"Total pembelian sukses akun ini: {jumlah_pembelian} kali.")
    print("Pemberitahuan: pembelian ini hanya 1 paket/pulsa.")
    print("Jika ingin membeli paket/pulsa lagi, silakan mulai transaksi baru.")
    if bonus == "Tidak ada bonus":
        print("Belum ada bonus kali ini. Terus bertransaksi untuk mencapai bonus!")
    else:
        print(f"SELAMAT! Kamu mendapatkan {bonus}.")
    print(f"Sisa stok {paket['nama']}: {paket['stok']}")
    return True


def cetak_invoice(transaksi):
    print("\n========== INVOICE ==========")
    print("ID Transaksi :", transaksi["invoice"])
    print("Username     :", transaksi["username"])
    print("Paket        :", transaksi["nama_paket"])
    print("Jumlah       :", transaksi["jumlah"])
    print(f"Total        : Rp{transaksi['total']:,}")
    print("Bonus        :", transaksi.get("bonus", "Tidak ada"))
    print("Waktu        :", transaksi["waktu"])
    print("=============================")


def riwayat_transaksi(data, username, admin=False):
    tabel = PrettyTable()
    tabel.field_names = [
        "Invoice", "Username", "Paket",
        "Jumlah", "Total", "Bonus", "Waktu"
    ]

    ditemukan = False

    for transaksi in data["transaksi"]:
        if admin or transaksi["username"] == username:
            tabel.add_row([
                transaksi["invoice"],
                transaksi["username"],
                transaksi["nama_paket"],
                transaksi["jumlah"],
                f"Rp{transaksi['total']:,}",
                transaksi.get("bonus", "-"),
                transaksi["waktu"]
            ])
            ditemukan = True

    if ditemukan:
        print(tabel)
    else:
        print("Belum ada transaksi.")


def laporan_transaksi(data):
    """Menampilkan semua transaksi dan ringkasan dalam satu menu."""
    transaksi = data["transaksi"]
    tabel = PrettyTable()
    tabel.field_names = [
        "Invoice", "Username", "Paket", "Jumlah", "Total", "Bonus", "Waktu"
    ]

    for item in transaksi:
        tabel.add_row([
            item["invoice"],
            item["username"],
            item["nama_paket"],
            item["jumlah"],
            f"Rp{item['total']:,}",
            item.get("bonus", "-"),
            item["waktu"]
        ])

    print("\n=== SEMUA TRANSAKSI ===")
    if transaksi:
        print(tabel)
    else:
        print("Belum ada transaksi.")

    total_pendapatan = sum(item["total"] for item in transaksi)
    jumlah_transaksi = len(transaksi)
    jumlah_produk = {}
    for item in transaksi:
        nama = item["nama_paket"]
        jumlah_produk[nama] = jumlah_produk.get(nama, 0) + item["jumlah"]

    print("\n=== LAPORAN RINGKAS ===")
    print(f"Total pendapatan : Rp{total_pendapatan:,}")
    print(f"Jumlah transaksi : {jumlah_transaksi}")
    if jumlah_produk:
        terlaris = max(jumlah_produk, key=jumlah_produk.get)
        print(f"Produk terlaris  : {terlaris} ({jumlah_produk[terlaris]} unit)")
    else:
        print("Produk terlaris  : Belum ada transaksi")


def menu_admin(data, username):
    while True:
        print(f"\n=== MENU ADMIN: {username} ===")
        print("1. Lihat paket")
        print("2. Tambah paket")
        print("3. Ubah paket")
        print("4. Hapus paket")
        print("5. Semua transaksi & laporan ringkas")
        print("6. Logout")

        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            tampilkan_paket(data)
        elif pilih == "2":
            tambah_paket(data)
        elif pilih == "3":
            ubah_paket(data)
        elif pilih == "4":
            hapus_paket(data)
        elif pilih == "5":
            laporan_transaksi(data)
        elif pilih == "6":
            break
        else:
            print("Menu tidak tersedia.")


def menu_user(data, username):
    while True:
        print(f"\n=== MENU USER: {username} ===")
        print(f"Saldo: Rp{data['akun'][username]['saldo']:,}")
        print("1. Lihat paket")
        print("2. Top up saldo")
        print("3. Beli paket/pulsa")
        print("4. Riwayat transaksi")
        print("5. Logout")

        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            tampilkan_paket(data, tampil_stok=False)
        elif pilih == "2":
            top_up(data, username)
        elif pilih == "3":
            beli_paket(data, username)
        elif pilih == "4":
            riwayat_transaksi(data, username)
        elif pilih == "5":
            break
        else:
            print("Menu tidak tersedia.")


def main():
    data = muat_data()

    while True:
        bersihkan_layar()
        print("=== SISTEM MANAJEMEN PAKET INTERNET & PULSA ===")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")

        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            username = login(data)

            if username:
                role = data["akun"][username]["role"]

                if role == "admin":
                    menu_admin(data, username)
                elif role == "user":
                    menu_user(data, username)
                else:
                    print("Role akun tidak valid.")

        elif pilih == "2":
            registrasi(data)

        elif pilih == "3":
            print("Terima kasih telah memakai program ini.")
            break

        else:
            print("Menu tidak tersedia.")

        input("\nTekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, FileNotFoundError, OSError) as error:
        print(f"Terjadi kesalahan: {error}")
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna.")
