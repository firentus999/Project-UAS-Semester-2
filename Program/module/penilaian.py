def penilaian():
    from texttable import Texttable
    table=Texttable()
    jawab="y"
    no=0
    nama=[]
    nim=[]
    nilai_tugas=[]
    nilai_uts=[]
    nilai_uas=[]
    while(jawab=="y"):
        nama.append(input("masukan nama:"))
        nim.append(input("masukan nim:"))
        nilai_tugas.append(input("masukan nilai tugas:"))
        nilai_uts.append(input("masukan nilai uts:"))
        nilai_uas.append(input("masukan nilai uas:"))
        jawab=input("tambah data (y)?")
    no +=1
    for i in range (no):
        tugas = int(nilai_tugas[i])
        uts = int(nilai_uts[i])
        uas = int(nilai_uas[i])
        akhir = (tugas*30/100)+(uts*35/100)+(uas*35/100)
        table.set_cols_dtype(['a','i','i','i','i','i','i'])
        table.add_rows([['NO','NAMA','NIM','TUGAS','UTS','UAS','AKHIR'],
                        [i+1,nama[i],nim[i],nilai_tugas[i],nilai_uts[i],nilai_uas[i],akhir]])
    print(table.draw())

