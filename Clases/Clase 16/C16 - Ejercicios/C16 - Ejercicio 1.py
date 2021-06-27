dictMovies = {
    "1990":"Dances with Wolves",  
    "1991":"The Silence of the Lambs",     
    "1992":"Unforgiven",     
    "1993":"Schindler's list",      
    "1994":"Forrest Gump",  
    "1995":"Braveheart",   
    "1996":"The English Patient",  
    "1997":"Titanic",      
    "1998":"Shakespeare in Love",      
    "1999":"American Beauty",    
    "2000":"Gladiator",   
    "2001":"A Beautiful Mind",    
    "2002":"Chicago",    
    "2003":"The Lord of the Rings: The Return of the King",    
    "2004":"Million Dollar Baby",   
    "2005":"Crash",
    "2006":"The Departed",
    "2007":"No Country for Old Men",
    "2008":"Slumdog Millionaire",
    "2009":"The Hurt Locker",
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

age = input("Elige un año entre el 1990 y el 2020: ")

while True:
    if age in dictMovies:
        print("--------------------------------------------------------------------------")
        print("La película ganadora del oscar en el año",age, "fue", dictMovies.get(age))
        print("--------------------------------------------------------------------------")
        age = input("¿Querés saber la ganadora de otro año? Escribí un año nuevamente: ")
    else:
        print("¡AÑO NO DISPONIBLE!")
        age = input("Vuelve a escribir el año de manera correcta: ")