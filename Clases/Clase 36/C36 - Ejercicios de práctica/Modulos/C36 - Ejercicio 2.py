from modulos.ClaseNerd import Nerd
import datetime as dt

fechaNacimiento = dt.date(1992, 4, 20)

ClaseNerd = Nerd("ramiro", fechaNacimiento)

ClaseNerd.programar()
ClaseNerd.presentarse()
