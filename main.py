def linear_search(liste, ziel):
    for index, wert in enumerate(liste):
        if wert == ziel:
            return index
    return -1


if __name__ == '__main__':
    zahlen = [3, 8, 2, 7, 5]
    ziel = 7
    resultat = linear_search(zahlen, ziel)
    print(f'Index des gesuchten Elements: {resultat}')
