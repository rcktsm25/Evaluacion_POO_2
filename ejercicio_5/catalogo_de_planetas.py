from datetime import datetime
#################### MODELO 1 #########################
class CuerpoCeleste:
    def __init__(self, id_celeste, nombre, masa_kg):
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre no puede estar vacío.")
        if masa_kg <= 0:
            raise ValueError("La masa debe ser mayor a 0.")

        self.id_celeste = id_celeste
        self.nombre = nombre
        self.masa_kg = masa_kg
        self.historial_eventos = []

        self._registrar_evento("creación", None, f"nombre={nombre}, masa={masa_kg} kg")

    def _registrar_evento(self, campo, anterior, nuevo):
        self.historial_eventos.append({
            "fecha": datetime.now(),
            "campo": campo,
            "valor_anterior": anterior,
            "valor_nuevo": nuevo
        })

    def actualizar_nombre(self, nuevo_nombre):
        if not nuevo_nombre or not isinstance(nuevo_nombre, str):
            raise ValueError("El nombre no puede estar vacío.")
        anterior = self.nombre
        self.nombre = nuevo_nombre
        self._registrar_evento("nombre", anterior, nuevo_nombre)

    def actualizar_masa(self, nueva_masa):
        if nueva_masa <= 0:
            raise ValueError("La masa debe ser mayor a 0.")
        anterior = self.masa_kg
        self.masa_kg = nueva_masa
        self._registrar_evento("masa", anterior, nueva_masa)

    def consultar_ficha(self):
        return {
            "id": self.id_celeste,
            "nombre": self.nombre,
            "masa_kg": self.masa_kg,
            "ultima_actualizacion": self.historial_eventos[-1]["fecha"] if self.historial_eventos else None,
            "numero_modificaciones": len(self.historial_eventos)
        }


estrella = CuerpoCeleste(1, "Estrella X", 1.989e30)
print(estrella.consultar_ficha())


estrella.actualizar_nombre("Estrella Y")


estrella.actualizar_masa(2.0e30)


print(estrella.consultar_ficha())
print("Historial:", estrella.historial_eventos)
