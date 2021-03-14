import psycopg2
from datetime import date
from io import open
print('Bienvenido - Programa de calculo de edad actual. \nSeleccione una opción')
while True:
    print('\n\t1 - Iniciar')
    print('\t0 - Salir')
    try:
        menu = int(input())
        if menu == 1:
            try:
                año=int(input('\n Ingrese año de nacimiento.'))
                mes=int(input('\n Ingrese mes de nacimiento.'))
                dia=int(input('\n Ingrese dia de nacimiento.'))
                fecha=date.today()
                if (fecha.day>=dia):
                    if(fecha.month>=mes):
                        añox=(fecha.year)-año
                    else:
                        añox=(fecha.year)-año-1
                else:
                    if(fecha.month>=mes):
                        añox=(fecha.year)-año
                    else:
                        añox=(fecha.year)-año-1
            except:
                print('Error de ingreso. - Ingrese un valor numerico')
            añoa=str(año)
            mesa=str(mes)
            diaa=str(dia)
            añoxa=str(añox)
            print('\nUsted nacio el dia: : ',dia,' del mes  ',mes, ' del año ',año,'. Usted tiene: ',añox,'años')
            conn = psycopg2.connect(
            database="exam1", user='postgres', password='123', host='localhost', port= '5432'
            )
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO p4 (oo,mes,dia,edad) VALUES (%s, %s, %s, %s)''',(año,mes,dia,añox))
            conn.commit()
            conn.close()
            archivo_texto=open("201700325.txt","a")
            archivo_texto.write('\n\nCuarto Programa:\nUsted nacio el dia:  '+diaa+' del mes  '+mesa+ ' del año '+añoa+'. Usted tiene: '+añoxa+'años')
            archivo_texto.close()
        elif menu==0:
            break
        else:
            z=int(input('Opcion incorrecta \n Oprima cualqier letra'))
    except:
        print('Error de ingreso. - Ingrese un valor numerico')
