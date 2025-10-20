import math
riwayat = []  

def hitung():
    try:
        op = input("Masukkan operator (+, -, *, /, %, **, sqrt): ")

        if op == "sqrt":
            angka_1 = float(input("Masukkan angka: "))
            if angka_1 < 0:
                print("Error: tidak bisa menghitung akar dari bilangan negatif.")
                return
            r = math.sqrt(angka_1)
            hasil_str = f"√{angka_1} = {r}"
        else:
            angka_1 = float(input("Masukkan angka pertama: "))
            angka_2 = float(input("Masukkan angka kedua: "))

            if op == '+':
                r = angka_1 + angka_2
            elif op == '-':
                r = angka_1 - angka_2
            elif op == '*':
                r = angka_1 * angka_2
            elif op == '/':
                if angka_2 == 0:
                    print("Error: pembagian dengan nol")
                    return
                r = angka_1 / angka_2
            elif op == '%':
                r = angka_1 % angka_2
            elif op == '**':
                r = angka_1 ** angka_2
            else:
                print("Operator tidak dikenal")
                return

            hasil_str = f"{angka_1} {op} {angka_2} = {r}"

        print(hasil_str)
        riwayat.append(hasil_str)

    except ValueError:
        print("Input harus berupa angka!")

def tampilkan_riwayat():
    if not riwayat:
        print("Belum ada riwayat perhitungan.")
    else:
        print("\n=== Riwayat Perhitungan ===")
        for idx, item in enumerate(riwayat, start=1):
            print(f"{idx}. {item}")

if __name__ == "__main__":
    while True:
        pilihan = input("\nKetik 'keluar' untuk berhenti, 'riwayat' untuk melihat hasil sebelumnya, atau tekan Enter untuk mulai: ")

        if pilihan.lower() in ("keluar", "exit", "quit"):
            print("Program selesai. Terima kasih!")
            break
        elif pilihan.lower() == "riwayat":
            tampilkan_riwayat()
        else:
            hitung()