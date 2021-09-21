def swappingData(filea, fileb):
    dataA = open(filea, "r")
    dataB = open(fileb, "r")
    dataSwap1  = dataA.read()
    dataSwap2 = dataB.read()
    dataA.close()
    dataB.close()
    dataA = open(filea, "w")
    dataB = open(fileb, "w")
    dataA.write(dataSwap2)
    dataB.write(dataSwap1)

swappingData("file1.txt", "file2.txt")    
