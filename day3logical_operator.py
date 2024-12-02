#and -> if all condition are 
# true then only true, otherwise false 
#False and false = false eg: voting system
# true and false = false 
# false and true = false

#OR
#-> if any condition are true then result is true 
#eg: login email, login num 
#true or false : true , fasle or true : true , false or false : false , true or true : true 
"""not : not true: false
not false : true 

#comprasion operator: <,> <= , =>, =(mean barabar), ==,= , !- 
bit wise operator = || 

* string manipuator.
#string concatenation 
str7 ="sushil"
str8 ="shrestha"

finalString = str7 + " "+ str8 
print(finalString,"\n")


print("Enter the age:")
age=int(input())

print("\nEnter the Citizenship:")
citizenship = input()

#condition check
if(age>18 and citizenship=="nepali"):
    print("You can Vote")
else:
    print("sorry") 
    
first_name ="ram"
second_name ="shyam"

print(first_name+second_name) #concat

a="ram"
b="9"
print(a+str(b))
first_sentence = "   hello i am  from  mars   "

str ="i am studing python from apna COllege"

print(str.endswith("ege"))   #returns true of string ends with substr
print(str.endswith("apna"))

print(str.capitalize()) #capitalize first string

#replace old string to new string
print(str.replace("a" ,"O")) #str.replace("old-string, "new-replace-string)

#to find string position in first
print(str.find("o")) #return 1st index of 1st occurance

#count the string from specifice string
print(str.count("am")) #count the occurance of substr
print(str.count("a"))

#remove the whiteSpace
firstString ="     this is  BIT Student    "
print(firstString.strip())

#splite the String
skill_shikshya = "skillshikshya@gmail.com"

splite_data = skill_shikshya.split('@')
print(splite_data)

String Handing Function In Python
str.endswith()
str.capitalize()
str.replace()
str.find()
str.count()
str.strip() #remove whiteSpace
str.split() #splite string 


#WAP to find occurance of '$' in a string 
str1 ="the Dollor $ price in Nepal in current time is $1 per dollor is about Rs.136"

findValue= str1.count("$")
print("The Position Of string $ in the above string is:", findValue)
""" 

father_name =  "some name"
print(father_name.upper())
print(father_name.capitalize())
print(father_name.title()) 

#class work , describe any 10 string manipulation function with example

s = "Hello, World!"
print(len(s))  # Output: 13 

s = "Hello, WORLD!"
print(s.lower())  # Output: hello, world! 

s = "hello, world!"
print(s.upper())  # Output: HELLO, WORLD!

s = "   Hello, World!   "
print(s.strip())  # Output: "Hello, World!"

s = "apple,banana,cherry"
print(s.split(","))  # Output: ['apple', 'banana', 'cherry']

fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))  # Output: "apple, banana, cherry"

s = "I like apples"
print(s.replace("apples", "bananas"))  # Output: "I like bananas"

s = "Hello, World!"
print(s.find("World"))  # Output: 7
print(s.find("Python"))  # Output: -1


s = "Hello, World!"
print(s.startswith("Hello"))  # Output: True
print(s.startswith("World"))  # Output: False

s = "hello, world!"
print(s.capitalize())  # Output: "Hello, world!"