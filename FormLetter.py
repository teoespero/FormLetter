# ****
# Program Name: FormLetter.py
# Author: Teo Espero (GIST)
# Date Written: 20200426
# Description:  Write a program that will print three form letters asking for votes in the upcoming election.
#               This program will make use of Python's tuples and list handling capabilities
# ****

def printTemplate(addressee, candidate, sender):
    ## This UDf is designed to accept parameters from the
    ## main program. This will be the UDF to print the
    ## formletter.

    ## To simplify the approach we will be concatenating the message
    ## from several parts. Inserting the value from the list and tuple
    ## as needed in our letter.

    message = "Dear %s,\n" % (addressee)
    message = message + "I would like you to vote for %s\n" % (candidate)
    message = message + "because I think %s is best for\n" % (candidate)
    message = message + "this country.\n\n"
    message = message + "Sincerely,\n"
    message = message + "%s\n" % (sender)

    ## print the formletter
    ## along with its data
    print(message)
    return


## Main Program

## tuple for the candidate names
candidate = ("Joe Biden", "Bernie Sanders", "Donald Trump")

## list for the candidate names
addressee = ["Hildegard", "Cheech", "Moe"]

##sender
sender = "Brunhilda"

## we will be using a for loop
## to go through the candidate names
for names in candidate:
    ## on this part we are using the index posiition of
    ## the candidate to position which data is to be sent
    ## to the function

    printTemplate(addressee[candidate.index(names)], candidate[candidate.index(names)], sender)

## EOF

## output
"""
Dear Hildegard,
I would like you to vote for Joe Biden
because I think Joe Biden is best for
this country.

Sincerely,
Brunhilda

Dear Cheech,
I would like you to vote for Bernie Sanders
because I think Bernie Sanders is best for
this country.

Sincerely,
Brunhilda

Dear Moe,
I would like you to vote for Donald Trump
because I think Donald Trump is best for
this country.

Sincerely,
Brunhilda"""
