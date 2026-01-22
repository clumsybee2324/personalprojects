my_num=15
i=0
while i<3:
    guess=int(input("Guess the number: "))
    if(my_num== guess):
        print("WELL DONE! ")
        break
    else:
        i+=1
