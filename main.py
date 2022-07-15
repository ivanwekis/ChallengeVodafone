import sys
import data_io
import stats
import validations


def main():
    """This is the main part of the code, here we execute in order the different instructions"""
    try:
        header_list = {'Name', 'Email', 'Billing'}
        data = data_io.exist_and_download_file(str(sys.argv[1]))
        header = validations.check_csv(data, header_list)
        costumers = validations.costumer_dictionary(data, header)

        with open(str(sys.argv[2]), 'w') as encrypted_csv:
            data_io.write_header_and_encrypted_data(header, costumers, encrypted_csv)

        avg, mini, maxi = stats.billing_stats(costumers)
        print("Stats for the Billing:\n average: %s, minimum: %s, maximum: %s" % (avg, mini, maxi))
        avgn, minin, maxin = stats.name_stats(costumers)
        print("Stats for the Name :\n average: %s, minimum: %s, maximum: %s" % (avgn, minin, maxin))
    except IndexError as err:
        print("Please, introduce at least two parameters: 'python3 main.py argv[1] argv[2]' \n", err)


if __name__ == '__main__':
    main()


