def check_csv(dat, header):
    """this function allows you to check if the .csv file is correct and includes the specified headers.
     If it is correct, it returns a list with the file headers."""
    try:
        check = 0
        header_file = next(dat)
        num = header_file.count(',')
        num = num+1
        lt = []
        for i in range(num):
            lt.append(header_file.split(',')[i])
            if i == (num-1):
                x = lt[i]
                x = x.replace("\n", "")
                lt.pop(i)
                lt.append(x)
        for word in header:
            if word in lt:
                check=check+1

        if check == len(header):
            print("The file is correct")
            return lt
        else:
            print("The format of the .csv file doesn't correct.")
            exit(0)
    except TypeError as err:
        print("The file doesn't exists", err)


def costumer_dictionary(data, header):
    """To handle the information in the csv in a simple way, we make use of the information by entering it
    into a dictionary."""
    i = 0
    costumers = {}
    for row in data:
        costumer = {}
        for x in range(len(header)):
            costumer[header[x]] = row.split(',')[x].replace("\n", "")
        costumers[i] = costumer
        i = i+1
    return costumers
