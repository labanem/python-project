#A translator program

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in 'a,e,i,o,u':
            if letter.isupper():
                translation = translation + 'X'
            else:
                translation = translation + 'x'
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter Phrase: ")))
