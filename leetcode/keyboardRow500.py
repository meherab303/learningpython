def keyBoardRow(words):
    firstRow=set("qwertyuiop")
    secondRow=set("asdfghjkl")
    thirdRow=set("zxcvbnm")
    new_words=[]
    for word in words:
       
        if all(char in firstRow for char in word.lower()):
            new_words.append(word)
        elif all(char in secondRow for char in word.lower()):
            new_words.append(word)
        elif all(char in thirdRow for char in word.lower()):
            new_words.append(word)
         
                
            
    return new_words        

print(keyBoardRow(["hello","Alaska","Dad","peace"]))

# names = ['Alice', 'Bob']

# ages = [25, 30]
# print( zip(names, ages))
# for name, age in list(zip(names, ages)):

#     print(f'{name} is {age} years old.')

# paired = list(zip(names, ages))

# print(paired) #
# my_foods = ['pizza', 'falafel', 'carrot cake']

# friend_foods = my_foods[:]
# print(friend_foods)
