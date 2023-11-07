try:
    mark = int(input("Enter mark: "))
    if mark >= 0 and mark <= 100:
        if mark >= 80:
            print("DISTINCTION")
        elif mark > 40:
            print("PASS")
        else:
            print("FAIL")
    else:
        print("INVALID DATA")    
except:
    print("INVALID DATA")

