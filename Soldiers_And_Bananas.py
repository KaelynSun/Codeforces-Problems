FirstCost, TotalMoney, NumberOfBananas = map(int, input().split(" "))
SpentMoney = 0

for i in range(NumberOfBananas + 1):
    CostofBananas = i * FirstCost
    SpentMoney += CostofBananas

if  SpentMoney > TotalMoney:
    BorrowedMoney = SpentMoney-TotalMoney
    print(BorrowedMoney)
elif SpentMoney <= TotalMoney:
    print(0)