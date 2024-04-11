import random

def hangman():
    ord_lista = ["kakel", "tofflor", "hemlängtan", "frihet", "nycklar", "grotta", "gaffel", "stuga", "potatis"]
    ord = random.choice(ord_lista)
    fel = 0
    gissade_bokstäver = []
    rätt = False

    print("Välkommen till hänga gubbe!")
    print("Gissa på ordet:")
    print("_ " * len(ord))
    while fel < 6 and not rätt:
        bokstav = input("Gissa på en bokstav: ")
        if bokstav in gissade_bokstäver:
            print("Du har redan gissat på bokstaven", bokstav)
        elif bokstav in ord:
            print("Bokstaven finns i ordet!")
            gissade_bokstäver.append(bokstav)
        else:
            fel += 1
            print("Fel gissat! Du har", 6 - fel, "försök kvar.")
            gissade_bokstäver.append(bokstav)

        if all(bokstav in gissade_bokstäver for bokstav in ord):
            print(f"Grattis! Du har gissat rätt på ordet", ord)
            rätt = True

        print("Gissade bokstäver:", gissade_bokstäver)
        print("_ " * len(ord))
    print("Spelet är tyvärr slut. Ordet var:", ord)    
def main():
    hangman()

if __name__ == '__main__':
    main()