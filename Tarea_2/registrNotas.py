from alumnos import alumno
print('.: Bienvenidos al registro de notas :.')
alumnos = []
comandos = ['R', 'C', 'P', 'S', 'X']

while True:
    cmd = input('Ingrese comando : ')
    if cmd in comandos:
        if cmd == 'R':
            print('\n')
            print('<< Se registrará nuevo alumno >>')
            nombre = input('Ingrese el nombre del nuevo alumno : ')
            while nombre.isalpha() == False:
                print('¡ALERTA! : El nombre solo debe contener letras')
                print('\n')
                nombre = input('Ingrese el nombre del nuevo alumno : ')
            apellido = input('Ingrese el apellido del nuevo alumno : ')
            while apellido.isalpha() == False:
                print('¡ALERTA! : El apellido solo debe contener letras')
                print('\n')
                apellido = input('Ingrese el apellido del nuevo alumno : ')
            edad = input('Ingrese la edad del nuevo alumno : ')
            while not edad.isdigit() or len(edad) > 2:
                print('¡ALERTA! : La edad debe ser un número menor a 100')
                print('\n')
                edad = input('Ingrese la edad del nuevo alumno : ')
            nacionalidad = input('Ingrese la Nacionalidad del nuevo alumno : ') 
            while nacionalidad.isalpha() == False:
                print('¡ALERTA! : La nacionalidad solo debe contener letras')
                print('\n')
                nacionalidad = input('Ingrese la Nacionalidad del nuevo alumno : ') 
            objAlumno = alumno(nombre, apellido, edad, '', nacionalidad)
            alumnos.append(objAlumno)
            print('\n')
        elif cmd == 'C':
            print('<< Se actualizarán las notas de los alumno(s) >>')
            for alumnoInfo in alumnos:
                if alumnoInfo.nota == '':
                    notaAlumno = input(f'Ingrese la nota del alumno {alumnoInfo.nombre} : ')
                    while not notaAlumno.isdigit() or int(notaAlumno) < 0 or int(notaAlumno) > 20:
                        print('¡ALERTA! : La nota del alumno debe de ser un número entre 0 y 20')
                        print('\n')
                        notaAlumno = input(f'Ingrese la nota del alumno {alumnoInfo.nombre} : ')
                    alumnoInfo.registrarNota(notaAlumno)
            print('\n')
        elif cmd == 'P':
            print('<< Se mostrara el promedio de las notas de los alumno(s) >>')
            sumaNotas = 0
            i = 0
            promedio = 0
            for alumnoInfo in alumnos:
                if alumnoInfo.nota != '':
                    sumaNotas += int(alumnoInfo.nota)
                    i += 1
                    promedio = sumaNotas / i
            print(f'El promedio de notas para {i} es : {promedio}')
            print('\n')
        elif cmd == 'S':
            print('<< Se mostrara la suma total de las notas de los alumno(s) >>')
            sumaNotas = 0
            i = 0
            for alumnoInfo in alumnos:
                if alumnoInfo.nota != '':
                    nota = int(alumnoInfo.nota)
                    sumaNotas += nota
                    i += 1
            print(f'La suma de notas para {i} es : {sumaNotas}')
            print('\n')
        else:
            print('Comando de finalización')
            break
    else:
        print('Comando incorrecto')
