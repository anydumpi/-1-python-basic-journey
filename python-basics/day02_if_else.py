nama = "Diva"
umur = 20

if umur < 13: print ("Anak-anak")
elif umur <= 17: print ("Remaja")
else: print ("Dewasa")

#===================================
umur = int (input ("Masukkan umur anda: "))
membership = input ("Punya membership? (Ya/Tidak): ") .strip() .lower()
if umur >= 18 and membership == "Ya": print ("Akses penuh")
elif umur >= 18 and membership == "Tidak": print ("Akses terbatas")
else: print ("Tidak diizinkan")