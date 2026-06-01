class VendingMachine:
    def __init__(self):
        # 1. Daftar produk yang tersedia beserta harga dan stoknya
        self.produk = {
            "1": {"nama": "Coca-Cola", "harga": 8000, "stok": 5},
            "2": {"nama": "Aqua Minum", "harga": 4000, "stok": 10},
            "3": {"nama": "Teh Kotak", "harga": 6000, "stok": 0},  # Simulasi stok habis
            "4": {"nama": "Kopi Susu", "harga": 10000, "stok": 3}
        }
        self.saldo_user = 0 # Tempat menampung uang yang dimasukkan user

    def tampilkan_produk(self):
        print("\n=== DAFTAR MINUMAN VENDING MACHINE ===")
        print(f"Saldo Anda Saat Ini: Rp{self.saldo_user}")
        print("--------------------------------------")
        for nomor, info in self.produk.items():
            status_stok = info['stok'] if info['stok'] > 0 else "HABIS"
            print(f"[{nomor}] {info['nama']} - Rp{info['harga']} (Stok: {status_stok})")
        print("[0] Batalkan / Ambil Kembalian Uang")
        print("======================================")

    def masukkan_uang(self, jumlah_uang):
        if jumlah_uang > 0:
            self.saldo_user += jumlah_uang
            print(f" Berhasil memasukkan uang: Rp{jumlah_uang}")
        else:
            print("❌ Jumlah uang tidak valid!")

    def beli_produk(self, nomor_pilihan):
        # Cek apakah nomor pilihan ada di menu
        if nomor_pilihan not in self.produk:
            print("❌ Pilihan tidak tersedia di menu!")
            return

        item = self.produk[nomor_pilihan]

        # Cek Kondisi 1: Apakah stok masih ada?
        if item["stok"] <= 0:
            print(f"❌ Maaf, stok {item['nama']} sudah habis! Silakan pilih yang lain.")
            return

        # Cek Kondisi 2: Apakah uang user cukup?
        if self.saldo_user < item["harga"]:
            kekurangan = item["harga"] - self.saldo_user
            print(f"❌ Uang tidak cukup! Kurang Rp{kekurangan}. Silakan masukkan uang lagi.")
            return

        # Proses Transaksi jika lolos semua pengecekan
        self.saldo_user -= item["harga"] # Potong saldo uang
        item["stok"] -= 1 # Kurangi stok barang
        print(f" Clink! [1] {item['nama']} jatuh ke wadah pengambilan. Nikmati minuman Anda!")

    def kembalikan_sisa_uang(self):
        if self.saldo_user > 0:
            print(f" Uang kembalian Anda diambil: Rp{self.saldo_user}. Terima kasih!")
            self.saldo_user = 0
        else:
            print(" Terima kasih telah berkunjung!")


# --- CARA MENJALANKAN SIMULASINYA ---
if __name__ == "__main__":
    vm = VendingMachine()
    
    # Loop Utama Program (Mesin akan terus menyala)
    while True:
        vm.tampilkan_produk()
        aksi = input("\nMau lakukan apa? (1: Masukkan Uang, 2: Pilih Minuman, 3: Keluar): ")

        if aksi == "1":
            uang = int(input("Masukkan nominal uang Anda (Contoh: 5000): "))
            vm.masukkan_uang(uang)
            
        elif aksi == "2":
            pilihan = input("Masukkan nomor kode minuman yang mau dibeli: ")
            if pilihan == "0":
                vm.kembalikan_sisa_uang()
                break
            vm.beli_produk(pilihan)
            
        elif aksi == "3":
            vm.kembalikan_sisa_uang()
            break
        else:
            print("❌ Pilihan menu aksi salah!")