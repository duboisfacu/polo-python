#Extraer año y película directamente del diccionario

dictMovies = {
    "2010":"The King's Speech",
    "2011":"The Artist",
    "2012":"Argo",
    "2013":"12 Years a Slave",
    "2014":"Birdman",
    "2015":"Spotlight",
    "2016":"Moonlight",    
    "2017":"The Shape of Water",
    "2018":"Green Book",
    "2019":"Parasite",
    "2020":"Nomadland",
}

for anio, pelicula in dictMovies.items():
    print(f"Y el oscar a mejor película del año {anio} es para... {pelicula}!")