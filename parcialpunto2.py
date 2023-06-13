from collections import deque

# Definir la lista principal de superhéroes
lista_avengers = [
    ('Ant-Man', 'Scott Lang', 'Avengers', 1962),
    ('Black Widow', 'Natasha Romanoff', 'Avengers', 1964),
    ('Captain America', 'Steve Rogers', 'Avengers', 1941),
    ('Capitana Marvel', '', 'Avengers', 1968),
    ('Hawkeye', 'Clint Barton', 'Avengers', 1964),
    ('Iron Man', 'Tony Stark', 'Avengers', 1963),
    ('Star Lord', 'Peter Quill', 'Guardianes de la galaxia', 1976),
    ('Thor', 'Thor Odinson', 'Avengers', 1962),
    ("Rocket Raccoonn", "Raccoonn", "Guardianes de la galaxia", 1976),
    ("Groot", "Groot", "Guardianes de la galaxia", 1960),
    ("Gamora", "Gamora Zen Whoberi Ben Titan", "Guardianes de la galaxia", 1975),
    ("Dax el Destructor", "Arthur Sampson Douglas", "Guardianes de la galaxia", 1973),
    ("Mantis", "Mantis Brandt", "Guardianes de la galaxia", 1973),
    ("Hombre Elastico","Reed Richards", "Los cuatro fantásticos", 1961),
    ("Mujer Invisible","Susan Storm", "Los cuatro fantásticos", 1961),
    ("Antorcha Humana","Jonathan Storm", "Los cuatro fantásticos", 1961),
    ("Mole","Ben Grimm", "Los cuatro fantásticos", 1961),
    ("Vlanck Widow", "Natalia Alianovna", "Avengers", 1964)
]

# a. Determinar si "Capitana Marvel" está en la lista y mostrar su nombre de personaje
nombre_personaje_capitana_marvel = ''
for heroe in lista_avengers:
    if heroe[0] == 'Capitana Marvel':
        nombre_personaje_capitana_marvel = heroe[1]
        break

if nombre_personaje_capitana_marvel != '':
    print("El nombre de personaje de Capitana Marvel es: {nombre_personaje_capitana_marvel}")
else:
    print("Capitana Marvel no está en la lista.")

# b. Almacenar los superhéroes que pertenezcan al grupo "Guardianes de la galaxia" en una cola e indicar cuántos son
guardianes_de_la_galaxia = deque()
for heroe in lista_avengers:
    if heroe[2] == 'Guardianes de la galaxia':
        guardianes_de_la_galaxia.append(heroe[0])

print(f"Hay {len(guardianes_de_la_galaxia)} superhéroes en el grupo Guardianes de la galaxia.")
print(f"Superhéroes en el grupo Guardianes de la galaxia:", list(guardianes_de_la_galaxia))

# c. Mostrar de manera descendente los superhéroes que pertenecen al grupo "Los cuatro fantásticos" y "Guardianes de la galaxia"
grupo_cuatro_fantasticos = "Los cuatro fantásticos"
grupo_guardianes = "Guardianes de la galaxia"

superheroes_cuatro_fantasticos = []
superheroes_guardianes = []

for heroe in lista_avengers:
    if heroe[2] == grupo_cuatro_fantasticos:
        superheroes_cuatro_fantasticos.append(heroe[0])
    elif heroe[2] == grupo_guardianes:
        superheroes_guardianes.append(heroe[0])

print(f"Superhéroes del grupo {grupo_cuatro_fantasticos} (descendente):")
for heroe in reversed(superheroes_cuatro_fantasticos):
    print(heroe)

print(f"Superhéroes del grupo {grupo_guardianes} (descendente):")
for heroe in reversed(superheroes_guardianes):
    print(heroe)

# d. Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960
superheroes_posterior_1960 = [heroe[0] for heroe in lista_avengers if heroe[3] > 1960]
print("Superhéroes cuyo nombre de personaje tiene año de aparición posterior a 1960:", superheroes_posterior_1960)

# e.Hemos detectado que la superhéroe “Black Widow” está mal
#cargada por un error de tipeo, figura como “Vlanck Widow”,
#modifique dicho superhéroe para solucionar este problema.
for i, heroe in enumerate(lista_avengers):
    if heroe[0] == 'Vlanck Widow':
        lista_avengers[i] = ('Black Widow', heroe[1], heroe[2], heroe[3])
        break

# f. Agregar los personajes faltantes de la lista auxiliar a la lista principal
lista_auxiliar = [('Black Cat', '', 'Avengers', 1979), ('Hulk', '', '', 1962), ('Rocket Racoonn', 'Racoonn', 'Guardianes de la galaxia', 1976), ('Loki', '', 'Avengers', 1962)]

for personaje in lista_auxiliar:
    if personaje not in lista_avengers:
        lista_avengers.append(personaje)

# g. Mostrar todos los personajes que comienzan con C, P o S
personajes_cps = [heroe[1] for heroe in lista_avengers if heroe[1] and heroe[1][0] in ('C', 'P', 'S')]
print("Personajes que comienzan con C, P o S:", personajes_cps)

# h. Cargar al menos 20 superhéroes a la lista
lista_avengers.extend([
    ('Spider-Man', 'Peter Parker', 'Avengers', 1962),
    ('Wolverine', 'Logan', 'X-Men', 1974),
    ('Doctor Strange', 'Stephen Strange', 'Avengers', 1963),
    ('Scarlet Witch', 'Wanda Maximoff', 'Avengers', 1964),
    ('Black Panther', 'TChalla', 'Avengers', 1966),
    ('Vision', '', 'Avengers', 1968),
    ('Capitana Marvel', 'Carol Denvers', 'Avengers', 1968),
    ('Thanos', '', 'Villanos', 1973),
    ('Quicksilver', 'Pietro Maximoff', 'Avengers', 1964),
    ('Deadpool', 'Wade Wilson', 'X-Men', 1991),
    ('Hawkeye', 'Kate Bishop', 'Avengers', 2005),
    ('Jessica Jones', '', '', 2001),
    ('Daredevil', 'Matt Murdock', '', 1964),
    ('Falcon', 'Sam Wilson', 'Avengers', 1969),
    ('Luke Cage', '', '', 1972),
    ('Iron Fist', 'Danny Rand', '', 1974),
    ('She-Hulk', 'Jennifer Walters', 'Avengers', 1980),
    ('Winter Soldier', 'Bucky Barnes', 'Avengers', 2005),
    ('Nick Fury', '', 'Avengers', 1963),
    ('Elektra', '', '', 1981)
])

# Imprimir la lista actualizada
print("\nLista actualizada de superhéroes:")
for heroe in lista_avengers:
    print(f"{heroe[0]} - {heroe[1]} - {heroe[2]} - {heroe[3]}")
