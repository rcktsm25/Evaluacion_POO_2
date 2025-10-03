##______________________ejercico_1______________________##

from gestion_parcelas import Parcela 


p = Parcela(id_parcela=1, superficie_ha=10.5, cultivo_actual="choclo")

p.actualizar_cultivo("choclo")
p.rectificar_superficie(12, "Medición más precisa")
p.desactivar("Descanso de la tierra")
try:
    p.actualizar_cultivo("manzanas")  
except Exception as e:
    print("Error:", e)

p.activar("Se reanuda la producción")
p.actualizar_cultivo("manzanas")

p.mostrar_historial()


