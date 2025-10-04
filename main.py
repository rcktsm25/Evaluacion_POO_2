##______________________ejercico_1______________________##

from gestion_parcelas import Parcela
from parcela_con_riego import ParcelaConRiego 


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

##############MODELO 2 ########################
from datetime import datetime

from gestion_parcelas import Parcela

p = ParcelaConRiego(1, 10.50, "Trigo", "activa")


p.actualizar_cultivo("Maíz")


p.configurar_tasa(1500)      
p.configurar_umbral(2000) 
p.cargar_agua(20000)         


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


##______________________ejercico_2______________________##









##______________________ejercicio_3______________________##
from ejercicio_3.registro_actividad_fisica import Actividad


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
print(f" Nombre actualizado: {act1.nombre}")


act1.actualizar_duracion(75)
print(f"Duración actualizada: {act1.duracion_min} min")


print("\nHistorial de eventos:")
for e in act1.historial_eventos:
    print(f"- {e['fecha']} | {e['campo']}: {e['anterior']} -> {e['nuevo']}")
