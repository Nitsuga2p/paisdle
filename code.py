import streamlit as st
print("Bienvenido a paisdle 🌎")
import random
import unicodedata
from colorama import Fore, Style, init
init()
países=["Chile",
        "Argentina",
        "Perú",
        "Bolivia",
        "Brasil",
        "Ecuador","Paraguay",
        "Colombia",
        "Venezuela",
        "Surinam",
        "Guyana",
        "Uruguay",
        "Panamá",
        "Cuba",
        "Costa Rica",
        "Nicaragua",
        "Honduras",
        "El Salvador",
        "Guatemala",
        "Belice",
        "Jamaica",
        "Bahamas",
        "México",
        "Estados Unidos",
        "Canadá",
        "Albania",
        "Alemania",
        "Andorra",
        "Armenia",
        "Austria",
        "Azerbaiyán",
        "Bélgica",
        "Bielorrusia",
        "Bosnia y Herzegovina",
        "Bulgaria",
        "Chequia",
        "Chipre",
        "Ciudad del Vaticano",
        "Croacia",
        "Dinamarca",
        "Eslovaquia",
        "Eslovenia",
        "España",
        "Estonia",
        "Finlandia",
        "Francia",
        "Georgia"
        ]
 
print(países)
respuesta=[]
p=random.choice(países)
 
chi=[
    "Español",
    "700.000km2,800.000km2",
    "Color bandera: Blanco",
    "Color bandera: Rojo",
    "Color bandera: Azul",
    "10millones-20millones",
    "Laico",
    "Extrema Derecha"
    ]
 
arg=[
    "Español",
     "+1.000.000km2",
     "Color bandera: Celeste",
     "Color bandera: Blanco",
     "40millones-50millones",
     "Laico",
     "Extrema derecha"
     ]
 
per=[
    "Español",
    "+1.000.000km2",
    "Color bandera: Rojo",
    "Color bandera: Blanco",
    "30millones-40millones",
    "Laico",
    "Centroizquierda"
    ]
 
bol=[
    "Español",
    "+1.000.000km2",
    "Color bandera: Rojo",
    "Color bandera: Amarillo",
    "Color bandera: Verde",
    "10millones-20millones",
    "Laico",
    "Centroderecha"
    ]
 
bra=[
    "Portugués",
    "+1.000.000km2",
    "Color bandera: Verde",
    "Color bandera: Amarillo",
    "Color bandera: Azul",
    "+100 millones",
    "Laico",
    "Centroizquierda"
    ]
 
ecu=[
    "Español",
    "200.000km2-300.000km2",
    "Color bandera: Rojo",
    "Color bandera: Amarillo",
    "Color bandera: Azul",
    "10millones-20millones",
    "Laico",
    "Centroderecha"
    ]
 
col=[
    "Español",
    "+1.000.000km2",
    "Color bandera: Amarillo",
    "Color bandera: Azul",
    "Color bandera: Rojo",
    "50millones-60millones",
    "Laico",
    "Izquierda"
    ]
 
pry=[
    "Español",
    "400.000km2-500.000km2",
    "Color bandera: Rojo",
    "Color bandera: Blanco",
    "Color bandera: Azul",
    "1millón-10millones",
    "Laico",
    "Derecha"
    ]
 
vzl=[
    "Español",
    "900.000km2-1.000.000km2",
    "Color bandera: Amarillo",
    "Color bandera: Azul",
    "Color bandera: Rojo",
    "20millones-30millones",
    "Laico",
    "Izquierda"
    ]
 
sur=[
    "Neerlandés",
    "100.000km2-200.000km2",
    "Color bandera: Verde",
    "Color bandera: Rojo",
    "Color bandera: Amarillo",
    "Color bandera: Blanco",
    "<1millón",
    "Laico",
    "Centroizquierda"
    ]
 
guy=[
    "Inglés",
    "200.000kim2-300.000km2",
    "Color bandera: Rojo",
    "Color bandera: Amarillo",
    "Color bandera: Verde"
    "<1millón",
    "Laico",
    "Centroizquierda"
    ]
 
ury=[
    "Español",
    "100.000km2-200.000km2",
    "Color bandera: Azul",
    "Color bandera: Blanco",
    "1millón-10millones",
    "Laico",
    "Centroizquierda"
    ]
 
pan=[
    "Español",
    "<100.000km2",
    "Color bandera: Azul",
    "Color bandera: Rojo"
    "Color bandera: Blanco",
    "1millón-10millones",
    "Laico",
    "Centroderecha"
    ]
 
cub=[
    "Español",
    "100.000km2-200.000km2",
    "Color bandera: Rojo",
    "Color bandera: Blanco",
    "Color bandera: Azul",
    "1millón-10millones",
    "Laico",
    "Extrema izquierda"
    ]
 
crc=[
    "Español",
    "<100.000km2",
    "Color bandera: Azul",
    "Color bandera: Rojo",
    "Color bandera: Blanco",
    "1millón-10millones",
    "Catolicismo",
    "Derecha"
    ]
 
nca=[
    "Español",
    "100.000km2-200.000km2",
    "Color bandera: Azul",
    "Color bandera: Blanco",
    "1millón-10millones",
    "Laico",
    "Izquierda"
    ]
 
hon=[
    "Español",
    "100.000km2-200.000km2",
    "Color bandera: Azul",
    "Color bandera: Blanco",
    "10millones-20millones",
    "Laico",
    "Derecha"
    ]
 
esa=[
    "Español",
    "<100.000km2",
    "Color bandera: Azul",
    "Color bandera: Blanco",
    "1millón-10millones",
    "Laico",
    "Extrema derecha"
    ]
 
gua=[
    "Español",
    "100.000km2-200.000km2",
    "Color bandera: Azul",
    "Color bandera: Blanco",
    "10millones-20millones",
    "Laico",
    "Centroizquierda"
    ]
 
blz=[
    "Inglés",
    "<100.000km2",
    "Color bandera: Azul",
    "Color bandera: Rojo",
    "<1millón",
    "Laico",
    "Centroizquieda"
    ]
 
jam=[
    "Inglés",
    "<100.000km2",
    "Color bandera: Verde",
    "Color bandera: Negro"
    "Color bandera: Amarillo",
    "1millón-10millones",
    "Laico",
    "Centroderecha"
    ]
 
bah=[
    "Inglés",
    "<100.000km2",
    "Color bandera: Azul",
    "Color bandera: Amarillo",
    "Color bandera: Negro",
    "<1millón",
    "Laico",
    "Centroizquierda"
    ]
 
mex=[
    "Español",
    "+1.000.000km2",
    "Color bandera: Verde",
    "Color bandera: Rojo",
    "Color bandera: Blanco",
    "+100 millones",
    "Laico",
    "Izquierda"
    ]
 
usa=[
    "Inglés",
    "+1.000.000km2",
    "Color bandera: Azul",
    "Color bandera: Rojo",
    "Color bandera: Blanco",
    "+100 millones",
    "Laico",
    "Derecha"
    ]
 
can=[
    "Inglés",
    "Francés",
    "+1.000.000km2",
    "Color bandera: Blanco",
    "Color bandera: Rojo",
    "40millones-50millones",
    "Laico",
    "Centroizquierda"
    ]
 
alb=[
    "Albanés",
    "<100.000km2",
    "Color bandera: Rojo",
    "Color bandera: Negro",
    "1millón-10millones",
    "Laico",
    "Centroizquierda"
    ]
 
ger=[
    "Alemán",
    "300.000km2-400.000km2",
    "Color bandera: Rojo",
    "Color bandera: Amarillo",
    "Color bandera: Negro",
    "80millones-90millones",
    "Laico",
    "Centroderecha"
    ]
 
adr=[
    "Catalán",
    "<100.000km2",
    "Color bandera: Amarillo",
    "Color bandera: Rojo",
    "Color bandera: Azul",
    "<1millón",
    "Laico",
    "Centroderecha"
    ]
 
arm=[
    "Armenio",
    "<100.000km2",
    "Color bandera: Rojo",
    "Color bandera: Azul",
    "Color bandera: Amarillo",
    "1millón-10millones",
    "Cristianismo",
    "Centro"
    ]
 
aut=[
    "Alemán",
    "<100.000km2",
    "Color bandera: Rojo",
    "Color bandera: Blanco",
    "1millón-10millones",
    "Laico",
    "Centroizquierda-Centroderecha"
    ]
 
aze=[
    "Azerí",
    "<100.000km2",
    "Color bandera: Azul",
    "Color bandera: Verde",
    "Color bandera: Rojo",
    "10millones-20millones",
    "Laico",
    "Autoritarismo"
    ]
 
bel=[
    "Alemán",
    "Francés",
    "Neerlandés",
    "<100.000km2",
    "Color bandera: Negro",
    "Color bandera: Rojo",
    "Color bandera: Amarillo",
    "10millones-20millones",
    "Laico",
    "Centroderecha"
    ]
 
blr=[
    "Bielorruso",
    "Ruso",
    "200.000km2-300.00km2",
    "Color bandera: Rojo",
    "Color bandera: Verde",
    "1millón-10millones",
    "Laico",
    "Autoritarismo"
    ]
 
bih=[
    "Bosnio",
    "Serbio",
    "Croata",
    "<100.000km2",
    "Color bandera: Amarillo",
    "Color bandera: Azul",
    "Color bandera: Blanco",
    "1millón-10millones",
    "Laico",
    "Centroderecha"
    ]
 
bul=[
    "Búlgaro",
    "100.000km2-200.000km2",
    "Color bandera: Blanco",
    "Color bandera: Verde",
    "Color bandera: Rojo",
    "1millón-10millones",
    "Laico",
    "Centroizquierda"
    ]
 
cze=[
    "Checo",
    "<100.000km2",
    "Color bandera: Azul",
    "Color bandera: Rojo",
    "Color bandera: Blanco",
    "10millones-20millones",
    "Laico",
    "Derecha"
    ]
 
cyp=[
    "Griego",
    "Turco",
    "<100.000km2",
    "Color bandera: Blanco",
    "Color bandera: Naranjo",
    "<1millón",
    "Laico",
    "Centroderecha"
    ]
 
v=[
    "Italiano",
    "Latín",
    "<100.000km2",
    "Color bandera: Blanco",
    "Color bandera: Amarillo",
    "<1millón",
    "Catolicismo",
    "Monarquía absoluta y teocrática"
    ]
 
cro=[
    "Croata",
    "<100.000km2",
    "Color bandera: Azul",
    "Color bandera: Rojo",
    "Color bandera: Blanco",
    "1millón-10millones",
    "Laico",
    "Centroderecha"
    ]
 
dk=[
    "Danés",
    "<100.000km2",
    "Color bandera: Rojo",
    "Color bandera: Blanco",
    "1millón-10millones",
    "Luteranismo",
    "Centroderecha"
    ]
 
svk=[
    "Eslovaco",
    "<100.000km2",
    "Color bandera: Blanco",
    "Color bandera: Rojo",
    "Color bandera: Rojo",
    "1millón-10millones",
    "Laico",
    "Coalición izquierda-extrema derecha"
    ]
 
slo=[
    "Esloveno",
    "<100.000km2",
    "Color bandera: Blanco",
    "Color bandera: Azul",
    "Color bandera: Rojo",
    "1millón-10millones",
    "Laico",
    "Centroizquierda"
    ]
 
esp=[
    "Español",
    "500.000km2-600.000km2",
    "Color bandera: Amarillo",
    "Color bandera: Rojo",
    "40millones-50millones",
    "Laico",
    "Centroizquierda"
    ]
 
est=[
    "Estonio",
    "<100.000km2",
    "Color bandera: Azul",
    "Color bandera: Blanco",
    "Color bandera: Negro",
    "1millón-10millones",
    "Laico",
    "Centroderecha"
    ]
 
fin=[
    "Fines",
    "Sueco",
    "300.000km2-400.000km2",
    "Color bandera: Blanco",
    "Color bandera: Azul",
    "1millón-10millones",
    "Laico",
    "Centroderecha"
    ]
 
fra=[
    "Francés",
    "600.000km2-700.000km2",
    "Color bandera: Rojo",
    "Color bandera: Blanco",
    "Color bandera: Azul",
    "60millones-70millones",
    "Laico",
    "Centroderecha"
    ]
 
geo=[
    "Georgiano",
    "<100.000km2",
    "Color bandera: Blanco",
    "Color bandera: Rojo",
    "1millón-10millones",
    "Laico",
    "Centroderecha"
    ]
 
 
listas_países={
    "Chile": chi,
    "Argentina": arg,
    "Perú": per,
    "Bolivia": bol,
    "Brasil": bra,
    "Ecuador": ecu,
    "Paraguay": pry,
    "Colombia":col,
    "Surinam":sur,
    "Guyana":guy,
    "Uruguay":ury,
    "Panamá":pan,
    "Cuba":cub,
    "Costa Rica":crc,
    "Nicaragua":nca,
    "Honduras":hon,
    "El Salvador":esa,
    "Guatemala":gua,
    "Belice":blz,
    "Jamaica":jam,
    "Bahamas":bah,
    "México":mex,
    "Estados Unidos":usa,
    "Canadá":can,
    "Albania":alb,
    "Alemania":ger,
    "Andorra":adr,
    "Armenia":arm,
    "Austria":aut,
    "Azerbaiyán":aze,
    "Bélgica":bel,
    "Bielorrusia":blr,
    "Bosnia y Herzegovina":bih,
    "Bulgaria":bul,
    "Chequia":cze,
    "Chipre":cyp,
    "Ciudad del Vaticano":v,
    "Croacia":cro,
    "Dinamarca":dk,
    "Eslovaquia":svk,
    "Eslovenia":slo,
    "España":esp,
    "Estonia":est,
    "Finlandia":fin,
    "Francia":fra,
    "Georgia":geo
    }

 
    
a=str(input("Intente adivinar el país. Ingrese un país de la lista (recuerde utilizar una buena ortografía): "))
respuesta=listas_países[p]
intentos=1
while a!=p:
    if a in listas_países:
        l=listas_países[a]
        print(l)
        i1=[]
        m1=[]
        for x in(l):
            if x in(respuesta):
                i1.append(x)
            elif x not in(respuesta):
                m1.append(x)
        tick="\U00002705"
        cruz="\U0000274C"
        i1.append(tick)
        m1.append(cruz)
        for elemento in(i1):
            print(Fore.GREEN + elemento)
        for elemento in(m1):
            print(Fore.RED + elemento)
        a=str(input(Fore.WHITE + "Inténtelo de nuevo: "))
        intentos=intentos+1

 
if a==p:
    print(respuesta)
    print(Fore.GREEN + "Felicidades, lo adivinaste")
    print(Fore.YELLOW + "Te tomó",intentos,"intentos")

 
if intentos==1:
    pts=1000
elif intentos==2:
    pts=850
elif intentos==3:
    pts=750
elif intentos==4:
    pts=650
elif intentos==5:
    pts=500
elif 5<intentos<10:
    pts=300
else:
    pts=100

print("Puntuación:",pts,"puntos")
