###
# Zamienia literę na odpowiadające jej słowo ICAO
###
def icao(letter):
    # Zamień literę na wielką literę
    letter = letter.capitalize()

    # Przypisz odpowiednie słowo ICAO na podstawie litery
    if letter == 'A':
        icao_name = 'Alfa'
    elif letter == 'B':
        icao_name = 'Bravo'
    elif letter == 'C':
        icao_name = 'Charlie'
    elif letter == 'D':
        icao_name = 'Delta'
    elif letter == 'E':
        icao_name = 'Echo'
    elif letter == 'F':
        icao_name = 'Foxtrot'
    elif letter == 'G':
        icao_name = 'Golf'
    elif letter == 'H':
        icao_name = 'Hotel'
    elif letter == 'I':
        icao_name = 'India'
    elif letter == 'J':
        icao_name = 'Juliett'
    elif letter == 'K':
        icao_name = 'Kilo'
    elif letter == 'L':
        icao_name = 'Lima'
    elif letter == 'M':
        icao_name = 'Mike'
    elif letter == 'N':
        icao_name = 'November'
    elif letter == 'O':
        icao_name = 'Oscar'
    elif letter == 'P':
        icao_name = 'Papa'
    elif letter == 'Q':
        icao_name = 'Quebec'
    elif letter == 'R':
        icao_name = 'Romeo'
    elif letter == 'S':
        icao_name = 'Sierra'
    elif letter == 'T':
        icao_name = 'Tango'
    elif letter == 'U':
        icao_name = 'Uniform'
    elif letter == 'V':
        icao_name = 'Victor'
    elif letter == 'W':
        icao_name = 'Whiskey'
    elif letter == 'X':
        icao_name = 'X-ray'
    elif letter == 'Y':
        icao_name = 'Yankee'
    elif letter == 'Z':
        icao_name = 'Zulu'
    else:
        icao_name = '???'  # Dla nieznanych znaków

    return icao_name


# Użycie funkcji
name = input('Enter your name: ')
print('ICAO words for spelling out your name:')

# Iteracja przez każdą literę wprowadzonego imienia
for char in name:
    word = icao(char)  # Przekształć literę na odpowiednik ICAO
    print(word, end=" ")  # Wyświetl słowo ICAO
