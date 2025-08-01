# Andriely Alejandro Casallas Calderon 2025

from datetime import datetime

class Docente:
    def __init__(self, id, nombre, email, telefono, fechaIngreso, cantCursos, salario, materia, horasSemanales, titulacion):
        # Inicializa los atributos del docente
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.fechaIngreso = fechaIngreso  # Fecha de ingreso en formato "YYYY-MM-DD"
        self.cantCursos = cantCursos      # Cantidad de cursos que dicta
        self.salario = salario            # Salario del docente
        self.asignaturas = materia        # Materias que dicta
        self.horasSemanales = horasSemanales  # Horas semanales trabajadas
        self.titulacion = titulacion      # Título académico

    def obtenerInfo(self):
        costoPorHora = self.salario / (self.horasSemanales * 4)
        # Obtiene la fecha y hora actual
        fechaActual = datetime.now()
        # Convierte la fecha de ingreso de string a objeto datetime
        fechaDeIngreso = datetime.strptime(self.fechaIngreso, "%Y-%m-%d")
        # Calcula el tiempo que lleva en la empresa
        tiempoEnLaUniversidad = fechaActual - fechaDeIngreso
        # Imprime la información del docente
        textoApoyo = ""
        if tiempoEnLaUniversidad.days < 0:
            textoApoyo = "Lleva: Porfavor ingrese una fecha valida."
        elif tiempoEnLaUniversidad.days == 0:
            textoApoyo = "Lleva: El docente, entro el dia de hoy"
        else:
            textoApoyo = f"Lleva: ({tiempoEnLaUniversidad.days // 365} años o {tiempoEnLaUniversidad.days // 30} meses o {tiempoEnLaUniversidad.days} días con nosotr@s)"
        print(f"""
            ================================================

            Docente:
            {textoApoyo}
            id: {self.id}
            nombre: {self.nombre}
            email: {self.email}
            teléfono: {self.telefono}
            fechaIngreso: {self.fechaIngreso}
            cantCursos: {self.cantCursos}
            salario: {self.salario}
            asignaturas: {self.asignaturas}
            horasSemanales: {self.horasSemanales}
            titulación: {self.titulacion}
            Costo por hora: {costoPorHora:.1f} USD

            ================================================
            """)