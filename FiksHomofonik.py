substitusi = {
    'a':['BU','CE','IT'],
    'b':['KL','OP'],
    'c':['NH','CM'],
    'd':['GT'],
    'e':['DI','UF','CR'],
    'f':['KI','VF'],
    'g':['OI'],
    'h':['MZ','NI'],
    'i':['FT','GY','MN'],
    'j':['LO','PU'],
    'k':['GH','VC','CX'],
    'l':['DF'],
    'm':['HM','AM'],
    'n':['AN','NZ'],
    'o':['TR','HG','LI'],
    'p':['FD'],
    'q':['OI','SQ'],
    'r':['XG'],
    's':['ZX'],
    't':['LM','AS','CV'],
    'u':['UO','YT'],
    'v':['XI'],
    'w':['cx'],
    'x':['PV','KX'],
    'y':['XQ','DV'],
    'z':['VZ','YQ'],
}

def enkripsi(teks):
    teks_enkripsi = ''
    for huruf in teks:
        if huruf.lower() in substitusi:
            simbol = substitusi[huruf.lower()]
            teks_enkripsi += simbol[0]  #simbol [0] Menggunakan simbol pertama dari daftar substitusi #simbol [1] Menggunakan simbol ke2
    return teks_enkripsi

def deskripsi(teks_enkripsi):
    teks_deskripsi = ''
    for i in range(0, len(teks_enkripsi), 2):
        simbol = teks_enkripsi[i:i+2]
        for huruf, daftar_simbol in substitusi.items():
            if simbol in daftar_simbol:
                teks_deskripsi += huruf
                break
        else:
            teks_deskripsi += simbol
    return teks_deskripsi

if __name__ == '__main__':
    print ('-----------------------------------')
    print ('    Nama        : Munis Zulhusni   ')
    print ('    Nim         : A11.2021.13693   ')
    print ('    Kelas       : A11.4302         ')
    print ('-----------------------------------')    

    option = int (input ('1. Enkripsi\n2. Deskripsi\nPilih Option              : '))
    if option == 1:
        teks = input ('Masukan pesan (Plaintext) : ')
        print(enkripsi(teks))
    elif option == 2:
        teks_enkripsi = input ('Masukan pesan (Chipertext): ')
        print(deskripsi(teks_enkripsi))
    else:
        print ('TIDAK VALID! PILIH OPSI LAIN!')    