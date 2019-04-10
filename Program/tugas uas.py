
from module.penilaian import penilaian
from module.kalkulator import kalkulator
from module.penggajian import penggajian
import getpass
def pembayaran_UTS():
    from texttable import Texttable
    table1=Texttable()
    jawab="y"
    no=0
    nama=[]
    nim=[]
    kelas=[]
    pembayaran_spp=[]
    pembayaran_permatakuliah=[]
    uang_kas=[]
    biaya_admin=[]
    biaya_seminar=[]
    while(jawab=="y"):
        nama.append(input("Masukan Nama :"))
        nim.append(input("Masukan Nim :"))
        kelas.append(input("Masukan Kelas :"))
        jawab=input("Apa anda mau bayar uang SPP y/t ?")
        if jawab=="y":
            pembayaran_spp.append(input("Masukan berapa bulan anda mau bayar uang SPP :"))
        elif jawab=="t":
            pembayaran_spp.append(0)
        else:
            pass
        jawab=input("Apa anda mau bayar uang permatakuliah (y/t) ?")
        if jawab=="y":
            pembayaran_permatakuliah.append(250000)
        elif jawab=="t":
            pembayaran_permatakuliah.append(0)
        else:
            pass
        jawab=input("Apa anda mau bayar uang KAS y/t ?")
        if jawab=="y":
            uang_kas.append(20000)
        elif jawab=="t":
            uang_kas.append(0)
        else:
            pass
        jawab=input("Apa anda mau bayar uang SEMINAR y/t ?")
        if jawab=="y":
            biaya_seminar.append(100000)
        elif jawab=="t":
            biaya_seminar.append(0)
        else:
            pass
        biaya_admin.append(5000)
        jawab=input("tambah data (y)?")
        no+=1
    for i in range (no):
        spp = int(pembayaran_spp[i])
        mapel = int(pembayaran_permatakuliah[i])
        kas = int(uang_kas[i])
        admin=int(biaya_admin[i])
        event=int(biaya_seminar[i])
        total =(spp*500000)+(mapel+0)+(event+0)+(kas+0)+(admin+0)
        table1.set_cols_dtype(['a','i','i','i','i','i','i','i','i','i'])
        table1.add_rows([['NO','NAMA','KELAS','NIM','SPP','MAPEL','EVENT','KAS','ADMIN','TOTAL'],[i+1,nama[i],kelas[i],nim[i],pembayaran_spp[i],pembayaran_permatakuliah[i],biaya_seminar[i],uang_kas[i],biaya_admin[i],total]])
    print(table1.draw())
def pembayaran_UAS():
    from texttable import Texttable
    table2=Texttable()
    jawab="y"
    no=0
    nama=[]
    nim=[]
    kelas=[]
    pembayaran_spp=[]
    pembayaran_permatakuliah=[]
    uang_kas=[]
    biaya_admin=[]
    biaya_seminar=[]
    while(jawab=="y"):
        nama.append(input("Masukan nama :"))
        nim.append(input("Masukan nim :"))
        kelas.append(input("Masukan Kelas :"))
        jawab=input("Apa anda mau bayar uang SPP y/t ?")
        if jawab=="y":
            pembayaran_spp.append(input("Masukan berapa bulan anda mau bayar uang SPP :"))
        elif jawab=="t":
            pembayaran_spp.append(0)
        else:
            pass
        jawab=input("Apa anda mau bayar uang permatakuliah (y/t) ?")
        if jawab=="y":
            pembayaran_permatakuliah.append(250000)
        elif jawab=="t":
            pembayaran_permatakuliah.append(0)
        else:
            pass
        jawab=input("Apa anda mau bayar uang kas y/t ?")
        if jawab=="y":
            uang_kas.append(20000)
        elif jawab=="t":
            uang_kas.append(0)
        else:
            pass
        jawab=input("Apa anda mau bayar uang SEMINAR y/t ?")
        if jawab=="y":
            biaya_seminar.append(100000)
            biaya_seminar.append(0)
        else:
            pass
        biaya_admin.append(5000)
        jawab=input("tambah data (y)?")
        no+=1
    for i in range (no):
        spp = int(pembayaran_spp[i])
        mapel = int(pembayaran_permatakuliah[i])
        kas = int(uang_kas[i])
        admin=int(biaya_admin[i])
        event=int(biaya_seminar[i])
        total =(spp*500)+(mapel+0)+(event+0)+(kas+0)+(admin+0)
        table2.set_cols_dtype(['a','i','i','i','i','i','i','i','i','i'])
        table2.add_rows([['NO','NAMA','KELAS','NIM','SPP','MAPEL','EVENT','KAS','ADMIN','TOTAL'],
                        [i+1,nama[i],kelas[i],nim[i],pembayaran_spp[i],pembayaran_permatakuliah[i],biaya_seminar[i],uang_kas[i],biaya_admin[i],total]])
    print(table2.draw())

def Menu():
    print('========"MENU PILHAN PROGRAM"========')
    print(" ")
    print("1. Pembayaran UTS Mahasiswa")
    print("2. Pembayaran UAS Mahasiswa")
    print("3. Pembayaran GAJI Karyawan")
    print("4. Penilaian UJIAN Mahasiswa")
    print("5. Kalkulator Sederhana")
    print("6. Exit")
    print(70*"=")
    pilihan=input("Silahkan input :")
    print(70*"=")
    if pilihan=="1":
        pembayaran_UTS()
        lagi()
    elif pilihan=="2":
        pembayaran_UAS()
        lagi()
    elif pilihan=="3":
        penggajian()
        lagi()
    elif pilihan=="4":
        penilaian()
        lagi()
    elif pilihan=="5":
        kalkulator()
        lagi()
    elif pilihan=="6":
        exit()
    else:
        print("Silahkan masukan pilihan lain !")
def lagi():
    jawab=input("TAMBAH LAGI DATA (y/t) ? ")
    if jawab=="y":
        Menu()
    elif jawab=="t":
        exit()
    else:
        print("TERIMA KASIH !")
def login1():
    print("+++++++++++ SILAHKAN LOGIN ++++++++++++")
    print(" ")
    nama=input("Silahkan Masukan Nama = ")
    if nama=="agus":
        login2()
    else:
        print("Nama yang anda masukan salah")
def login2():
    password=getpass.getpass("Masukan Password :")
    if password=="00000":
        Menu()
    else:
        ("Password Yang Anda Masukan Salah !")
login1()
