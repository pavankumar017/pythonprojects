
player = input("What is your name? ")
print("Hello, " + player + "!")

check = input("Dou you wanna  play the quiz game? ")

if check.lower()!= "yes":
    quit()

print("Okay lets play !")
score = 0 

q1 =  input("what is the capital of India? ")

if q1.lower() in "New delhi" :
    print("correct")
    score +=1
else:
    print("inccorrect")

q2 = q1 =  input("what is the capital of Karnataka? ")

if q1.lower() == "bengaluru" :
    print("correct")
    score +=1
else:
    print("inccorrect")


print("Your total score is "+ str(score))