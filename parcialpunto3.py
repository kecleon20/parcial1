class BitacoraBobaFett:
    def __init__(self):
        self.bitacora = []

    def agregar_mision(self, planeta, objetivo, recompensa):
        mision = (planeta, objetivo, recompensa)
        self.bitacora.append(mision)

    def mostrar_planetas_visitados(self):
        print("Planetas visitados en orden de misiones:")
        for mision in self.bitacora:
            print(mision[0])

    def calcular_creditos_recaudados(self):
        total_creditos = 0
        for mision in self.bitacora:
            total_creditos += mision[2]
        return total_creditos

    def encontrar_mision_han_solo(self):
        for i, mision in enumerate(self.bitacora):
            if mision[1] == "Han Solo":
                return i + 1, mision[0]

# Bitacora de Boba Fett
bitacora = BitacoraBobaFett()
bitacora.agregar_mision("Tatooine", "Jabba the Hutt", 5000)
bitacora.agregar_mision("Bespin", "Lando Calrissian", 8000)
bitacora.agregar_mision("Endor", "Leia Organa", 6000)
bitacora.agregar_mision("Hoth", "Han Solo", 10000)
bitacora.agregar_mision("Coruscant", "Bail Organa", 4000)

# Mostrar los planetas visitados en orden de misiones
bitacora.mostrar_planetas_visitados()

# Calcular el total de creditos recaudados
total_creditos = bitacora.calcular_creditos_recaudados()
print(f"Total de créditos recaudados: {total_creditos} créditos galácticos")

# Encontrar la misión de captura de Han Solo y el planeta correspondiente
numero_mision, planeta = bitacora.encontrar_mision_han_solo()
print(f"Han Solo fue capturado en la misión número {numero_mision} en el planeta {planeta}")
