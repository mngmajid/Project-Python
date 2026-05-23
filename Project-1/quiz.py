

print ("Selamat datang di permainan qiz! ")

playing = input("Apa kamu mau main? ").lower()

if playing != "ya":
    print("Selamat Tinggal!")
    quit()

print("\nOke! Mari kita mulai!")

# inisial variabel untuk menghitung benar salah
benar = 0
salah = 0

answer = input("1. Siapa nama presiden pertama Indonesia? ").lower()
if answer == "soekarno":
    print("Benar!")
    benar += 1
else:
    print("Salah! Jawabannya adalah Soekarno.")
    salah += 1

answer = input("2. Kapan Indonesia Merdeka? ").lower()
if answer == "1945":
    print("Benar!")
    benar += 1
else:
    print("Salah! Jawabannya adalah 1945.")
    salah += 1

answer = input("3. Siapa yang di sebut Bapak Pendidikan di Indonesia? ").lower()
if answer == "ki hadjar dewantara":
    print("Benar!")
    benar += 1
else:
    print("Salah! Jawabannya adalah Ki Hadjar Dewantara.")
    salah += 1

answer = input("4. Nama Bapak proklamator indonesia? ").lower()
if answer == "soekarno":
    print("Benar!")
    benar += 1
else:
    print("Salah! Jawabannya adalah Soekarno.")
    salah += 1

answer = input("5. siapakah penemu pesawat asal indonesia? ").lower()
if answer == "b.j Habibie":
    print("Benar!")
    benar += 1
else:
    print("Salah! Jawabannya adalah B.J. Habibie.")
    salah += 1

answer = input("Apa kepanjangan NKRI ").lower()
if answer == "Negara Kesatuan Republik Indonesia":
    print("Benar!")
    benar += 1
else:
    print("Salah! Jawabannya adalah Negara Kesatuan Republik Indonesia.")
    salah += 1

print ("\n--Quiz Selesai--")
print (f"Total jawaban Benar: {benar}")
print ("Total jawaban Salah: ", salah)

total_pertanyaan = benar + salah
skor = (benar/total_pertanyaan)*100

# f memberitahu pyton kalau ada variabel yang di cetak
print (f"Selamat! Anda mendapatkan Skor: {skor:.2f}")
