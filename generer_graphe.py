import matplotlib.pyplot as plt

def syracuse_vectoriel(x, y):
    history = []
    # On monte à 30 étapes pour avoir un beau graphique sans surcharger
    while (x, y) not in history and len(history) < 30:
        history.append((x, y))
        if x % 2 == 0 or y % 2 == 0:
            x = x // 2
            y = y // 2
        else:
            x = 3 * x + 1
            y = 3 * y + 1
    history.append((x, y))
    return history

# Génération des données
trajectoire = syracuse_vectoriel(3, 5)

# Séparation des coordonnées X et Y pour le graphique
liste_x = [pt[0] for pt in trajectoire]
liste_y = [pt[1] for pt in trajectoire]

# Création du graphique géométrique
plt.figure(figsize=(8, 6))
plt.plot(liste_x, liste_y, marker='o', c='b', linestyle='-', linewidth=2)
plt.title("Trajectoire géométrique de Syracuse Vectoriel (3, 5)")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.grid(True)
plt.show()
