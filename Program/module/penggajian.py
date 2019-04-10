def penggajian():
    from texttable import Texttable
    table=Texttable()
    jawab="y"
    no=0
    nama=[]
    jabatan=[]
    gaji=[]
    while(jawab=="y"):
        nama.append(input("masukan nama :"))
        jab=input("jabatan:")
        jabatan.append(jab)
        if (jab=='operator'):
            gaji.append(300000)
            jawab=input(" \ntambah lagi (y)?")
        elif (jab=='leader'):
            gaji.append(5000000)
            jawab=input(" \ntambah lagi (y)?")
        elif (jab=='manager'):
            gaji.append(10000000)
            jawab=input(" \ntambah lagi (y)?")
        else:
            break 
        no +=1
    for i in range (no):
        table.add_rows ([['NO','NAMA','JABATAN','GAJI'],[i+1,nama[i],jabatan[i],gaji[i]]])
    print(table.draw())

