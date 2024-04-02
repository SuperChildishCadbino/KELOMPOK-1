#Genre List
genre = ['Action', 'Horror']

#Database List Film Action
action = [
    {"Judul Film": "Blade Runner 2049", "Tahun": 2017, "Genre": "Action, Fiction", "Sutradara": "Luke Scott", "Durasi" : "163 Menit", "tiket" : "Rp 35.000"},
    {"Judul Film": "Everything Everywhere All at Once", "Tahun": 2023, "Genre": "Action, Fiction", "Sutradara": "Daniel Kwan", "Durasi" : "140 Menit", "tiket" : "Rp 35.000"},
    {"Judul Film": "Inception", "Tahun": 2010, "Genre": "Action,Fiction", "Sutradara": "Christopher Nolan", "Durasi" : "148 Menit","tiket" : "Rp 45.000"}]
horror = [
    {"Judul Film": "Get Out", "Tahun": 2017, "Genre": "Horror, Thriller", "Sutradara": "Jordan Pelee", "Durasi" : "104 Menit", "tiket" : "Rp 50.000"},
    {"Judul Film": "A Quiet Place", "Tahun": 2018, "Genre": "Horror", "Sutradara": "John Krasinski", "Durasi" : "90  Menit", "tiket" : "Rp 40.000"},
    {"Judul Film": "The LightHouse", "Tahun": 2019, "Genre": "Psychological, Horror", "Sutradara": "Robert Eggers", "Durasi" : "110 Menit", "tiket" : "Rp 45.000"}]

#Database Film action:
action1 = {"Judul Film": "Blade Runner 2049", "Tahun": 2017, "Genre": "Action, Fiction", "Sutradara": "Luke Scott", "Durasi" : "163 Menit", "tiket" : "Rp 35.000"}
action2 = {"Judul Film": "Everything Everywhere All at Once", "Tahun": 2023, "Genre": "Action, Fiction", "Sutradara": "Daniel Kwan", "Durasi" : "140 Menit", "tiket" : "Rp 35.000"}
action3 = {"Judul Film": "Inception", "Tahun": 2010, "Genre": "Action,Fiction", "Sutradara": "Christopher Nolan", "Durasi" : "148 Menit","tiket" : "Rp 45.000"}

#Database Film Horror
horror1 = {"Judul Film": "Get Out", "Tahun": 2017, "Genre": "Horror, Thriller", "Sutradara": "Jordan Pelee", "Durasi" : "104 Menit", "tiket" : "Rp 50.000"}
horror2 = {"Judul Film": "A Quiet Place", "Tahun": 2018, "Genre": "Horror", "Sutradara": "Daniel Kwan", "Durasi" : "90 Menit", "tiket" : "Rp 40.000"}
horror3 = {"Judul Film": "The LightHouse", "Tahun": 2019, "Genre": "Psychological, Horror", "Sutradara": "Robert Eggers", "Durasi" : "110 Menit", "tiket" : "Rp 45.000"}

#Theater Random Generate
import random
theater_number = random.randint(1,6)

#Invoicefilm_action = 
invoice_action1 = f"""
    Judul film : {action1['Judul Film']}
    Tahun      : {action1['Tahun']}
    Genre      : {action1['Genre']}
    Durasi     : {action1['Durasi']}
    Harga      : {action1['tiket']}
    Date       : Rabu, 3 April 2024, 14:35 - 17:55
    Theater    : {theater_number}"""
invoice_action2 = f"""
    Judul film : {action2['Judul Film']}
    Tahun      : {action2['Tahun']}
    Genre      : {action2['Genre']}
    Durasi     : {action2['Durasi']}
    Harga      : {action2['tiket']}
    Date       : Minggu, 7 April 2024, 20:00 - 23:00
    Theater    : {theater_number}"""
invoice_action3 = f"""
    Judul film : {action3['Judul Film']}
    Tahun      : {action3['Tahun']}
    Genre      : {action3['Genre']}
    Durasi     : {action3['Durasi']}
    Harga      : {action3['tiket']}
    Date       : Selasa, 9 April 2024, 12:30 - 14:50
    Theater    : {theater_number}"""

invoice_horror1 = f"""
    Judul film : {horror1['Judul Film']}
    Tahun      : {horror1['Tahun']}
    Genre      : {horror1['Genre']}
    Durasi     : {horror1['Durasi']}
    Harga      : {horror1['tiket']}
    Date       : Rabu, 3 April 2024, 15:35 - 17:00
    Theater    : {theater_number}"""
invoice_horror2 = f"""
    Judul film : {horror2['Judul Film']}
    Tahun      : {horror2['Tahun']}
    Genre      : {horror2['Genre']}
    Durasi     : {horror2['Durasi']}
    Harga      : {horror2['tiket']}
    Date       : Rabu, 3 April 2024, 13:00 - 14:30
    Theater    : {theater_number}"""
invoice_horror3 = f"""
    Judul film : {horror3['Judul Film']}
    Tahun      : {horror3['Tahun']}
    Genre      : {horror3['Genre']}
    Durasi     : {horror3['Durasi']}
    Harga      : {horror3['tiket']}
    Date       : Rabu, 3 April 2024, 18:35 - 21:00
    Theater    : {theater_number}"""

while True:
    print(23*'-')
    print("====== SELAMAT DATANG DI BIOSKOP XLL ======")
    print(23*'-')
    print("[1]. Pilih Film")
    print("[0]. Exit Program")
    print("-------------------------------------------\n")

    pilihan = int(input("Masukkan Pilihan Anda : "))

    if pilihan == 1:
        while pilihan != 0:
            if pilihan == 1:
                print("-------------------------------------------")
                print("============ DAFTAR GENRE FILM ============")
                print("-------------------------------------------")

                for genres in range(len(genre)):
                    print(f"{genres + 1}. {genre[genres]}")
                    print("------------------------------")

                pilihan_genre = int(input("Masukkan Pilihan Anda : "))
                if pilihan_genre == 1:
                    print("\nFilm yang sedang tayang\n")
                    print(133*'-')
                    print("No.   |             Judul Film             | Tahun  |         Genre            |     Sutradara     |   Durasi  |     Harga Tiket    |")
                    print("------|------------------------------------|--------|--------------------------|-------------------|-----------|--------------------|")
                    for item, film in enumerate(action, start=1):
                        print(f"{item:<5} | {film['Judul Film']:<34} | {film['Tahun']:<6} | {film['Genre']:<24} | {film['Sutradara']:<17} | {film['Durasi']:<5} | {film['tiket']:<18} |")
                    print(133*'-')
                    print()

                    pilihan_film = int(input("Pilih judul film [1-3] : "))

                    if pilihan_film == 1:
                        print()
                        print(invoice_action1)
                        print()

                        konfirmasi = input("Konfirmasi pilihan? [Ya/Tidak] : ")
                        if konfirmasi.lower() == 'ya': 
                            quantity = int(input("Masukkan quantity tiket : "))
                            total_harga = 0
                            for t in range(1, quantity + 1):
                                print(f"\n === Tiket {t} ===")
                                nama = input("Masukkan Nama: ")
                                umur = int(input("Umur: "))
                                if umur < 18:
                                    print()
                                    print('Umur anda :', umur)
                                    print(54*"!")
                                    print("Maaf, Anda belum mencukupi umur untuk menonton film ini")
                                    print(54*"!")
                                    print()
                                    break
                                else:
                                    tiket = {"Nama": nama, "Umur": umur}
                                    print(55*'-')
                                    print("                     INVOICE TIKET               ")
                                    print(55*'-')
                                    print('    Nama :', nama)
                                    print('    Umur :', umur)
                                    print(invoice_action1)
                                    print(55*'-')
                                    print()
                                    total_harga += 35000
                                    
                            if quantity == 2:
                                total_harga = 70000
                            else :
                                pass
                                
                            print("Total Harga Tiket:", total_harga, "rb")
                            konfirmasi_pembayaran = input("Konfirmasi pembayaran? [Ya/Tidak] : ")
                            if konfirmasi_pembayaran.lower() == 'ya':
                                print("Pembayaran berhasil.")
                            elif konfirmasi_pembayaran.lower() == 'tidak':
                                print("Anda kembali di menu genre")
                                continue
                            else:
                                print("Inputan tidak Valid!,silahkan pilih [YA/TIDAK]")

                    elif pilihan_film == 2:
                        print()
                        print(invoice_action2)
                        print()

                        konfirmasi = input("Konfirmasi pilihan? [Ya/Tidak] : ")
                        if konfirmasi.lower() == 'ya': 
                            quantity = int(input("Masukkan quantity tiket : "))
                            total_harga = 0
                            for t in range(1, quantity + 1):
                                print(f"\n === Tiket {t} ===")
                                nama = input("Masukkan Nama: ")
                                umur = int(input("Umur: "))
                                if umur < 18:
                                    print()
                                    print('Umur anda :', umur)
                                    print(54*"!")
                                    print("Maaf, Anda belum mencukupi umur untuk menonton film ini")
                                    print(54*"!")
                                    print()
                                    break
                                else:
                                    tiket = {"Nama": nama, "Umur": umur}
                                    print(55*'-')
                                    print("                     INVOICE TIKET               ")
                                    print(55*'-')
                                    print('    Nama :', nama)
                                    print('    Umur :', umur)
                                    print(invoice_action2)
                                    print(55*'-')
                                    print()
                                    #total harga akan diisikan sesuai harga tiket
                                    total_harga += 35000
                                    
                            if quantity == 2:
                                total_harga = 70000
                            else :
                                pass
                                
                            print("Total Harga Tiket:", total_harga, "rb")
                            konfirmasi_pembayaran = input("Konfirmasi pembayaran? [Ya/Tidak] : ")
                            if konfirmasi_pembayaran.lower() == 'ya':
                                print("Pembayaran berhasil.")
                            elif konfirmasi_pembayaran.lower() == 'tidak':
                                print("Anda kembali di menu genre")
                                continue
                            else:
                                print("Inputan tidak Valid!,silahkan pilih [YA/TIDAK]")

                    elif pilihan_film == 3:
                        print()
                        print(invoice_action3)
                        print()

                        konfirmasi = input("Konfirmasi pilihan? [Ya/Tidak] : ")
                        if konfirmasi.lower() == 'ya': 
                            quantity = int(input("Masukkan quantity tiket : "))
                            total_harga = 0
                            for t in range(1, quantity + 1):
                                print(f"\n === Tiket {t} ===")
                                nama = input("Masukkan Nama: ")
                                umur = int(input("Umur: "))
                                if umur < 18:
                                    print()
                                    print('Umur anda :', umur)
                                    print(54*"!")
                                    print("Maaf, Anda belum mencukupi umur untuk menonton film ini")
                                    print(54*"!")
                                    print()
                                    break
                                else:
                                    tiket = {"Nama": nama, "Umur": umur}
                                    print(55*'-')
                                    print("                     INVOICE TIKET               ")
                                    print(55*'-')
                                    print('    Nama :', nama)
                                    print('    Umur :', umur)
                                    print(invoice_action3)
                                    print(55*'-')
                                    print()
                                    total_harga += 45000
                                    
                            if quantity == 2:
                                total_harga = 90000
                            else :
                                pass
                                
                            print("Total Harga Tiket:", total_harga, "rb")
                            konfirmasi_pembayaran = input("Konfirmasi pembayaran? [Ya/Tidak] : ")
                            if konfirmasi_pembayaran.lower() == 'ya':
                                print("Pembayaran berhasil.")
                            elif konfirmasi_pembayaran.lower() == 'tidak':
                                print("Anda kembali di menu genre")
                                continue
                            else:
                                print("Inputan tidak Valid!,silahkan pilih [YA/TIDAK]")

                    else :
                        print("Inputan tidak valid! Silahkan masukan angka [1-3]")

                elif pilihan_genre == 2:
                    print("\nFilm yang sedang tayang\n")
                    print(133*'-')
                    print("No.   |             Judul Film             | Tahun  |         Genre            |     Sutradara     |   Durasi  |     Harga Tiket    |")
                    print("------|------------------------------------|--------|--------------------------|-------------------|-----------|--------------------|")
                    for item1, film in enumerate(horror, start=1):
                        print(f"{item1:<5} | {film['Judul Film']:<34} | {film['Tahun']:<6} | {film['Genre']:<24} | {film['Sutradara']:<17} | {film['Durasi']:<5} | {film['tiket']:<18} | ")
                    print(133*'-')
                    print()

                    pilihan_film = int(input("Pilih judul film [1-3] : "))

                    if pilihan_film == 1:
                        print()
                        print(invoice_horror1)
                        print()

                        konfirmasi = input("Konfirmasi pilihan? [Ya/Tidak] : ")
                        if konfirmasi.lower() == 'ya': 
                            quantity = int(input("Masukkan quantity tiket : "))
                            total_harga = 0
                            for t in range(1, quantity + 1):
                                print(f"\n === Tiket {t} ===")
                                nama = input("Masukkan Nama: ")
                                umur = int(input("Umur: "))
                                if umur < 18:
                                    print()
                                    print('Umur anda :', umur)
                                    print(54*"!")
                                    print("Maaf, Anda belum mencukupi umur untuk menonton film ini")
                                    print(54*"!")
                                    print()
                                    break
                                else:
                                    tiket = {"Nama": nama, "Umur": umur}
                                    print(55*'-')
                                    print("                     INVOICE TIKET               ")
                                    print(55*'-')
                                    print('    Nama :', nama)
                                    print('    Umur :', umur)
                                    print(invoice_action1)
                                    print(55*'-')
                                    print()
                                    total_harga += 50000
                                    
                            if quantity == 2:
                                total_harga = 100000
                            else :
                                pass
                                
                            print("Total Harga Tiket:", total_harga, "rb")
                            konfirmasi_pembayaran = input("Konfirmasi pembayaran? [Ya/Tidak] : ")
                            if konfirmasi_pembayaran.lower() == 'ya':
                                print("Pembayaran berhasil.")
                            elif konfirmasi_pembayaran.lower() == 'tidak':
                                print("Anda kembali di menu genre")
                                continue
                            else:
                                print("Inputan tidak Valid!,silahkan pilih [YA/TIDAK]")

                    elif pilihan_film == 2:
                        print()
                        print(invoice_horror2)
                        print()

                        konfirmasi = input("Konfirmasi pilihan? [Ya/Tidak] : ")
                        if konfirmasi.lower() == 'ya': 
                            quantity = int(input("Masukkan quantity tiket : "))
                            total_harga = 0
                            for t in range(1, quantity + 1):
                                print(f"\n === Tiket {t} ===")
                                nama = input("Masukkan Nama: ")
                                umur = int(input("Umur: "))
                                if umur < 18:
                                    print()
                                    print('Umur anda :', umur)
                                    print(54*"!")
                                    print("Maaf, Anda belum mencukupi umur untuk menonton film ini")
                                    print(54*"!")
                                    print()
                                    break
                                else:
                                    tiket = {"Nama": nama, "Umur": umur}
                                    print(55*'-')
                                    print("                     INVOICE TIKET               ")
                                    print(55*'-')
                                    print('    Nama :', nama)
                                    print('    Umur :', umur)
                                    print(invoice_horror2)
                                    print(55*'-')
                                    print()
                                    #total harga akan diisikan sesuai harga tiket
                                    total_harga += 40000
                                    
                            if quantity == 2:
                                total_harga = 80000
                            else :
                                pass
                                
                            print("Total Harga Tiket:", total_harga, "rb")
                            konfirmasi_pembayaran = input("Konfirmasi pembayaran? [Ya/Tidak] : ")
                            if konfirmasi_pembayaran.lower() == 'ya':
                                print("Pembayaran berhasil.")
                            elif konfirmasi_pembayaran.lower() == 'tidak':
                                print("Anda kembali di menu genre")
                                continue
                            else:
                                print("Inputan tidak Valid!,silahkan pilih [YA/TIDAK]")

                    elif pilihan_film == 3:
                        print()
                        print(invoice_horror3)
                        print()

                        konfirmasi = input("Konfirmasi pilihan? [Ya/Tidak] : ")
                        if konfirmasi.lower() == 'ya': 
                            quantity = int(input("Masukkan quantity tiket : "))
                            total_harga = 0
                            for t in range(1, quantity + 1):
                                print(f"\n === Tiket {t} ===")
                                nama = input("Masukkan Nama: ")
                                umur = int(input("Umur: "))
                                if umur < 18:
                                    print()
                                    print('Umur anda :', umur)
                                    print(54*"!")
                                    print("Maaf, Anda belum mencukupi umur untuk menonton film ini")
                                    print(54*"!")
                                    print()
                                    break
                                else:
                                    tiket = {"Nama": nama, "Umur": umur}
                                    print(55*'-')
                                    print("                     INVOICE TIKET               ")
                                    print(55*'-')
                                    print('    Nama :', nama)
                                    print('    Umur :', umur)
                                    print(invoice_horror3)
                                    print(55*'-')
                                    print()
                                    total_harga += 45000
                                    
                            if quantity == 2:
                                total_harga = 90000
                            else :
                                pass
                                
                            print("Total Harga Tiket:", total_harga, "rb")
                            konfirmasi_pembayaran = input("Konfirmasi pembayaran? [Ya/Tidak] : ")
                            if konfirmasi_pembayaran.lower() == 'ya':
                                print("Pembayaran berhasil.")
                            elif konfirmasi_pembayaran.lower() == 'tidak':
                                print("Anda kembali di menu genre")
                                continue
                            else:
                                print("Inputan tidak Valid!,silahkan pilih [YA/TIDAK]")

                    else :
                        print("Inputan tidak valid! Silahkan masukan angka [1-3]")
                        break  # Kembali ke menu sebelumnya
                
                else:
                    print()
                    print("Pilihan tidak ada dalam list!")

    elif pilihan == 0:
        print("Terima kasih telah menggunakan layanan kami. Sampai jumpa lagi!")
        break

    else:
        print('Inputan tidak ada!')
        print()