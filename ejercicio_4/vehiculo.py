from datetime import datetime

class Vehiculo:
    def __init__(self, id_vehiculo, patente, peso_kg, usuario="sistema"):
        if not patente or not isinstance(patente, str) or patente.strip() == "":
            raise ValueError("Patente inválida.")
        if peso_kg <= 0:
            raise ValueError("El peso debe ser mayor a 0.")

        self.id_vehiculo = id_vehiculo
        self.patente = patente
        self.peso_kg = peso_kg
        self.estado = "habilitado"
        self.historial_eventos = []

        self._registrar_evento(usuario, "alta", f"Vehículo {patente} creado con peso {peso_kg} kg")

    def _registrar_evento(self, usuario, tipo_evento, detalle):
        self.historial_eventos.append({
            "fecha": datetime.now(),
            "usuario": usuario,
            "tipo_evento": tipo_evento,
            "detalle": detalle
        })

    def actualizar_peso(self, nuevo_peso, usuario="sistema"):
        if self.estado == "inhabilitado":
            raise ValueError("No se puede actualizar el peso: vehículo inhabilitado.")
        if nuevo_peso <= 0:
            raise ValueError("El peso debe ser mayor a 0.")
        anterior = self.peso_kg
        self.peso_kg = nuevo_peso
        self._registrar_evento(usuario, "actualización_peso", f"{anterior} → {nuevo_peso} kg")

    def habilitar(self, motivo, usuario="sistema"):
        anterior = self.estado
        self.estado = "habilitado"
        self._registrar_evento(usuario, "habilitar", f"{anterior} → habilitado ({motivo})")

    def inhabilitar(self, motivo, usuario="sistema"):
        anterior = self.estado
        self.estado = "inhabilitado"
        self._registrar_evento(usuario, "inhabilitar", f"{anterior} → inhabilitado ({motivo})")

    def consultar_ficha(self):
        return {
            "id": self.id_vehiculo,
            "patente": self.patente,
            "peso_kg": self.peso_kg,
            "estado": self.estado,
            "ultima_actualizacion": self.historial_eventos[-1]["fecha"] if self.historial_eventos else None,
            "cambios_estado": sum(1 for e in self.historial_eventos if e["tipo_evento"] in ["habilitar", "inhabilitar"])
        }


class Auto(Vehiculo):
    def __init__(self, id_vehiculo, patente, peso_kg, asientos_totales, sistema_retencion_infantil="si", usuario="sistema"):
        super().__init__(id_vehiculo, patente, peso_kg, usuario)
        if asientos_totales < 1:
            raise ValueError("El auto debe tener al menos 1 asiento.")

        self.asientos_totales = asientos_totales
        self.ocupantes_actuales = 0
        self.sistema_retencion_infantil = sistema_retencion_infantil
        self.eventos_ocupacion = []

        self._registrar_evento(usuario, "alta_auto", f"Auto creado con {asientos_totales} asientos y 0 ocupantes")

    def _registrar_ocupacion(self, accion, cantidad, antes, despues):
        self.eventos_ocupacion.append({
            "fecha": datetime.now(),
            "accion": accion,
            "cantidad": cantidad,
            "ocupantes_antes": antes,
            "ocupantes_despues": despues
        })

    def subir_personas(self, n, usuario="sistema"):
        if self.estado == "inhabilitado":
            raise ValueError("No se puede subir personas: vehículo inhabilitado.")
        if n < 1:
            raise ValueError("Debe subir al menos 1 persona.")
        if self.ocupantes_actuales + n > self.asientos_totales:
            raise ValueError("No hay suficientes asientos disponibles.")
        antes = self.ocupantes_actuales
        self.ocupantes_actuales += n
        self._registrar_ocupacion("subida", n, antes, self.ocupantes_actuales)

    def bajar_personas(self, n, usuario="sistema"):
        if self.estado == "inhabilitado":
            raise ValueError("No se puede bajar personas: vehículo inhabilitado.")
        if n < 1:
            raise ValueError("Debe bajar al menos 1 persona.")
        if self.ocupantes_actuales - n < 0:
            raise ValueError("No puede quedar ocupación negativa.")
        antes = self.ocupantes_actuales
        self.ocupantes_actuales -= n
        self._registrar_ocupacion("bajada", n, antes, self.ocupantes_actuales)

    def reconfigurar_asientos(self, nuevo_total, motivo, usuario="sistema"):
        if nuevo_total < 1:
            raise ValueError("El número de asientos debe ser al menos 1.")
        if self.ocupantes_actuales > nuevo_total:
            raise ValueError("No se puede reducir asientos por debajo de los ocupantes actuales.")
        anterior = self.asientos_totales
        self.asientos_totales = nuevo_total
        self._registrar_evento(usuario, "reconfigurar_asientos", f"{anterior} → {nuevo_total} ({motivo})")

    def vaciar_auto(self, motivo, usuario="sistema"):
        antes = self.ocupantes_actuales
        self.ocupantes_actuales = 0
        self._registrar_ocupacion("vaciar", antes, antes, 0)
        self._registrar_evento(usuario, "vaciar_auto", motivo)

    def consultar_ocupacion(self):
        return {
            "ocupantes": self.ocupantes_actuales,
            "asientos_libres": self.asientos_totales - self.ocupantes_actuales,
            "tasa_ocupacion_%": (self.ocupantes_actuales / self.asientos_totales) * 100
        }



v = Vehiculo(1, "ABCD12", 1450)
print(v.consultar_ficha())


v.actualizar_peso(1500)   # OK
try:
    v.actualizar_peso(0)  # Rechazo
except Exception as e:
    print("Error:", e)


v.inhabilitar("mantención")
try:
    v.actualizar_peso(1600)  
except Exception as e:
    print("Error:", e)
v.habilitar("mantención finalizada")

a = Auto(2, "EFGH34", 1200, 5)


a.subir_personas(3)  
try:
    a.subir_personas(3)  
except Exception as e:
    print("Error:", e)


a.bajar_personas(2)   
try:
    a.bajar_personas(5) 
except Exception as e:
    print("Error:", e)


a.reconfigurar_asientos(2, "reparación")  
try:
    a.reconfigurar_asientos(0, "inválido")  
except Exception as e:
    print("Error:", e)


a.vaciar_auto("fin de turno")


a.inhabilitar("fallo técnico")
try:
    a.subir_personas(1)  
except Exception as e:
    print("Error:", e)

print("Historial eventos vehículo:", v.historial_eventos)
print("Eventos ocupación auto:", a.eventos_ocupacion)
