'''
Counting vowels in python3
'''
def CountingVowels(str):
    str = str.lower()
    vowels = 'aeiou'
    vowelsCount = 0
    consonantsCount = 0
    for c in str:
        if c in vowels:
            vowelsCount += 1
        elif c >= 'a' and c <= 'z':
            consonantsCount += 1
    return vowelsCount, consonantsCount

while 1==1:
    print("Enter a phrase - enter exit to close the program")
    x = input()
    if x=="exit":
        exit()
    vowels, consonants =  CountingVowels(x)
    print(f'vowels: {vowels}, consonants: {consonants}')