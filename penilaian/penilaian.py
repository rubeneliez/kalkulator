def hitung_nilai_akhir(tugas, uts, uas):
    return 0.3 * tugas + 0.3 * uts + 0.4 * uas

def tentukan_grade(akhir):
    if akhir >= 85:
        return 'A', 'Sangat Baik'
    elif akhir >= 70:
        return 'B', 'Baik'
    elif akhir >= 55:
        return 'C', 'Cukup'
    elif akhir >= 40:
        return 'D', 'Kurang'
    else:
        return 'E', 'Sangat Kurang'

def input_nilai(nama_nilai):
    while True:
        try:
            nilai = float(input(f"Nilai {nama_nilai}: "))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus antara 0 - 100.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

def main():
    while True:
        name = input("Nama Mahasiswa: ")

        tugas = input_nilai("Tugas")
        uts = input_nilai("UTS")
        uas = input_nilai("UAS")

        akhir = hitung_nilai_akhir(tugas, uts, uas)
        grade, predikat = tentukan_grade(akhir)

        print(f"\n{name} => Nilai Akhir: {akhir:.2f}, Grade: {grade} ({predikat})\n")

        ulang = input("Apakah ingin input data mahasiswa lain? (y/n): ").lower()
        if ulang != 'y':
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()
