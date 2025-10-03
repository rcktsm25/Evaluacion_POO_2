##______________________ejercico_1______________________##

from gestion_parcelas import Parcela 


p = Parcela(id_parcela=1, superficie_ha=10.5, cultivo_actual="Trigo")

p.actualizar_cultivo("Maíz")
p.rectificar_superficie(12, "Medición más precisa")
p.desactivar("Descanso de la tierra")
try:
    p.actualizar_cultivo("Soja")  # Esto lanzará excepción
except Exception as e:
    print("Error:", e)

p.activar("Se reanuda la producción")
p.actualizar_cultivo("Soja")

p.mostrar_historial()

