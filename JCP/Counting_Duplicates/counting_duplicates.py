from collections import Counter
def counting_duplicates(word):
    result = Counter(word)
    print(result)

def counting_duplicates_II(word):
    result = dict()
    for c in word:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    print(result)

counting_duplicates("anona")
counting_duplicates_II("anona")