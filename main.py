##______________________ejercico_1______________________##

from gestion_parcelas import Parcela
from parcela_con_riego import ParcelaConRiego 


p = Parcela(id_parcela=1, superficie_ha=10.5, cultivo_actual="choclo")

p.actualizar_cultivo("choclo")
p.rectificar_superficie(12, "Medición más precisa")
p.desactivar("Descanso de la tierra")
try:
    p.actualizar_cultivo("manzanas")  
except ValueError as e:
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


##_____________________ejercicio_4______________________##

from ejercicio_4.vehiculo import Auto, Vehiculo



v = Vehiculo(1, "ABCD12", 1450)
print(v.consultar_ficha())


v.actualizar_peso(1500)   
try:
    v.actualizar_peso(0) 
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

# Vaciar auto
a.vaciar_auto("fin de turno")


a.inhabilitar("fallo técnico")
try:
    a.subir_personas(1)  
except Exception as e:
    print("Error:", e)


print("Historial vehículo:", v.historial_eventos)
print("Eventos auto:", a.eventos_ocupacion)


##_____________________ejercicio_5______________________##
from ejercicio_5.catalogo_de_planetas import CuerpoCeleste
#################### MODELO 1 ##############################
estrella = CuerpoCeleste(1, "Estrella X", 1.989e30)
print(estrella.consultar_ficha())

estrella.actualizar_nombre("Estrella Y")

estrella.actualizar_masa(2.0e30)

print(estrella.consultar_ficha())
print("Historial:", estrella.historial_eventos)
#################### MODELO 2 ##############################
from ejercicio_5.catalogo_de_planeta_2 import Planeta
estrella = CuerpoCeleste(1, "Estrella X", 2e30)
print(" Creado:", estrella.consultar_ficha())


tierra = Planeta(2, "Tierra", 5.97e24, 6371, 149_600_000)


marte = Planeta(3, "Marte", 6.42e23, 3389, 227_900_000)


print("Densidad Tierra:", tierra.calcular_densidad(), "kg/km³")


print(" Comparación:", tierra.comparar_distancia(marte))

try:
    fail_planeta = Planeta(4, "Fail", 1e23, 0, 100_000)
except ValueError as e:
    print(" Error:", e)


marte.actualizar_masa(7e23)
print(" Nueva masa Marte:", marte.masa_kg)


try:
    tierra.radio_km = 10000
except AttributeError as e:
    print(" No se puede modificar directamente:", e)
######################################################################