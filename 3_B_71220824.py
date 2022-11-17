print ("=========== CATATAN BELANJA ==========")
print ("=========== Daftar 1 ==========")
listsaya1 = ['Sikat Gigi', 'odol', 'Shampo', 'Sabun', 'Ciduk']
print ("Daftar Belanja 1", listsaya1)
print ("")
print ("=========== Daftar 2 ==========")
listsaya2 = ['Teh', 'Gula', 'Garam', 'Micin', 'Kecap']
print ("Daftar belanja 2 :", listsaya2)
print ("")
print ("Jawab dengan angka [1/2]")
print ("1. Rubah Belanjaan")
print ("2. Keluar")
u = int(input ("Masukan Pilihan: "))
if u == 2:
    print
else:
    if u == 1:
        v = input("Masukan nama item ke daftar 1 : ")
        w = int(input("Masukan index yang akan dirubah : "))
        listsaya1[w]=v
        x = input("Masukan nama item ke daftar 2 : ")
        y = int(input("Masukan nama item ke daftar 2:"))
        listsaya2[y]=x
        print ("=========== Daftar 1 ==========")
        print ("Daftar Belanja 1: ",listsaya1)
        print ("")
        print ("=========== Daftar 2===========")
        print ("Daftar Belanja 2: ",listsaya2)
    else:
        print("Try Again")
