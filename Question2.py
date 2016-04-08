def main():
    outputDictionary = {'a': 1, 'c': 3, 'b': 2, 'd': 8}
    outputSum = 0
    for k in outputDictionary:
        outputSum += outputDictionary[k]
    print(outputSum)
main()
