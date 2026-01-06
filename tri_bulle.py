#!/usr/bin/env python3

def tri_bulle(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] < liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

# Exemple d'utilisation
ma_liste = [64, 34, 25, 12, 22, 11, 90]
print("Liste non triée:", ma_liste)
ma_liste_triee = tri_bulle(ma_liste)
print("Liste triée:", ma_liste_triee)
