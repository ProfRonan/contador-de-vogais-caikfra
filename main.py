def count_vowels(string: str) -> int:
    vogais = "aeiouAEIOU"
    contador = 0
    for char in string:
        if char in vogais:
            contador +=1
    return contador