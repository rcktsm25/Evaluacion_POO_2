from datetime import datetime

class Parcela:
    def __init__(self, id_parcela, superficie_ha, cultivo_actual, estado="activa"):
        if superficie_ha <= 0:
            raise ValueError("La superficie debe ser mayor a 0.")
        if not cultivo_actual.strip():
            raise ValueError("El cultivo no puede estar vacío.")
        
        self.id_parcela = id_parcela
        self._superficie_ha = round(superficie_ha, 2)   
        self.cultivo_actual = cultivo_actual
        self.estado = estado
        self.historial_eventos = []

        self._registrar_evento("CREACIÓN", f"Parcela creada con cultivo '{cultivo_actual}' y superficie {self._superficie_ha} ha")

    @property
    def superficie_ha(self):
        return self._superficie_ha

    # --- Operaciones ---
    def actualizar_cultivo(self, nuevo_cultivo):
        if self.estado == "inactiva":
            raise RuntimeError("No se puede actualizar cultivo en una parcela inactiva.")
        if not nuevo_cultivo.strip():
            raise ValueError("El cultivo no puede estar vacío.")
        
        cultivo_prev = self.cultivo_actual
        self.cultivo_actual = nuevo_cultivo
        self._registrar_evento("CAMBIO_CULTIVO", f"De '{cultivo_prev}' a '{nuevo_cultivo}'")

    def activar(self, motivo):
        if self.estado == "activa":
            return  # ya está activa, no hace nada
        self.estado = "activa"
        self._registrar_evento("ACTIVACIÓN", motivo)

    def desactivar(self, motivo):
        if self.estado == "inactiva":
            return  # ya está inactiva
        self.estado = "inactiva"
        self._registrar_evento("DESACTIVACIÓN", motivo)

    def rectificar_superficie(self, nueva_superficie, motivo):
        if nueva_superficie <= 0:
            raise ValueError("La superficie debe ser mayor a 0.")
        superficie_prev = self._superficie_ha
        self._superficie_ha = round(nueva_superficie, 2)
        self._registrar_evento("RECTIFICACIÓN_SUPERFICIE", f"De {superficie_prev} ha a {self._superficie_ha} ha. Motivo: {motivo}")

    # --- Método interno ---
    def _registrar_evento(self, tipo, detalle):
        evento = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tipo": tipo,
            "detalle": detalle
        }
        self.historial_eventos.append(evento)

    def mostrar_historial(self):
        for e in self.historial_eventos:
            print(f"[{e['fecha']}] {e['tipo']}: {e['detalle']}")
