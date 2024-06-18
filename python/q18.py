def anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False
    
    frequency_str1 = {}
    frequency_str2 = {}
    
    for char in str1:
        if char in frequency_str1:
            frequency_str1[char] += 1
        else:
            frequency_str1[char] = 1
    
    for char in str2:
        if char in frequency_str2:
            frequency_str2[char] += 1
        else:
            frequency_str2[char] = 1
    
    return frequency_str1 == frequency_str2


print(anagrams("listen","silent"))
print(anagrams("Hello", "hello"))
print(anagrams("aabbcc", "aabbc"))

    
