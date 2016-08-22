def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ualphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter.isupper():
        position = ualphabet.index(letter)
    else:
        position = alphabet.index(letter)
    return(position)

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ualphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char.isalpha():
        charpos = alphabet_position(char)
        endpos = (charpos + int(rot)) % 26
        if char.isupper():
            return (ualphabet[endpos])
        else:
            return(alphabet[endpos])
    else:
        return(char)
