import psycopg2
from io import open
print('Bienvenido - Programa de calculo de sueldo semanal. \nSeleccione una opción')
while True:
    print('\n\t1 - Iniciar')
    print('\t0 - Salir')
    try:
        menu = int(input())
        if menu == 1:
            try:
                h=float(input('\nIngrese las horas trabajadas en la semana: >>'))
                h1=0
                if(h<=40):
                    h1=h*50
                elif(h>40):
                    h1=((h-40)*75)+2000
                elif(h<=0):
                    h1=0
                else:
                    h1=0
                
            except:
                print('Error de ingreso. - Ingrese un valor numerico')
            hx=str(h)
            hx1=str(h1)
            print('\nEl sueldo semanal es: Q: ',h1,' respectivo a  ',h, ' horas trabajadas ')
            conn = psycopg2.connect(
            database="exam1", user='postgres', password='123', host='localhost', port= '5432'
            )
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO p2 (horas,sueldo) VALUES (%s, %s)''',(h,h1))
            conn.commit()
            conn.close()
            archivo_texto=open("201700325.txt","a")
            archivo_texto.write('\n\nSegundo Programa:\n El sueldo semanal es: Q: '+hx1+' respectivo a  '+hx+ ' horas trabajadas ')
            archivo_texto.close()
        elif menu==0:
            break
        else:
            z=int(input('Opcion incorrecta \n Oprima cualqier letra'))
    except:
        print('Error de ingreso. - Ingrese un valor numerico')
