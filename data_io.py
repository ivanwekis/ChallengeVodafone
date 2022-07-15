import mask


def average_billing(dat, pos):
    """this function calculates the average billing of costumers, is used in the
    'write_header_and_encrypted_data' function"""

    ave = 0
    num = 0
    for row in dat:
        num = num+1
        ave = ave + int(float(row.split(',')[pos]))
    ave = ave/num
    return ave


def exist_and_download_file(file_name):
    """This function allows you to check if the file entered by parameters exists.
    If it is correct, it returns the data."""
    try:
        dat = open(str(file_name))
        return dat
    except FileNotFoundError as err:
        print("The file doesn't exists: ", err)
        exit(0)


def write_header_and_encrypted_data(header, costumers, encrypted_csv):
    """This functions writes the header without been encrypted in the encrypted file and later
    encrypt the data costumer by costumer"""
    try:
        num = len(header)
        num = num-1
        i = 0
        for word in header:
            if i == num:
                encrypted_csv.write(word + '\n')
            else:
                i = i + 1
                encrypted_csv.write(word + ",")

        average = mask.average_billing(costumers)

        for x in range(len(costumers)):
            for i in range(len(costumers[x])):
                if header[i] == "Email":
                    email = mask.validate_and_encrypt_email(costumers[x].get(header[i]))
                    encrypted_csv.write(email)
                elif header[i] == "Billing":
                    encrypted_csv.write(str(average))
                else:
                    word = mask.encrypt_word(costumers[x].get(header[i]))
                    encrypted_csv.write(word)
                if i == len(costumers[x])-1:
                    encrypted_csv.write("\n")
                else:
                    encrypted_csv.write(",")
    except IndexError as err:
        print("Index error: ", err)
        exit(0)

