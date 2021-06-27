#contador

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
cont = 0

for x in dictMovies.items():
    cont += 1
    print(f"{cont}) {x[1]} ({x[0]})") 