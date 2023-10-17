print("What is the capital city of Japan?")
answer = input("Ans: ")
# if answer == "Tokyo" or answer == "TOKYO" or answer == "tokyo":
if answer.upper() == "TOKYO":
    print("RIGHT!")
else:
    print("WRONG!")
