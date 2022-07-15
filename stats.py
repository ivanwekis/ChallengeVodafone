def billing_stats(costumers):
    """"This function return the stats of the billing. It returns the average, maximum and minimum billing"""
    avg = 0
    mini = 100000000
    maxi = 0
    i=0
    for x in range(len(costumers)):
        if costumers[x].get("Billing").isdecimal():
            value = costumers[x].get("Billing")
            value = int(value)
            avg = avg + value
            if value > maxi:
                maxi = value
            if value < mini:
                mini = value
            i = i + 1
    avg = avg/i
    return avg, mini, maxi


def name_stats(costumers):
    """"This function return the stats of the billing. It returns the average, maximum and minimum length of the name"""
    avgn = 0
    minin = 100000000
    maxin = 0
    for x in range(len(costumers)):
        value = len(costumers[x].get("Name"))
        avgn = avgn + value
        if value > maxin:
            maxin = value
        if value < minin:
            minin = value
    avgn = avgn / len(costumers)
    return avgn, minin, maxin

