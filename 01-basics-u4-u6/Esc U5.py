escerciseUser = int(input("enter the number of the exercise you want to see: "))

while escerciseUser > 0: 
    if escerciseUser == 1 :
        #esc 1 
        print("\nesc 1")
        a = False 
        b = True
        r = not a and b
        print(r)

        a = False
        b = False
        r = not a and b
        print(r)

        a = False
        b = True
        r = (a and b) or (not a and not b)
        print(r)

        a = 8
        b = 28
        r = a < b and b < 10
        print(r)

        a = 8
        b = 28
        c = 88
        r = a < b and b < 10 and c == 88
        print(r)
        pass
    elif escerciseUser == 2 :
        #esc 2 
        print ("\nesc 2") 
        a = input ("enter 1st word: ")
        b = input ("enter 2nd word: ")
        if (a < b):
            print ("A is longer than B and its length is:({})".format(len(a)))
        if (a > b):
            print ("B is longer than A and its length is:({})".format(len(b)))
        if (a == b):
            print ("A and B have the same length and their combined length is:({})".format(len(a)+ len(b)))
        pass
    elif escerciseUser == 3 :
        #esc 3
        print ("\nesc 3")
        fl1 = float (input ("enter a float number: "))
        fl2 = float (input ("enter a second float number: "))
        fl3 = float (input ("enter a third float number: "))

        sum = fl1 + fl2 + fl3
        median = sorted([fl1, fl2, fl3])[2]
        print("the median of the 3 numbers is:", median)
        pass
    
    elif escerciseUser == 4 :   
        #esc 4 print for in range
        print ("\nesc 4")
        for i in range (1, 11):
            print (i)
        pass
    elif escerciseUser == 5 :
        #esc 5 print break
        print ("\nesc 5")
        sum = 0
        while True:
            n = int (input ("enter a number (0 to stop): "))
            if n == 0:
                break
            sum += n
        print ("the sum is:", sum)
        pass
    elif escerciseUser == list:
        #list comprehension
        print ("\nesc list comprehension")
        input_list = [1, 2, 3, 4, 5]
        output_list = [i for i in input_list if i%2 == 0]
        print (output_list)
        pass
    elif escerciseUser == dict:
        #dictionary comprehension
        print ("\nesc dictionary comprehension")
        input_list = {1,2,3,4,5,6,7}
        output_dict = {i: i**2 for i in input_list if i%2 != 0}
        print (output_dict)
        pass
    elif escerciseUser == set:
        #set comprehension
        print ("\nesc set comprehension")
        input_list = [1,2,3,4,5,6,7,8,9,10]
        output_set = {i for i in input_list if i%3 == 0}
        print (output_set)
        pass
    elif escerciseUser == "exit":
        break
    escerciseUser = int(input("enter the number of the exercise you want to see:"))
