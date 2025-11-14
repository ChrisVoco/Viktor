from jaro import jaro_winkler_metric
from easygui import *
import random
import json
import os

# Loo tühi list ja set unikaalsuse jaoks
kysimused = []
seen = set()

# Loe failiread
with open("fail.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # eemalda tühikud ja \n
        if not line:
            continue  # tühja rea puhul jätka

        # Muuda rida tegelikuks tupliks
        tup = eval(line)  

        kysimused.append(tup)


def quiz():
    Health = 100 # palju elusi on
    score = 0 # algne skoor

    Mängja = enterbox("Siseta mängja nimi: ")

    print("\n")

    max_punkte = len(kysimused) # vaatab palju küsimuse on

    random.shuffle(kysimused) # segab küsimused

    for kysimus, Õige_vastus in kysimused: 
        Kasutaja_vastus = enterbox(str(kysimus)) # saad vasdata küsimusele
        
        tulemus = jaro_winkler_metric(Õige_vastus.lower(), Kasutaja_vastus.lower())
        
        if tulemus >= 0.95:   # kui vastus on vähemalt 90% sarnane
            print(f"Õige Vastus{Õige_vastus}")
            score += 1

        elif Kasutaja_vastus.strip().lower() == Õige_vastus.lower():
            print('Õige Vastus!', "(", Õige_vastus, ")")
            score += 1
        else:
            print("Vale Vastus! Õige Vastus Oli: ", "(", Õige_vastus, ")")
            Health -= 25

        print(f"Hetke skoor: {score}, Hetke tervis: {Health}%\n") # väljastab iga kord hetke skoori, elu ja teeb uue rea

        if Health <= 0: # kui elud otsa saavad lõpetab koodi
            break
    
    # lõpptulemus
    if Health > 0:
        msgbox(f"Quiz on lõppenud! Sinu lõpp-skoor on {score}/{max_punkte} ja tervis {Health}%.\n", "Lõpp") # väljastab skoori/max skoorist ja elude %
    else:
        msgbox(f"Quiz lõppes enneaegselt tänu su surmale. Sinu lõpp-skoor oli {score}/{max_punkte}.\n", "Lõpp") # väljastab Skoori/max skoorist ainult, siis kui surid enneaegselt

    filename = "data.json"

    if os.path.exists(filename): 
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f) # vaatab kas fail on olemas
    else:
        data = [] # kui faili polnud, siis alustab tühjast listist

    # Lisab uue mängija tulemuse
    user_data = {
        "Mängja": Mängja,
        "health": Health,
        "score": score
    }
    data.append(user_data) # lisab data.json uue user_data

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Andmed salvestatud faili data.json")

quiz() # paneb mängu tööle
