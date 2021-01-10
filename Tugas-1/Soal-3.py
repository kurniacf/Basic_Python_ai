# SOAL 3

a = float(input())  # Ujian teori
b = float(input())  # Ujian Praktek

if(a >= 70 and b >= 70):
    print("Selamat, anda lulus!")
elif(a >= 70 and b < 70):
    print("Anda harus mengulang ujian praktek")
elif(a < 70 and b >= 70):
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")
