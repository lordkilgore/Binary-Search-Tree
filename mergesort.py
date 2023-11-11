def merge(inputArray, startIndex, endIndex, mid):
    mergedArray = [i for i in range(endIndex - startIndex + 1)]

    mergePos = 0
    leftPos = startIndex
    rightPos = mid + 1

    while (leftPos <= mid and rightPos <= endIndex):
        if inputArray[leftPos] <= inputArray[rightPos]:
            mergedArray[mergePos] = inputArray[leftPos]
            leftPos = leftPos + 1
        else:
            mergedArray[mergePos] = inputArray[rightPos]
            rightPos = rightPos + 1
        
        mergePos = mergePos + 1
    
    while (leftPos <= mid):
        mergedArray[mergePos] = inputArray[leftPos]
        leftPos = leftPos + 1
        mergePos = mergePos + 1

    while (rightPos <= endIndex):
        mergedArray[mergePos] = inputArray[rightPos]
        rightPos = rightPos + 1
        mergePos = mergePos + 1
    
    for i in range(len(mergedArray)):
        inputArray[startIndex + i] = mergedArray[i]

def mergeSort(inputArray, startIndex = 0, endIndex = "n"):
    if endIndex == "n":
        endIndex = len(inputArray) - 1

    mid = 0

    if (startIndex < endIndex):
        mid = ((startIndex + endIndex) // 2)

        mergeSort(inputArray, startIndex, mid)
        mergeSort(inputArray, mid + 1, endIndex)

        merge(inputArray, startIndex, endIndex, mid)
