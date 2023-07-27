# Задача 14: Требуется вывести все целые
# степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.



inputNum = 10
numberList = [1]

while numberList[(len(numberList)-1)]<inputNum:
    numberList.append(numberList[(len(numberList)-1)]*2)
numberList.remove(numberList[(len(numberList)-1)])
print(str(numberList)[1:-1])