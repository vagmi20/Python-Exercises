def vowelsList(str): 
    l = list(str.lower())
    listOfVowels = []
    for i in l:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            listOfVowels.append(i)
    return listOfVowels

print(vowelsList("I love all the Bhagavathulas"))
