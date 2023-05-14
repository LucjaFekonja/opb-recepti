import pandas as pd
from pandas import DataFrame

from Database import Repo
from model import *
from typing import Dict
from re import sub
import dataclasses



# Vse kar delamo z bazo se nahaja v razredu Repo.
repo = Repo()



def uvozi_recepte(pot):
    """
    Uvozimo csv z recepti v v bazo.
    Pri tem predpostavljamo, da imamo tabele že ustvarjene. 
    Vsako vrstico posebaj še obdelamo, da v bazi dobimo željeno strukturo. Uporabimo
    razred Repo za klic funkcij za uvoz v bazo.
    """

    df = pd.read_csv(pot)

    
    for row in df.itertuples():
        # row je seznam posamezne vrstice, ki se začne z indexom 1
        if row[4] != 'mins' or row[4] != 'hr' or row[4] != 'hrs':
            print(row)
        elif row[4] == 'hr':
            row[3] = 60 * int(row[3])
        else:
            continue

        if row[6] != 'mins' or row[6] != 'hr' or row[6] != 'hrs':
            print(row)
        elif row[6] == 'hr':
            row[5] = 60 * int(row[5])
        else:
            continue
        
        repo.dodaj_recept(
            Recept(
                ime=row[2],
                st_porcij=row[7],
                cas_priprave=row[3],
                cas_kuhanja=row[5] 
            )
        )

def uvozi_kategorije(pot):
    df = pd.read_csv(pot)


    for row in df.itertuples():

        repo.dodaj_kategorijo(

            Kategorija(
            id_recepta = row[1],
            kategorija = row[2]
            )
        )

def uvozi_sestavine_receptov(pot):
    df = pd.read_csv(pot, sep=";",skiprows=[0], encoding="Windows-1250")


    for row in df.itertuples():
        locena_vrstica = row.split(',')

        repo.dodaj_sestavino(

            SestavineReceptov(
            id = locena_vrstica[0],
            ime = locena_vrstica[1],
            )
        )


def uvozi_postopke(pot):
    df = pd.read_csv(pot, sep=";",skiprows=[0], encoding="Windows-1250")

    #ne smemo lociti na vejice, saj se pojavijo tudi v povedih!
    for row in df.itertuples():
        locena_vrstica = row.split(',', 2)

        repo.dodaj_postopek(

            Postopek(
            id = locena_vrstica[0],
            st_koraka = locena_vrstica[1],
            postopek = locena_vrstica[2],
            )
        )

def uvozi_csv(pot, ime):
    """
    Uvozimo csv v bazo brez večjih posegov v podatke.
    Ustvarimo pandasov DataFrame ter nato z generično metodo ustvarimo ter
    napolnimo tabelo v postgresql bazi.
    """
    df = pd.read_csv(pot, sep=";",skiprows=[0], encoding="Windows-1250")

    # Zamenjamo pomišljaje z prazno vrednostjo
    df.replace(to_replace="-", value="", inplace=True)

    # Naredimo tabelo z dodatnim serial primary key stolpcem
    repo.df_to_sql_create(df, ime, add_serial=True, use_camel_case=True)

    # uvozimo podatke v to isto tabelo
    repo.df_to_sql_insert(df, ime, use_camel_case=True)




# Primeri uporabe. Zakomentiraj določene vrstice, če jih ne želiš izvajat!
    

##pot = "obdelani-podatki/recepti.csv"
##pot = "obdelani-podatki/kategorije.csv"
##pot = "obelani-podatki/sestavine-receptov.csv"
##pot = "obelani_podatki/postopki.csv"

# Uvozi csv s cenami izdelkov v ločene (in povezane) entitete
# Tabele morajo biti prej ustvarjene, da zadeva deluje

##uvozi_recepte(pot)
##uvozi_kategorije(pot)
##uvozi_sestavine_receptov(pot)
##uvozi_postopke(pot)

# Uvozi csv s cenami, le da tokar uvozi le eno tabelo, ki jo
# predhodno še ustvari, če ne obstaja.

#uvozi_csv(pot, "NovaTabela")



## A TO SPLOH RABVA? NE RAZUMM CIST KAJ DELA SPODNJA STVAR? USTVARJA NOVE KATEGORIJE?
# S pomočjo generične metode dobimo seznam izdelkov in kategorij
# Privzete nastavi

# Dobimo prvih 100 izdelkov
recepti = repo.dobi_gen(Recept, skip=0, take=100)

t = repo.dobi_gen(ReceptPosSes)

# Dobimo prvih 10 kategorij
kategorije = repo.dobi_gen(Kategorija)

# Dodamo novo kategorijo

nova_kategorija = Kategorija(
    oznaka="Nova kategorija"
)

repo.dodaj_gen(nova_kategorija)

# vrednost nova_kategorija.id je sedaj določen na podlagi
# serial vrednosti iz baze in jo lahko uporabimo naprej.


# Dodamo nov recept v to kategorijo
novi_recept = Recept(
    ime = 'Novi recept',
    kategorija=nova_kategorija.id
)
repo.dodaj_gen(novi_recept)


# Dobimo recept z idjem 832
recept = repo.dobi_gen_id(Recept, 832)

# izdelku spremenimo ime in ga posodobimo v bazi
recept.ime += " spremenjeno ime"
repo.posodobi_gen(recept)



# spremenimo seznam receptov in ga shranimo v bazo

for i in recepti:
    i.ime = f'({i.ime})'

repo.posodobi_list_gen(recepti)
