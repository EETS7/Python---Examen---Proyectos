import psycopg2
from io import open
print('Bienvenido - Programa de detección de numeros. \nSeleccione una opción')
while True:
    print('\n\t1 - Iniciar')
    print('\t0 - Salir')
    try:
        menu = int(input())
        if menu==1:
            print('\nIngrese 5 numeros para detectar el mayor y menor.')
            try:
                x1=int(input('1 ero. >>'))
                x2=int(input('2  do. >>'))
                x3=int(input('3 ero. >>'))
                x4=int(input('4  to. >>'))
                x5=int(input('5  to. >>'))
                if(x1>x2 and x1>x3 and x1>x4 and x1>x5):
                    mayor=x1
                elif(x2>x1 and x2>x3 and x2>x4 and x2>x5):
                    mayor=x2
                elif(x3>x1 and x3>x2 and x3>x4 and x2>x5):
                    mayor=x3
                elif(x4>x1 and x4>x2 and x4>x3 and x4>x5):
                    mayor=x4
                elif(x5>x1 and x5>x2 and x5>x3 and x5>x4):
                    mayor=x5
                else:
                    mayor=0
                if(x1<x2 and x1<x3 and x1<x4 and x1<x5):
                    menor=x1
                elif(x2<x1 and x2<x3 and x2<x4 and x2<x5):
                    menor=x2
                elif(x3<x1 and x3<x2 and x3<x4 and x2<x5):
                    menor=x3
                elif(x4<x1 and x4<x2 and x4<x3 and x4<x5):
                    menor=x4
                elif(x5<x1 and x5<x2 and x5<x3 and x5<x4):
                    menor=x5
                else:
                    menor=0
            except:
                print('Error de ingreso')
            mayorb=str(mayor)
            menorb=str(menor)
            x11=str(x1)
            x22=str(x2)
            x33=str(x3)
            x44=str(x4)
            x55=str(x5)
            print('--Numero Mayor: ',mayor,'\n--Numero Menor: ',menor)
            conn = psycopg2.connect(
            database="exam1", user='postgres', password='123', host='localhost', port= '5432'
            )
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO p1 (d1,d2,d3,d4,d5,mayor,menor) VALUES (%s, %s, %s, %s, %s, %s, %s)''',(x1,x2,x3,x4,x5,mayor,menor))
            conn.commit()
            conn.close()
            archivo_texto=open("201700325.txt","a")
            archivo_texto.write('\n Primer Programa:\n1 :'+x11+'\n2: '+x22+'\n3: '+x33+'\n4: '+x44+'\n5: '+x55+'\nMayor: '+mayorb+'\nMenor: '+menorb)
            archivo_texto.close()
        elif menu==0:
            print('Salir, Adios')
            break
        else:
            z=int(input('Opcion incorrecta \n Oprima cualqier letra'))
    except:
        print('Error de ingreso. - Ingrese valores numericos')
        
        
