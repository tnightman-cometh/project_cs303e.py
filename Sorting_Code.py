print = ("Rosalina", "Princess Peach", "Toad", "Yoshi", "Luigi", "Mario", "Wario", "Donkey Kong", "Bowser", "Waluigi")

unsorttedList = [x.strip("\n") for x in open("alphabet.txt")]

def upper_case(startingList):
    newList = []
    for word in startingList:
        newList.append(word.capitalize())
    return newList

def partition(list, first, last):
    pivot = list[last]
    lower = first - 1
    top = last

    done = 0
    while not done:

        while not done:
            lower += 1
            if lower == top:
                done = 1
                break
            if list[lower] > pivot:
                temp = list[top]
                list[top] = list[lower]
                list[lower] = temp
                break

        while not done:
            top -= 1
            if top == lower:
                done = 1
                break
            if list[top] < pivot:
                temp2 = list[lower]
                list[lower] = list[top]
                list[top] = temp2
                break

    list[top] = pivot
    return top

def quicksort2(list, first, last):
    if first < last:
        p = partition(list, first, last)
        quicksort2(list, first, p-1)
        quicksort2(list, p+1, last)

def quicksort(list):
    quicksort2(list, 0, len(list)-1)

def main():
    quicksort(unsorttedList)
    for element in unsorttedList:
        print (element)
main()

numList = [10, 40, 30, 20, 50, 60]
print("Sort the list, show each move.")
print(numList)
avglength = len(numList)

for i in range(avglength):
    for j in range(avglength - 1):
        if numList[j] > numList[j + 1]:
            numList[j], numList[j + 1] = numList[j + 1], numList[j]
            print(numList)
