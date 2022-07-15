import re


def average_billing(costumers):
    """this function calculates the average billing of costumers, and check if it is correct the data,
    that is, it´s a number.If it is not correct, the value is not counted in the average."""
    try:
        avg = 0
        i = 0
        for x in range(len(costumers)):
            if costumers[x].get("Billing").isdecimal():
                avg = avg + float(costumers[x].get("Billing"))
                i = i + 1
            else:
                print("One of the billing data does not have a correct format: %s" % costumers[x].get("Billing"))
        avg = avg/i
        return avg
    except IndexError as err:
        print("An error has occurred: " + err)



def validate_and_encrypt_email(email):
    """"We check if the email has a correct format, that is, that it has an '@' and a '.'.
    If it is correct we encrypt it, if it is not, its letters are changed to '-'."""
    word = ""
    regex = '^[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        for letter in email:
            if letter.isalnum():
                word = word + 'X'
            else:
                word = word + letter
    else:
        print("The following email isn´t correct, please, correct it: ", email)
        for letter in email:
            if letter.isalnum():
                word = word + '-'
            else:
                word = word + letter
    return word


def encrypt_word(word):
    """This function encrypts any word passed to it and returns the result of the algorithm."""
    w = ""
    for letter in word:
        if letter.isalnum():
            w = w + 'X'
        else:
            w = w + letter
    return w