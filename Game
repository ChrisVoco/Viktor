import random

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


def quiz(): #lisa juurde
    Health = 100
    score = 0

    max_punkte = len(kysimused)

    random.shuffle(kysimused)

    for kysimus, Õige_vastus in kysimused:
        Kasutaja_vastus = input(str(kysimus))

        if Kasutaja_vastus.strip().lower() == Õige_vastus.lower():
            print('Õige Vastus!', "(", Õige_vastus, ")")
            score += 1
        else:
            print("Vale Vastus! Õige Vastus Oli: ", "(", Õige_vastus, ")")
            Health -= 25

        print(f"Hetke skoor: {score}, Hetke tervis: {Health}%\n")

        if Health <= 0:
            break
    
    # lõpptulemus
    if Health > 0:
        print(f"Quiz on lõppenud! Sinu lõpp-skoor on {score}/{max_punkte} ja tervis {Health}%.")
    else:
        print(f"Quiz lõppes enneaegselt tänu su surmale. Sinu lõpp-skoor oli {score}/{max_punkte}.")

quiz()
