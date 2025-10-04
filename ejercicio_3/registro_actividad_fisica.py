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




act1 = Actividad(1, "Ciclismo", 60)
print(f"Actividad creada: {act1.nombre}, duración: {act1.duracion_min} min")

try:
    act2 = Actividad(2, "", 30)
except ValueError as e:
    print("Error:", e)

try:
    act3 = Actividad(3, "Natación", 0)
except ValueError as e:
    print("Error:", e)


act1.actualizar_nombre("Ciclismo de montaña")
print(f"Nombre actualizado: {act1.nombre}")


act1.actualizar_duracion(75)
print(f"Duración actualizada: {act1.duracion_min} min")


print("\nHistorial de eventos:")
for e in act1.historial_eventos:
    print(f"- {e['fecha']} | {e['campo']}: {e['anterior']} -> {e['nuevo']}")
