# fungsi pertambahan
def add(x,y):
    return x+y
# fungsi pengurangan
def subtract(x,y):
    return x-y
# fungsi perkalian
def multiply(x,y):
    return x*y
#fungsi pembagian
def divide(x,y):
    return x/y

#menu operasi
def kalkulator():
    print("Pilih Operasi")
    print("1.Pertambahan")
    print("2.Pengurangan")
    print("3.Perkalian")
    print("4.Pembagian")
#Meminta input dari user
    pilihan=input("Masukan pilihan :")
    num1=int(input("Masukan blangan pertama :"))
    num2=int(input("Masukan bilangan kedua :"))

    if pilihan=='1':
        print(num1,"+",num2,"=",
        add(num1,num2))
    elif pilihan=='2':
        print(num1,"-",num2,"=",
        subtract(num1,num2))
    elif pilihan=='3':
        print(num1,"*",num2,"=",
        multiply(num1,num2))
    elif pilihan=='4':
        print(num1,"/",num2,"=",
        devide(num1,num2))
    else:
        print("Input yang anda  masukan salah !")

