

print ("Selamat datang di permainan qiz! ")

playing = input("Apa kamu mau main? ").lower()

if playing != "ya":
    quit()
print("Oke! Mari kita mulai!")

answer = input("1. Siapa nama presiden pertama Indonesia? ").lower()
if answer == "soekarno":
    print("Benar!")
else:
    print("Salah! Jawabannya adalah Soekarno.")

answer = input("2. Kapan Indonesia Merdeka? ").lower()
if answer == "1945":
    print("Benar!")
else:
    print("Salah! Jawabannya adalah 1945.")

answer = input("3. Siapa yang di sebut Bapak Pendidikan di Indonesia? ").lower()
if answer == "ki hadjar dewantara":
    print("Benar!")
else:
    print("Salah! Jawabannya adalah Ki Hadjar Dewantara.")

    answer = input("4. Nama Bapak proklamator indonesia? ").lower()
if answer == "soekarno":
    print("Benar!")
else:
    print("Salah! Jawabannya adalah Soekarno.")

    answer = input("5. siapakah penemu pesawat asal indonesia? ").lower()
if answer == "b.j Habibie":
    print("Benar!")
else:
    print("Salah! Jawabannya adalah B.J. Habibie.")

    answer = input("Apa kepanjangan NKRI ").lower()
if answer == "Negara Kesatuan Republik Indonesia":
    print("Benar!")
else:
    print("Salah! Jawabannya adalah Negara Kesatuan Republik Indonesia.")


