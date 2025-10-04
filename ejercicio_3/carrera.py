from datetime import datetime

class Actividad:
    def __init__(self, id_actividad, nombre, duracion_min):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if duracion_min < 1:
            raise ValueError("La duración mínima es 1 minuto.")
        
        self.id_actividad = id_actividad
        self.nombre = nombre
        self._duracion_min = duracion_min
        self.historial_eventos = []

    @property
    def duracion_min(self):
        return self._duracion_min

    def actualizar_nombre(self, nuevo_nombre):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
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
            "anterior": self._duracion_min,
            "nuevo": nueva_duracion
        }
        self.historial_eventos.append(evento)
        self._duracion_min = nueva_duracion


class Carrera(Actividad):
    def __init__(self, id_actividad, nombre, duracion_min, distancia_km):
        super().__init__(id_actividad, nombre, duracion_min)
        if distancia_km <= 0:
            raise ValueError("La distancia debe ser mayor a 0.")
        self._distancia_km = distancia_km
        self.eventos_registro = []

        # Registrar evento inicial
        self.eventos_registro.append({
            "fecha": datetime.now(),
            "distancia_registrada": distancia_km,
            "duracion_acumulada": self.duracion_min
        })

    @property
    def distancia_km(self):
        return self._distancia_km

    def registrar_distancia(self, nueva_distancia):
        if nueva_distancia <= 0:
            raise ValueError("La distancia registrada debe ser mayor a 0.")
        self._distancia_km += nueva_distancia
        self.eventos_registro.append({
            "fecha": datetime.now(),
            "distancia_registrada": nueva_distancia,
            "duracion_acumulada": self.duracion_min
        })

    def calcular_ritmo(self):
        if self._distancia_km <= 0:
            raise ValueError("No hay distancia registrada válida.")
        return round(self.duracion_min / self._distancia_km, 2)



yoga = Actividad(1, "Yoga", 60)
print(f"✅ Actividad creada: {yoga.nombre}, duración {yoga.duracion_min} min")


try:
    fail = Actividad(2, "Meditación", 0)
except ValueError as e:
    print("Error:", e)


carrera = Carrera(3, "Carrera 10K", 50, 10)
print(f"Carrera creada: {carrera.nombre}, {carrera.distancia_km} km en {carrera.duracion_min} min")


print("Ritmo:", carrera.calcular_ritmo(), "min/km")



try:
    carrera.registrar_distancia(-3)
except ValueError as e:
    print("Error al registrar distancia:", e)


carrera.actualizar_duracion(55)
print("🔄 Duración actualizada:", carrera.duracion_min, "min")


try:
    carrera.distancia_km = 42
except AttributeError as e:
    print("Error: no se puede alterar distancia_km directamente")


print("\nHistorial de eventos:")
for e in carrera.historial_eventos:
    print(f"- {e['fecha']} | {e['campo']}: {e['anterior']} -> {e['nuevo']}")

# Mostrar eventos de registro
print("\n Eventos de registro:")
for e in carrera.eventos_registro:
    print(f"- {e['fecha']} | Distancia registrada: {e['distancia_registrada']} km, Duración: {e['duracion_acumulada']} min")
