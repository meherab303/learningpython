def numberOfseniorCityzen(array):
    count=0
    for i in range(len(array)):
        if int(array[i][11:13])>60:
            count+=1
    return count        

print(numberOfseniorCityzen(["1313579440F2036","2921522980M5644"]))