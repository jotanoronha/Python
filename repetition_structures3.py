# This code counts and shows the amount of even and odd numbers between the values set by user.

v = int(input("Type a value: "))
p = int(input("Type another value: "))

# Ask the user if the count will be even or odd

c = str(input("Witch number you want to see (odd or even)? "))



if c == "odd":
    if p > v:        
        print(f"You choose, {c}")

        if v % 2 != 1:
            v = + 1

            for i in range(v,p + 1,2):
                print(i)
        else:
            for i in range(v,p + 1,2):
                print(i)


    else:
        print(f"You choose, {c}")

        if v % 2 != 1:
            v = (v +1)

            for x in range(p,v -1,2):
                print(x)   
        else:
            for x in range(p,v -1,2):
                print(x)

        
elif c == "even":

    if p >= v:        
        print(f"You choose, {c}")

        if v % 2 != 0:
            v, p = + 1 

            for i in range(v,p + 1,2):     
                print(i)
        else:
            for i in range(v,p + 1,2):     
                print(i)


# its cool use this expression below if you want to switch the start.
# v > p
# v, p = p, v

    else:
        print(f"You choose, {c}")
        v >= p
        if v % 2 != 0:
            v = (v +1)

            for x in range(p,v -1,2):
                print(x)
        else:
            for x in range(p,v -1,2):
                print(x) 
else:    
    print("You most type a value (odd or even).")