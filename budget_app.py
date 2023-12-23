class Category:
    type = ""
    money_we_get = 0
    amounts = []
    descriptions = []
    def __init__(self,type):
        self.type = type
        self.amounts = []
        self.descriptions = []
        self.money_we_get = 0
    def deposit(self,amount,description=""):
        self.money_we_get += amount
        self.amounts.append(amount)
        self.descriptions.append(description)
    def withdraw(self,amount,description=""):
        if(self.money_we_get - amount >= 0):
            self.money_we_get += amount
            self.amounts.append(amount)
            self.descriptions.append(description)
            return False
        else:
            return True
    def get_balance(self):
        return self.money_we_get
    def transfer(self,amount,category):
        if(category.check_funds(amount)):
            self.deposit(amount,f"Transfer From {category.type} Category")
            category.withdraw(-amount,f"Transfer To {self.type} Category")
            return True
        else:
            return False
    def check_funds(self,expecting):
        if(self.money_we_get > expecting):
            return True
        else:
            return False

    def __repr__(self):
        for i in range((30-len(self.type))//2):
            print("*",end="")
        print(self.type,end="")
        for i in range((30-len(self.type))//2):
            print("*",end="")
        print(" ")
        
        for i in range(len(self.amounts)):
            gap1 = len(self.descriptions[i])
            gap2 = len(str(self.amounts[i]))
            if(len(self.descriptions[i]) <= 23):
                print(self.descriptions[i],end="")  
            else:
                for j in range(23):
                    print(self.descriptions[i][j],end="")
                gap1 = 23
            print(" " * ((23 - gap1) + (7 - gap2)),end="")
            print(self.amounts[i])
        print("Total:",'%.2f' % sum(self.amounts))
        return ""

def create_spend_chart(spends):
    percentages = {}
    sum = 0
    
    print("Percentage spent by category")
    for i in spends:
        sum += i.get_balance()
    for j in spends:
        percentage = (j.get_balance()/sum * 100)
        percentages.update({j.type:percentage})
    for i in range(100,-10,-10):
        gap = (3- len(str(i)))
        print(" " * gap + f"{i}"+ "|",end=" ")
        for j in spends:
            if(percentages[j.type] > i):
                print("o",end=" ")
            else:
                print(" ",end=" ")
        print()
    print(" " *4,end="")
    print("-"*(len(spends)*3))
    print(" " *5,end="")
    start = 0
    end = 1
    max_letter = 0
    for i in spends:
        if len(i.type )> max_letter:
           max_letter = len(i.type)
    for i in range(max_letter):
        for a in range(len(spends)):
            for j in range(start,end):
                if(j <= len(spends[a].type)-1):
                    print(spends[a].type[j],end=" ")
                else:
                    print(" ",end=" ")
        print("")
        print(" "*4,end =" ")
        start += 1
        end += 1

        
outcomes = []
Food = Category("Food")
outcomes.append(Food)
Auto = Category("Auto")
outcomes.append(Auto)
Clothing = Category("Clothing")
outcomes.append(Clothing)

Food.deposit(1000.00,"initial deposit")
Food.withdraw(-15.17,"grocories")
Food.withdraw(-50.00,"Transfer To Clothing")
Food.withdraw(-10.89,"restaraunt and more food shopping")

Clothing.deposit(1000.00,"initial deposit")
Clothing.withdraw(-15.17,"grocories")
Clothing.withdraw(-50.00,"Transfer To Clothing")
Clothing.withdraw(-10.89,"restaraunt and more food shopping")

Auto.deposit(1000.00,"initial deposit")
Auto.withdraw(-15.17,"grocories")
Auto.withdraw(-50.00,"Transfer To Clothing")
Auto.withdraw(-50.00,"Transfer To Clothing")
Auto.withdraw(-50.00,"Transfer To Clothing")
Auto.withdraw(-10.89,"restaraunt and more food shopping")
Auto.transfer(400.00,Food)

create_spend_chart(outcomes)

print(Auto)

print(Food)

print(Clothing)
