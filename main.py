#Import random to make a random pokemon, string to camelcase input, and list for the names, types, weight, and height of all gen 1 pokemon
import random
import string
pNames = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
pType1 = ["grass","grass","grass","fire","fire","fire","water","water","water","bug","bug","bug","bug","bug","bug","normal","normal","normal","normal","normal","normal","normal","poison","poison","electric","electric","ground","ground","poison","poison","poison","poison","poison","poison","fairy","fairy","fire","fire","normal","normal","poison","poison","grass","grass","grass","bug","bug","bug","bug","ground","ground","normal","normal","water","water","fighting","fighting","fire","fire","water","water","water","psychic","psychic","psychic","fighting","fighting","fighting","grass","grass","grass","water","water","rock","rock","rock","fire","fire","water","water","electric","electric","normal","normal","normal","water","water","poison","poison","water","water","ghost","ghost","ghost","rock","psychic","psychic","water","water","electric","electric","grass","grass","ground","ground","fighting","fighting","normal","poison","poison","ground","ground","normal","grass","normal","water","water","water","water","water","water","psychic","bug","ice","electric","fire","bug","normal","water","water","water","normal","normal","water","electric","fire","normal","rock","rock","rock","rock","rock","normal","ice","electric","fire","dragon","dragon","dragon","psychic","psychic"]
pType2 = ["poison","poison","poison","single","single","flying","single","single","single","single","single","flying","poison", "poison","poison","flying","flying","flying","single","single", "flying","flying","single","single","single","single","single","single","single","single","ground","single","single","ground","single","single","single","single","fairy", "fairy", "flying","flying","poison","poison","poison","grass","grass","poison","poison","single","single","single","single","single","single","single","single","single","single","single","single","fighting","single","single","single","single","single","single","poison","poison","poison","poison","poison","ground","ground","ground","single","single","psychic","psychic","steel","steel","flying","flying","flying","single","ice","single","single","single","ice","poison","poison","poison","ground","single","single","single","single","single","single","psychic","psychic","single","single","single","single","single","single","single","rock","rock","single","single","single","single","single","single","single","single","psychic","fairy","flying","psychic","single","single","single","single","single","flying","ice","single","single","single","single","single","single","water","water","water","water","flying","single","flying","flying","flying","single","single","flying","single","single"]
pWeight = ["6.9","13","100","8.5","19","90.5","9","22.5","85.5","2.9","9.9","32","3.2","10","29.5","1.8","30","39.5","3.5","18.5","2","38","6.9","65","6","30","12","29.5","7","20","60","9","19.5","62","7.5","40","9.9","19.9","5.5","12","7.5","55","5.4","8.6","18.6","5.4","29.5","30","12.5","0.8","33.3","4.2","32","19.6","76.6","28","32","19","155","12.4","20","54","19.5","56.5","48","19.5","70.5","130","4","6.4","15.5","45.5","55","20","105","300","30","95","36","78.5","6","60","15","39.2","85.2","90","120","30","30","4","132.5","0.1","0.1","40.5","210","32.4","75.6","6.5","60","10.4","66.6","2.5","120","6.5","45","49.8","50.2","65.5","1","9.5","115","120","34.6","35","80","8","25","15","39","34.5","80","54.5","56","40.6","30","44.5","55","88.4","10","235","220","4","6.5","29","24.5","25","36.5","7.5","35","11.5","40.5","59","460","55.4","52.6","60","3.3","16.5","210","122","4"]
pHeight = ["0.7","1","2","0.6","1.1","1.7","0.5","1","1.6","0.3","0.7","1.1","0.3","0.6","1","0.3","1.1","1.5","0.3","0.7","0.3","1.2","2","3.5","0.4","0.8","0.6","1","0.4","0.8","1.3","0.5","0.9","1.4","0.6","1.3","0.6","1.1","0.5","1","0.8","1.6","0.5","0.8","1.2","0.3","1","1","1.5","0.2","0.7","0.4","1","0.8","1.7","0.5","1","0.7","1.9","0.6","1","1.3","0.9","1.3","1.5","0.8","1.5","1.6","0.7","1","1.7","0.9","1.6","0.4","1","1.4","1","1.7","1.2","1.6","0.3","1","0.8","1.4","1.8","1.1","1.7","0.9","1.2","0.3","1.5","1.3","1.6","1.5","8.8","1","1.6","0.4","1.3","0.5","1.2","0.4","2","0.4","1","1.5","1.4","1.2","0.6","1.2","1","1.9","1.1","1","2.2","0.4","1.2","0.6","1.3","0.8","1.1","1.3","1.5","1.4","1.1","1.3","1.5","1.4","0.9","6.5","2.5","0.3","0.3","1","0.8","0.9","0.8","0.4","1","0.5","1.3","1.8","2.1","1.7","1.6","2","1.8","4","2.2","2","0.4"]

#inputs your pokemon num guess and the actual pokemon num, sees if type 1 or 2 is correct, then returns
def typeRight(pGuessNum,pNum):
    if pType1[pNum] == pType1[pGuessNum]:
        if pType2[pNum] == pType2[pGuessNum]:
            return "Right type 1 and type 2"
        else:
            return "Right type 1"
    elif pType2[pNum] == pType2[pGuessNum]:
        return "Right type 2"
    else:
        return "Wrong type"

#inputs your pokemon num guess and the actual pokemon num, compares height, then returns
def heightRight(pGuessNum,pNum):
    if pHeight[pGuessNum] == pHeight[pNum]:
        return "Correct Height"
    elif pHeight[pGuessNum] < pHeight[pNum]:
        return "Taller"
    else:
        return "Shorter"

#inputs your pokemon num guess and the actual pokemon num, compares weight, then returns
def weightRight(pGuessNum,pNum):
    if pWeight[pGuessNum] == pWeight[pNum]:
        return "Correct Weight"
    elif pWeight[pGuessNum] < pWeight[pNum]:
        return "Heavier"
    else:
        return "Lighter"

#inputs the actual pokemon num, gets guess pokemon from user then camelcases, if user gives up can type give up to terminate loop
#if you do not enter a valid pokemon ask for another pokemon, if good converts pokemon to its index number
#if you guess correct pokemon returns "Correct" which terminates loop,
#if wrong guess checks what is right via several function then returns the results
def isRight(pNum):
    pGuess = input("Name a pokemon")
    pGuess = string.capwords(pGuess, sep = None)

    if pGuess == "Give Up":
        print(pNames[pNum])
        return "Give Up"

    if pGuess not in pNames:
        return "Not a Pokemon"
    pGuessNum = pNames.index(pGuess)

    if pNames[pNum] == pGuess:
        return "Correct"
    type = typeRight(pGuessNum,pNum)
    height = heightRight(pGuessNum,pNum)
    weight = weightRight(pGuessNum,pNum)
    return type, height, weight

#picks a random pokemon, then loops isRight until you guess the right pokemon or give up
def main():
    rdmPNum = int(random.random() * 151)

    isCorrect = "false"

    while(isCorrect != "Correct"):
        isCorrect = isRight(rdmPNum)
        print(isCorrect)
        if (isCorrect == "Give Up"):
            break

main()
