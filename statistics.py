
def calculateStats(numbers):
    if numbers == []:
        return float("nan")
    return{'avg': sum(numbers)/len(numbers), "max": max(numbers),
           "min": min(numbers)}
