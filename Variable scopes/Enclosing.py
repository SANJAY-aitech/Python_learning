#L --> E --> G --> B

#E == Enclosing
#It is done using nested function (function inside a function)

#===example===

def detail():
    age = 19 #Enclosing Variable

    def display():
        print("He is",age,"years old")
    display()
detail()
#He is 19 years old