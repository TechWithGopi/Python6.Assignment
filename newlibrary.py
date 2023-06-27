class multipleFunctions():
    def odd_even():
        num = int(input("Enter the number: "))
        if num % 2 == 1:
            print("Odd Number")
            message = "Odd Number"
        else:
            print("Even Number")
            message = "Even Number"
        return message

    
    def BMI():
        BMI = int(input("Enter the BMI Index:"))
        if BMI  < 18.5:
            print("Underweight")
            message = "Underweight"
        elif BMI< 25.9:
            print("Normal")
            message = ("Normal") 
        elif BMI < 29.9:
            print("Overweight")
            message = "Overweight"
        else:
            print("Very Overweight")
            message = "Very Overweight"
        return message