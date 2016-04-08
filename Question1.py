def main():
    inputList = [ 'a', 1, 'b', 2, 'c', 3, 'd',8 ]
    outputDictionary = dict(zip(inputList[0::2], inputList[1::2]))
    print(outputDictionary)
main()
