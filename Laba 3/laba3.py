class Budget:
    mainc = {0: 0}
    counts = {}

    def __init__(self, number, sum):
        Budget.counts.update({number: sum})
        self.number = number
        self.sum = sum

    def add(self, suma):
        if suma > Budget.counts[self.number]:
            return print("You don't have enough money.")
        else:
            Budget.mainc[0] += suma
            Budget.counts[self.number] -= suma

    def check(self):
        return 'Your budget is ' + str(Budget.mainc[0])

    def take(self, suma):
        if suma > Budget.mainc[0]:
            return 'Your budget is too small.'
        else:
            Budget.mainc -= suma
            Budget.counts[self.number] += suma

    def chkfamily(self):
        j = 1
        for i in Budget.counts.keys():
            print(str(j) + ') ' + str(Budget.counts[i]))
            j += 1

f1 = Budget(1111, 345)
f2 = Budget(2222, 865)
f3 = Budget(3333, 957)
print(f1.check())
f2.add(350)
f1.add(350)
f3.add(650)
print(f2.check())
f2.chkfamily()
