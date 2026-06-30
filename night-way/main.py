risque_min = {
    "Bar Central": 0,
    "Rue Victor Hugo": float('inf'),
    "Rue des Lilas": float('inf'),
    "Place République": float('inf'),
    "Domicile": float('inf'),
}

graphe = {
    "Bar Central": {"Rue Victor Hugo": 20, "Rue des Lilas": 50},
    "Rue Victor Hugo": { "Place République": 30, "Domicile": 40 },
    "Rue des Lilas": { "Place République": 10 },
    "Place République": { "Domicile": 15 },
}

venant_de = {
    "Bar Central": None,
    "Rue Victor Hugo": None,
    "Rue des Lilas": None,
    "Place République": None,
    "Domicile": None,
}


def compute():
    for cle, valeur in graphe.items():
        for voisin, score in valeur.items():
            nouveau_score = risque_min[cle] + score
            if nouveau_score < risque_min[voisin]:
                risque_min[voisin] = nouveau_score
                venant_de[voisin] = cle

    actuelle = "Domicile"
    chemin = []
    while actuelle is not None:
        chemin.append(actuelle)
        actuelle = venant_de[actuelle]
    chemin.reverse()

    return risque_min["Domicile"], chemin


def main() -> None:
    score, chemin = compute()
    print(score, chemin)


if __name__ == "__main__":
    main()