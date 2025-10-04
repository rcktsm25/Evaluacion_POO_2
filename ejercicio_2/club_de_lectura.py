from datetime import datetime

class Publicacion:
    def __init__(self, id_publicacion, titulo, anio):
        if not titulo.strip():
            raise ValueError("El título no puede estar vacío.")
        if anio < 1450:
            raise ValueError("El año debe ser >= 1450 (inicio de la imprenta moderna).")

        self.id_publicacion = id_publicacion
        self.titulo = titulo
        self.anio = anio
        self.historial_eventos = []  
    

    def actualizar_titulo(self, nuevo_titulo):
        if not nuevo_titulo.strip():
            raise ValueError("El nuevo título no puede estar vacío.")
        evento = {
            "fecha": datetime.now(),
            "campo": "titulo",
            "anterior": self.titulo,
            "nuevo": nuevo_titulo
        }
        self.historial_eventos.append(evento)
        self.titulo = nuevo_titulo

    def actualizar_año(self, nuevo_año):
        if nuevo_año < 1450:
            raise ValueError("El año debe ser >= 1450.")
        evento = {
            "fecha": datetime.now(),
            "campo": "año",
            "anterior": self.anio,
            "nuevo": nuevo_año
        }
        self.historial_eventos.append(evento)
        self.anio = nuevo_año


class Libro(Publicacion):
    def __init__(self, id_publicacion, titulo, anio, paginas_totales):
        super().__init__(id_publicacion, titulo, anio)

        if paginas_totales <= 0:
            raise ValueError("El libro debe tener más de 0 páginas.")

        self._paginas_totales = paginas_totales
        self._paginas_leidas = 0
        self.eventos_lectura = []  # solo lectura

    @property
    def paginas_totales(self):
        return self._paginas_totales

    @property
    def paginas_leidas(self):
        return self._paginas_leidas

    def leer(self, paginas):
        if paginas <= 0:
            raise ValueError("No se pueden leer páginas negativas o cero.")
        if self._paginas_leidas + paginas > self._paginas_totales:
            raise ValueError("No se pueden leer más páginas de las que quedan.")

        self._paginas_leidas += paginas
        evento = {
            "fecha": datetime.now(),
            "paginas_leidas": paginas,
            "total_acumulado": self._paginas_leidas
        }
        self.eventos_lectura.append(evento)

    def consultar_progreso(self):
        progreso = (self._paginas_leidas / self._paginas_totales) * 100
        return round(progreso)





pub1 = Publicacion(1, "Don Quijote", 1605)
print(f"Publicación creada: {pub1.titulo}, año {pub1.anio}")



try:
    pub2 = Publicacion(2, "Algo antiguo", 1400)
except ValueError as e:
    print("Error:", e)


libro = Libro(3, "Cien años de soledad", 1967, 500)


print(f"Libro creado: {libro.titulo}, páginas: {libro.paginas_totales}")




libro.leer(120)




print(f"Páginas leídas: {libro.paginas_leidas}, Progreso: {libro.consultar_progreso()}%")



try:
    libro.leer(400)
except ValueError as e:    print("Error:", e)
print("Progreso actual:", libro.consultar_progreso(), "%")

libro.actualizar_año(1970)


print("Nuevo año del libro:", libro.anio)



print("\nHistorial de eventos:")
for e in libro.historial_eventos:
    print(f"- {e['fecha']} | {e['campo']}: {e['anterior']} -> {e['nuevo']}")

    print("\nEventos de lectura:")
for e in libro.eventos_lectura:
    print(f"- {e['fecha']} | Leídas: {e['paginas_leidas']} (Acumulado: {e['total_acumulado']})")
