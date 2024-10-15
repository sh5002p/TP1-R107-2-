nb_minute = int(input("Entrez le nombre de minutes écoulé :" ))
nb_jour = nb_minute / 1440
nb_heures = nb_minute % 1440
nb_minutes = nb_minute % 60

print("le nombre de jour {:.0f} le nombre d heure {} le nombre de minutes {}, depuis {} minutes".format(nb_jour, nb_heures, nb_minutes, nb_minute))
