import psycopg2
from io import open
print('Bienvenido - Programa para determinar el tipo de triangulo. \nSeleccione una opción')
while True:
    print('\n\t1 - Iniciar')
    print('\t0 - Salir')
    try:
        menu = int(input())
        if menu == 1:
            try:
                x=int(input('Primer lado: >> '))
                y=int(input('Segundo lado:>> '))
                z=int(input('Tercer lado: >> '))
                if ((x==y)and(x==z)):
                    print('Triangulo Equilatero')
                    c='Equilatero'
                elif ((x==y)or(x==z)or(y==z)):
                    print('Triangulo Isosceles')
                    c='Isosceles'
                else:
                    print('Triangulo Escaleno')
                    c='Escaleno'

            except:
                print('Error de ingreso. - Ingrese un valor numerico')
            xx=str(x)
            yy=str(y)
            zz=str(z)
            conn = psycopg2.connect(
            database="exam1", user='postgres', password='123', host='localhost', port= '5432'
            )
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO p3 (lado1,lado2,lado3,triangulo) VALUES (%s, %s, %s, %s)''',(x,y,z,c))
            conn.commit()
            conn.close()
            archivo_texto=open("201700325.txt","a")
            archivo_texto.write('\n\nTercer Programa:\nLado 1: ' +xx+'\nLado 2: '+yy+'\nLado 3: '+zz+ '\nTriangulo: '+c)
            archivo_texto.close()
        elif menu==0:
            break
        else:
            zzz=int(input('Opcion incorrecta \n Oprima cualqier letra'))
    except:
        print('Error de ingreso. - Ingrese un valor numerico')
