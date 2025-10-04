#################### MODELO 2 ######################
import math


from ejercicio_5.catalogo_de_planetas import CuerpoCeleste


class Planeta(CuerpoCeleste):
    def __init__(self, id_celeste, nombre, masa_kg, radio_km, distancia_sol_km):
        super().__init__(id_celeste, nombre, masa_kg)
        if radio_km <= 0:
            raise ValueError("El radio debe ser mayor a 0.")
        if distancia_sol_km <= 0:
            raise ValueError("La distancia al sol debe ser mayor a 0.")
        self._radio_km = radio_km
        self._distancia_sol_km = distancia_sol_km

        self._registrar_evento("creación_planeta", None,
                               f"radio={radio_km} km, distancia_sol={distancia_sol_km} km")

    @property
    def radio_km(self):
        return self._radio_km
    @property
    def distancia_sol_km(self):
        return self._distancia_sol_km

    def actualizar_radio(self, nuevo_radio):
        if nuevo_radio <= 0:
            raise ValueError("El radio debe ser mayor a 0.")
        anterior = self._radio_km
        self._radio_km = nuevo_radio
        self._registrar_evento("radio", anterior, nuevo_radio)

    def actualizar_distancia_sol(self, nueva_distancia):
        if nueva_distancia <= 0:
            raise ValueError("La distancia al sol debe ser mayor a 0.")
        anterior = self._distancia_sol_km
        self._distancia_sol_km = nueva_distancia
        self._registrar_evento("distancia_sol", anterior, nueva_distancia)

    def calcular_densidad(self):
        # Volumen de esfera = 4/3 * pi * r^3
        volumen = (4/3) * math.pi * (self._radio_km ** 3)
        densidad = self.masa_kg / volumen
        return densidad

    def comparar_distancia(self, otro_planeta):
        if not isinstance(otro_planeta, Planeta):
            raise TypeError("La comparación solo es válida entre planetas.")
        if self._distancia_sol_km < otro_planeta.distancia_sol_km:
            return f"{self.nombre} está más cerca del sol que {otro_planeta.nombre}"
        elif self._distancia_sol_km > otro_planeta.distancia_sol_km:
            return f"{otro_planeta.nombre} está más cerca del sol que {self.nombre}"
        else:
            return f"{self.nombre} y {otro_planeta.nombre} están a la misma distancia del sol"



estrella = CuerpoCeleste(1, "Estrella X", 2e30)
print("Creado:", estrella.consultar_ficha())


tierra = Planeta(2, "Tierra", 5.97e24, 6371, 149_600_000)

marte = Planeta(3, "Marte", 6.42e23, 3389, 227_900_000)


print(" Densidad Tierra:", tierra.calcular_densidad(), "kg/km³")


print("Comparación:", tierra.comparar_distancia(marte))


try:
    fail_planeta = Planeta(4, "Fail", 1e23, 0, 100_000)
except ValueError as e:
    print("Error:", e)

marte.actualizar_masa(7e23)
print("Nueva masa Marte:", marte.masa_kg)

try:
    tierra.radio_km = 10000
except AttributeError as e:
    print("No se puede modificar directamente:", e)
