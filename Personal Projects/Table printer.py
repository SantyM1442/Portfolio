tabledata=[['apples','oranges','cherries','banana'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','moose','goose']]
def printTable(list):
    colWidths = [0] * len(list)
    for i in range(len(list)):
        for x in list[i]:
            if colWidths[i]<len(x):
                colWidths[i]=len(x)

    for i in range(len(list[0])):
        for x in range(len(list)):
            print(list[x][i].rjust(colWidths[x]), end=' ')
        print()

printTable(tabledata)