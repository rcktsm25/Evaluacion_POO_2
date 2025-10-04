from datetime import datetime

class Actividad:
    def __init__(self, id_actividad, nombre, duracion_min):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if duracion_min < 1:
            raise ValueError("La duración mínima es 1 minuto.")

        self.id_actividad = id_actividad
        self.nombre = nombre
        self.duracion_min = duracion_min
        self.historial_eventos = []  # solo lectura

    def actualizar_nombre(self, nuevo_nombre):
        if not nuevo_nombre.strip():
            raise ValueError("El nuevo nombre no puede estar vacío.")
        evento = {
            "fecha": datetime.now(),
            "campo": "nombre",
            "anterior": self.nombre,
            "nuevo": nuevo_nombre
        }
        self.historial_eventos.append(evento)
        self.nombre = nuevo_nombre

    def actualizar_duracion(self, nueva_duracion):
        if nueva_duracion < 1:
            raise ValueError("La duración mínima es 1 minuto.")
        evento = {
            "fecha": datetime.now(),
            "campo": "duracion_min",
            "anterior": self.duracion_min,
            "nuevo": nueva_duracion
        }
        self.historial_eventos.append(evento)
        self.duracion_min = nueva_duracion



