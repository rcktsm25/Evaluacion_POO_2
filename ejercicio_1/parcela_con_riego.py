from datetime import datetime


class Parcela:
    def __init__(self, id_parcela, superficie_ha, cultivo_actual, estado="activa"):
        self.id_parcela = id_parcela
        self.superficie_ha = superficie_ha
        self.cultivo_actual = cultivo_actual
        self.estado = estado

    def actualizar_cultivo(self, nuevo_cultivo):
        self.cultivo_actual = nuevo_cultivo

    def desactivar(self, motivo):
        self.estado = "inactiva"

class ParcelaConRiego(Parcela):
    def __init__(self, id_parcela, superficie_ha, cultivo_actual, estado="activa"):
        super().__init__(id_parcela, superficie_ha, cultivo_actual, estado)
        self._litros_disponibles = 0
        self.tasa_riego_l_ha = 0 
        self.umbral_min_litros = 0
        self.estado_riego = "habilitado" if estado == "activa" else "inhabilitado"
        self.eventos_riego = []

    def _registrar_evento(self, tipo, descripcion):
        evento = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tipo": tipo,
            "descripcion": descripcion
        }
        self.eventos_riego.append(evento)

    @property
    def litros_disponibles(self):
        return self._litros_disponibles

    def configurar_tasa(self, l_ha):
        if l_ha <= 0:
            raise ValueError("La tasa de riego debe ser mayor a 0.")
        self.tasa_riego_l_ha = l_ha
        self._registrar_evento("CONFIGURACIÓN_RIEGO", f"Tasa configurada en {l_ha} L/ha")

    def configurar_umbral(self, litros):
        if litros < 0:
            raise ValueError("El umbral no puede ser negativo.")
        self.umbral_min_litros = litros
        self._registrar_evento("CONFIGURACIÓN_RIEGO", f"Umbral configurado en {litros} L")

    def habilitar_riego(self):
        self.estado_riego = "habilitado"
        self._registrar_evento("RIEGO", "Riego habilitado")

    def inhabilitar_riego(self):
        self.estado_riego = "inhabilitado"
        self._registrar_evento("RIEGO", "Riego inhabilitado")

    def cargar_agua(self, litros):
        if litros <= 0:
            raise ValueError("Debe cargar una cantidad positiva de litros.")
        saldo_antes = self._litros_disponibles
        self._litros_disponibles += litros
        self._registrar_evento_riego("CARGA", litros, litros, saldo_antes, self._litros_disponibles, "carga")

    def regar_automatico(self, modo):
        if self.estado == "inactiva":
            self.estado_riego = "inhabilitado"
            raise Exception("No se puede regar una parcela inactiva.")
        if self.estado_riego == "inhabilitado":
            raise Exception("El riego está inhabilitado.")
        if self.tasa_riego_l_ha <= 0:
            raise Exception("Debe configurar una tasa de riego válida.")

        demanda = self.superficie_ha * self.tasa_riego_l_ha
        saldo_antes = self._litros_disponibles

        if modo == "estricto":
            if self._litros_disponibles - demanda >= self.umbral_min_litros:
                self._litros_disponibles -= demanda
                self._registrar_evento_riego("RIEGO", demanda, demanda, saldo_antes, self._litros_disponibles, "estricto")
            else:
                raise Exception("No hay agua suficiente para riego estricto (no se cumple el umbral).")

        elif modo == "parcial":
            posible = self._litros_disponibles - self.umbral_min_litros
            litros_aplicados = min(demanda, max(0, posible))
            if litros_aplicados > 0:
                self._litros_disponibles -= litros_aplicados
                self._registrar_evento_riego("RIEGO", demanda, litros_aplicados, saldo_antes, self._litros_disponibles, "parcial")
            else:
                raise Exception("No se puede regar ni en modo parcial (no hay agua suficiente).")
        else:
            raise ValueError("Modo inválido. Use 'estricto' o 'parcial'.")

    # Métodos internos
    def _registrar_evento_riego(self, tipo, litros_solicitados, litros_aplicados, saldo_antes, saldo_despues, modo):
        evento = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tipo": tipo,
            "litros_solicitados": litros_solicitados,
            "litros_aplicados": litros_aplicados,
            "saldo_antes": saldo_antes,
            "saldo_despues": saldo_despues,
            "modo": modo
        }
        self.eventos_riego.append(evento)


p = ParcelaConRiego(1, 10.50, "Trigo", "activa")


p.actualizar_cultivo("Maíz")


p.configurar_tasa(1500)      
p.configurar_umbral(2000) 
p.cargar_agua(20000)         

# Riego estricto
p.regar_automatico("estricto")  
print(p.litros_disponibles) 

p.desactivar("Descanso")
try:
    p.regar_automatico("estricto")
except Exception as e:
    print("Error:", e)

p2 = ParcelaConRiego(2, 10.50, "Trigo")
p2.configurar_tasa(1500)
p2.configurar_umbral(2000)
p2.cargar_agua(3000)
p2.regar_automatico("parcial")
print(p2.litros_disponibles)  
