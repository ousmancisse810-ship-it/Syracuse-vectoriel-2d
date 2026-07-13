def syracuse_vectoriel(x, y, max_iter=10000):
    cycle = {(1, 1), (2, 2), (4, 4)}
    deja_vus = set()

    for _ in range(max_iter):

        # Si on atteint le cycle recherché
        if (x, y) in cycle:
            return True

        # Boucle inattendue
        if (x, y) in deja_vus:
            return False

        deja_vus.add((x, y))

        # Règle de Syracuse vectorielle
        if x % 2 == 0 or y % 2 == 0:
            if x % 2 == 0:
                x //= 2
            if y % 2 == 0:
                y //= 2
        else:
            x = 3 * x + 1
            y = 3 * y + 1

    return False


# Test de 1 000 000 de couples
contre_exemples = []

for x in range(1, 1001):
    for y in range(1, 1001):
        if not syracuse_vectoriel(x, y):
            contre_exemples.append((x, y))
            print("Contre-exemple trouvé :", (x, y))
            break
    if contre_exemples:
        break

if len(contre_exemples) == 0:
    print("✅ Les 1 000 000 couples convergent vers le cycle (1,1)-(4,4)-(2,2).")
else:
    print("❌ Au moins un contre-exemple a été trouvé :", contre_exemples[0])
