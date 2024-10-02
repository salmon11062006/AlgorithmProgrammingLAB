myDict = {    
    '0':'o',
    '1':'i',
    '3':'e',
    '4':'a',
    '5':'s',
    '7':'t',
    ' ': ' '
}

new_sentence = ''
sentence = str(input("Enter your sentence: "))
v = list(sentence.lower())

for x in v:
    new_sentence += str(myDict.get(x))
print(new_sentence)