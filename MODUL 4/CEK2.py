class MotorManager:
    def __init__(self):
        self.motor_tersedia = self.reset_motor()

    def tampilkan_motor(self):
        list_motor_dengan_nomor = [f"{i+1}. {motor}" for i, motor in enumerate(self.motor_tersedia)]
        for item in list_motor_dengan_nomor:
            print(item)

    def tambah_motor(self, motor_baru):
        self.motor_tersedia.append(motor_baru)

    def hapus_motor(self, motor_hapus):
        if motor_hapus in self.motor_tersedia:
            self.motor_tersedia.remove(motor_hapus)
        else:
            print('Motor tidak terdapat pada list (perhatikan penulisan)')

    @staticmethod
    def reset_motor():
        return ['Honda Beat', 'Yamaha NMAX', 'Suzuki Satria']

    def main(self):
        while True:
            self.tampilkan_motor()

            tambah_atau_hapus = input("Pilih opsi Tambah, Hapus, RESET, STOP: ")

            if tambah_atau_hapus == "Tambah":
                tertambah_motor = input('Masukkan motor baru: ')
                self.tambah_motor(tertambah_motor)

            elif tambah_atau_hapus == "Hapus":
                terkurang_motor = input('Tulis motor yang ingin dihapus: ')
                self.hapus_motor(terkurang_motor)

            elif tambah_atau_hapus == "RESET":
                self.motor_tersedia = self.reset_motor()

            elif tambah_atau_hapus == "STOP":
                self.tampilkan_motor()  # Cetak daftar motor sebelum program berakhir
                break

            else:
                print("Tolong perhatikan penulisan")

if __name__ == "__main__":
    manager = MotorManager()
    manager.main()
