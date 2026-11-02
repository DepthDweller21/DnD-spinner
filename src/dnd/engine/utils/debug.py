def calculatePercentageChance(arr):
    total = 0
    for x in arr:
        total+=x
    print([(x/total)*100 for x in arr])