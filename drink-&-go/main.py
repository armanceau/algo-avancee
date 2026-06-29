pieces_possibles = [100, 50, 20, 5, 2, 1]

def compute(pieces_possibles, reste_a_rendre) -> tuple[int, list[int]]:
    pieces_possibles.sort(reverse=True) # EN cas d'imput non trié
    rep = []
    for piece in pieces_possibles:
        nb = reste_a_rendre // piece
        rep.append(nb)
        reste_a_rendre %= piece

    return rep, reste_a_rendre
    
    #print(f"pieces_possibles: {pieces_possibles}, reste_a_rendre: {reste_a_rendre}")
    
    
def main() -> None:
    print(compute(pieces_possibles, 17))


if __name__ == "__main__":
    main()



