
def input_positive_float(question):
    while True:
        try:
            number = float(input(question))
            if number < 0:
                print("Enter a positive number")
            else:
                return number
        except ValueError as e:
            print("Enter a number.")
##utility ensures the price is a positive float
def input_yes_or_no(question):
    itsavailable = 'yes'
    notavailable = 'no'
    while True:
        available = input(question)
        if available.lower() == itsavailable:
            return 1
        elif available == notavailable:
            return 0
        else:
            print("Enter yes or no")
## this utility verifies that they input yes or no for available
## returns 1 for yes, 0 for not available
