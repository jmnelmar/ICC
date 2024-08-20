def counting_ocurrences_of_a_character(s:str, ch:str):
    return len(s) - len(s.replace(ch,""))

str = "anona"
print(counting_ocurrences_of_a_character(str,"a"))
