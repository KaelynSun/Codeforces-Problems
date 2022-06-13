NumOfStones = int(input())
ColorOfStones = str(input())
Counter = 0

PreviousStones = None

for Stones in ColorOfStones:
    if Stones == PreviousStones:
        Counter += 1
    
    PreviousStones = Stones

print(Counter)