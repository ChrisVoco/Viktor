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

    Mängja = input("Siseta mängja nimi: ")

    max_punkte = len(kysimused) # vaatab palju küsimuse on

    random.shuffle(kysimused) # segab küsimused

    for kysimus, Õige_vastus in kysimused: 
        Kasutaja_vastus = input(str(kysimus)) # saad vasdata küsimusele

        if Kasutaja_vastus.strip().lower() == Õige_vastus.lower(): # kontrollib kas vastus on õige või mitte
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
        print(f"Quiz on lõppenud! Sinu lõpp-skoor on {score}/{max_punkte} ja tervis {Health}%.\n") # väljastab skoori/max skoorist ja elude %
    else:
        print(f"Quiz lõppes enneaegselt tänu su surmale. Sinu lõpp-skoor oli {score}/{max_punkte}.\n") # väljastab Skoori/max skoorist ainult, siis kui surid enneaegselt

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
