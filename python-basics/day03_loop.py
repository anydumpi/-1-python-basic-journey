
# Challenge 1: Print angka 1-10
for i in range(1, 11):
    print(i)

#Challenge 2: Print hanya angka genap dari 1-10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

#Challenge 3: Minta user input angka, lalu print angka itu sebanyak yang dia masukkan
angka= int (input ("Input jumlah repeat: "))
for i in range (angka): print ("Halo")

#Challenge 4: Hitung total dan rata-rata
angka = int (input ("Berapa angka?"))
total = 0
for i in range (angka):
    nilai = int(input ("Masukkan angka: "))
    total = total + nilai
rata_rata = total/angka
print ("Total:", total)
print ("Rata-rata:", rata_rata)

#Challenge 5: Password Attempt (Loop + Break)
password_benar = "python123"
for i in range (3):
    password = input ("Masukkan password: ")
    if password == password_benar: 
        print ("Login Berhasil")
        break
    else:
        print ("Password Salah")
else: 
    print ("Akses Diblokir")

#Challenge 6: Tebak Angka (Mini Game)
angka_rahasia = 7
tebakan = 0
while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka: "))
    if tebakan < angka_rahasia:
        print("Terlalu kecil")
    elif tebakan > angka_rahasia:
        print("Terlalu besar")
print("Benar!")

#Challenge 7: Angka Harus Positif
while True:
    angka = int(input("Input sini: "))
    if angka < 0:
        print("Angka tidak boleh negatif")
        continue
    if angka == 0:
        print("Program berhenti")
        break
    print("Valid")
