import random
import time

OPERATORS = ["+", "-", "*"]
minOperand = 3
maxOperand = 12
total_Problems = 10

def generate_problem():
    left = random.randint(minOperand, maxOperand)
    right = random.randint(minOperand, maxOperand)
    
    operator = random.choice(OPERATORS)
    
    expr = str(left) + " " + operator + str(right)
    ans = eval(expr) 
    return expr, ans

wrong =0
input ("Press enter to start!")
print("--------------------------")

start_time = time.time()

for i in range(total_Problems):
    expr, ans = generate_problem()
    while True:
        guess = input("Problem no" + str(i+1) + ":" + expr + "=")
        if guess == str(ans):
            break
        wrong += 1
        
end_time = time.time()
total_time = round(end_time - start_time,2)
        
print("--------------------------")
print("Nice Work! You finished in", total_time, "seconds!")
    