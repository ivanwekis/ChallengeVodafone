### This script was developed by Iván Moreno Arias using Python 3
#### The purpose of this program is to be able to encrypt a csv file taking into account the following points :

- If the input file does not have the header correctly, that is, it does not have a "Name", "Email" and "Invoicing", or does not exist, a message will be written on the console indicating it.
- The code checks the email and check that the billing field is a number.
- The output encrypted file is shown with 'X'. Except for the billing field, which shows the average of all customers.
- If the output file does not exist it is created, and if it does exist it will be overwritten without warning.
- Finally, some statistics are shown on the console. The average, maximum and minimum billing is shown. The average, maximum and minimum length of the names is also shown.
__ __
*CODE STRUCTURE*
#### The code is structured in modules that perform different functions. There are 5 modules in total:
1. main.py: This is the core of the script. Here we execute the different functions of the rest of the modules in order.
2. data_io.py:  The input/output module. In it, we have the functions that allow us to read the .csv files and write to the output one.
3. validations.py: In this module we check if the csv file has a correct format, it also returns a dictionary with the csv information for later encryption.
4. mask.py: As its name indicates, in this module we carry out the algorithms that allow us to encrypt the file.
5. stats.py: Finally, in this module, we calculate the statistics of the costumers, whether they are their name or billing.
__ __ 
*EXECUTION*
#### To execute the code the way is to write in the console "Python3 main.py arg1 arg2", where arg1 is the name of the input .csv file and arg2 is the name of the output file.
```commandline
python3 main.py argv[1] argv[2]
```
#### With the examples provided in the files, an example of execution is...
```commandline
python3 main.py customers2.csv encrypted.csv
```
#### You may need to give it execute permissions using the chmod command.
__ __ 
*POSIBLE ERRORS*
#### Errors may appear during execution when the csv file does not have a correct structure. The most common errors are:
- It is necessary to enter at least two parameters, the input file and the output file. If these two parameters are not entered an exception will be thrown.
- If a costumer has the billing field misspelled, that is, it is not a number or has characters that are not numbers, the value will not be taken into account to make the average, it will be ignored.
- The email will be checked to see if it has a valid structure. If the email does not have a valid structure, all its letters and numbers will be replaced by '-'.
__ __ 
*TEST*
#### Four .csv files are included, one of them is not correct (customers1.csv) and has been done on purpose. The other two are correct and completely different.
#### One of the correct .csv files could be like the next csv format.    
    Billing,Email,Name
    1340,santi@hotmail.com,Santi Juarez
    1250,adricabeza@gmail.com,Adrian Leon
    345,martiitaa@gmail.es,Marta Sanchez
    670,elchulodelbarrio@hotmail.com,David Bisbal
    980,lahuertaencasa@gamil.es,Calabacin
#### If we use the previous example to perform a test, the output we get is the following...
    Email,Name,Date,Billing,Age
    XXXXX@XXXXXXX.XXX,XXXXX XXXXXX,XX-XX-XXXX,917.0,XX
    XXXXXXXXXX@XXXXX.XXX,XXXXXX XXXX,XX-XX-XXXX,917.0,XX
    XXXXXXXXX@XXXXX.XX,XXXXX XXXXXXX,XX-XX-XXXX,917.0,XX
    XXXXXXXXXXXXXXXX@XXXXXXX.XXX,XXXXX XXXXXX,XX-XX-XXXX,917.0,XX
    XXXXXXXXXXXXXX@XXXXX.XX,XXXXXXXXX,XX-XX-XXXX,917.0,XX
#### And the output that the script returns to us by console is like this...
    The file is correct
    Stats for the Billing:
     average: 917.0, minimum: 345, maximum: 1340
    Stats for the Name :
     average: 11.4, minimum: 9, maximum: 13
__ __ 
*FILE WITH ERRORS*
#### The 'customers4.csv' is a file with a correct format, but it has an error in the email and another in the billing of one of the costumers.
    Email,Name,Date,Billing,Age
    santi@hotmail.com,Santi Juarez,24-05-2005,1340,23
    adricabeza@gmail.com,Adrian Leon,23-08-1999,125O,34
    martiitaa@gmail.es,Marta Sanchez,17-02-2007,345,62
    elchulodelbarrio@hotmailcom,David Bisbal,24-08-2009,670,41
    lahuertaencasagmail.es,Calabacin,13-09-2008,980,22
#### The output file is as shown below. We can see that the email that is not correct appears replaced by '-' and that to calculate the average it has not taken into account the value that is wrong.
    Email,Name,Date,Billing,Age
    XXXXX@XXXXXXX.XXX,XXXXX XXXXXX,XX-XX-XXXX,833.75,XX
    XXXXXXXXXX@XXXXX.XXX,XXXXXX XXXX,XX-XX-XXXX,833.75,XX
    XXXXXXXXX@XXXXX.XX,XXXXX XXXXXXX,XX-XX-XXXX,833.75,XX
    XXXXXXXXXXXXXXXX@XXXXXXX.XXX,XXXXX XXXXXX,XX-XX-XXXX,833.75,XX
    -------------------.--,XXXXXXXXX,XX-XX-XXXX,833.75,XX
#### Both errors are shown on the console, in addition to the statistics.
    The file is correct
    One of the billing data does not have a correct format: 12SO
    The following email isn´t correct, please, correct it:  lahuertaencasagmail.es
    Stats for the Billing:
     average: 833.75, minimum: 345, maximum: 1340
    Stats for the Name :
     average: 11.4, minimum: 9, maximum: 13
