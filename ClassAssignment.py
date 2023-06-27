class AllSnippets():
    
    
    lists = [1,2,3,4,5,6]



    def TechName():
        
        for names in lists:
            
            if names == 1 :
                print("Machine Learning")

            elif names == 2 :
                print("Neural Networks")

            elif names == 3 :
                print("Vision")

            elif names == 4 :
                print("Vision")

            elif names == 5 :
                print("Speech Processing")

            elif names == 6 :
                print("Natural Language Processing")
                
                
                
                
    def OddEven():
        
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(number ,"is Even number")
            message = number,"is Even number"
        else:
            print("Not Even number")
            message = "Not Even number"
        return message
    
    
    def age():
        
        name = input("Your Gender: ")
        age = int(input("Your Age: "))
        if age > 21:
            print("ELIGIBLE")
            message = "ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            message = "NOT ELIGIBLE"

        return message
    


    def percentage(Subject1, Subject2, Subject3, Subject4, Subject5):
        total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        average = (total / 500) * 100
        print("Subject1 =", Subject1)
        print("Subject2 =", Subject2)
        print("Subject3 =", Subject3)
        print("Subject4 =", Subject4)
        print("Subject5 =", Subject5)
        print("Total:", total)
        print("Percentage:", average)
           
        Subject1= 98
        Subject2= 87
        Subject3= 95
        Subject4= 95
        Subject5= 93
        
        
    def triangle1(Height_first, Breadth_first):
        area_of_triangle = (Height_first * Breadth_first) / 2
        print("Height:", Height_first)
        print("Breadth:", Breadth_first)
        print("Area of triangle: ", area_of_triangle )
        
        
        Height_first = 32
        Breadth_first = 34
        
        
        
    def triangle(Height1,Height2, Breadth):
        perimeter_of_triangle = Height1+Height2+Breadth
        print("Height1:",Height1)
        print("Height2:",Height2)
        print("Breadth:", Breadth)
        print("Perimeter of triangle: ", perimeter_of_triangle )
        
        
        
        Height1=2
        Height2=4
        Breadth=4