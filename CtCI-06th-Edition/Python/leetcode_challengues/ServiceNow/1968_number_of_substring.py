def countDistinct(s: str) -> int:
    count = 0
    dict = {}
    left, right = 0,0
    n = len(s)
    substr = ""
    while left < n:
        substr = s[left:right + 1]
        right += 1
        if substr not in dict:
            dict[substr] = 1

        if right > n - 1:
            left += 1
            right = left
    print(len(dict))
    
    

s = "aabbaba"
countDistinct(s)
