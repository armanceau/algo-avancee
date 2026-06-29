# algo-avancee

Rendu de monnaie d'un distributeur
Vous travaillez pour Drink&Go, une entreprise spécialisée dans la conception de distributeurs automatiques de
boissons installés dans les gares, les universités et les entreprises.
Depuis plusieurs semaines, le service client reçoit des plaintes :
« Le distributeur m’a rendu trop de petites pièces. »
« Le rendu de monnaie est lent. »
« La machine semble parfois incapable de rendre correctement la monnaie. »
La direction technique souhaite donc ré-écrire le programme embarqué dans ses distributeurs.
Vous devez écrire une fonction en Python qui détermine comment rendre une somme donnée avec le plus petit
nombre de pièces possible.
La fonction reçoit :
la liste des pièces disponibles ;
le montant restant à rendre, exprimé en centimes.
Elle doit retourner :
le nombre total de pièces utilisées ;
le détail des pièces choisies.
Votre programme doit être simple, rapide et adapté à des montants allant jusqu'à 2 euro. L'automate a un CPU à très
faible cadence (10 MHz) et à la RAM très limitée (512K).
Signature demandée
def compute(pieces_possibles, reste_a_rendre) -> tuple[int, list[int]]:
pass
Exemple de paramètres :
pieces_possibles = [100, 50, 20, 10, 5, 2, 1]
reste_a_rendre = 17
Les valeurs sont exprimées en centimes.
Exemple attendu
Un client achète une boisson à 0,83 € et insère une pièce de 1 €.
Le montant à rendre est donc :
1,00 € - 0,83 € = 0,17 €
Le programme doit calculer le rendu de monnaie optimal.
Sortie attendue :
Rendu de monnaie pour le client : 0,17 €
Nombre total de pièces : 3
Détail des pièces : 10, 5, 2
La solution optimale est donc :
10 cts + 5 cts + 2 cts = 17

-> Trier la liste de pièce à rendre pour mettre [max, min]
-> Boucle sur les pièces
-> pour chaque pièce on teste si on peut diviser le reste à rendre : 
    - Si oui -> alors on stock le reste de la division et on relance la boucle jusqu'a obtenir 0 
    - Si non -> on passe à l'élement suivant et on re teste

Cas concret:
    on donne la liste suivante: [100,50,10,5,2,1]
    un article coute 83 et on rentre 100
    1 Etape Calcule du reste a rendre
    100 - 83 = 17

    2 Etape Boucle de Calcule de piece
    2.1 
    17%100 = 17 # pas possible de mettre une piece de 100 passons a la piece inférieur
    17%50 = 17 # meme cas ici on passe a la piece inférieur
    17%10 = 7 # modulo possible on passe a la division entière pour voir le nombre de piece max on peux sortir

    17//10 = 1 # on stocke que l'on peut mettre 1 piece de 10 [10] on passe ensuite à la piece suivante (ne pas oublier de soustraire le 10 retirer soit 17-10=7)
    
    7%5 = 2 # modulo possible on passe a la division entière pour voir le nombre de piece max on peux sortir
    7//5 = 1 # on stocke que l'on peut mettre 1 piece de 5 [10,5] on passe ensuite à la piece suivante (ne pas oublier de soustraire le 5 retirer soit 7-5=2)

    2%2 = 0 # modulo possible on passe a la division entière pour voir le nombre de piece max on peux sortir (d'ailleur modulo donne zero donc on peu garder en mémoire que se sera la dernier étape des "piece")
    2//2 = 1 # on stocke que l'on peut mettre 1 piece de 2 [10,5,2]

    3 Etape Affichage du resultat
    On a terminer par rendre 1 piece de 10 une de 5 et une de 2

Cas concret 2:
    on donne la liste suivante: [4,3,1]
    un article coute 6 et on a 12 
