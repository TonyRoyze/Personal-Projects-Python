class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        temp = {'amount': amount, 'description': description}
        self.ledger.append(temp)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            temp = {'amount': (-1)*amount, 'description': description}
            self.ledger.append(temp)

            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']

        return balance

    def transfer(self, amount, catergory):
        if self.check_funds(amount) == True:
            wdescrption = "Transfer to " + str(catergory.name)
            ddescription = "Transfer from " + str(self.name)
            self.withdraw(amount, wdescrption)
            catergory.deposit(amount, ddescription)
            return True
        else:
            return False

    def check_funds(self, amount):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        if amount > balance:
            return False
        else:
            return True

    def __str__(self):
        count = int((30 - len(self.name))/2)
        star = "*" * count
        print(star + self.name + star)
        self.bill_items()
        return "Total: " + str(self.get_balance()) + "\n"

    def bill_items(self):
        for item in self.ledger:
            if (len(item['description']) > 23):
                desc = item['description'][:23]
            else:
                desc = item['description']

            amnt = '%.2f' % (item['amount'])

            space = " " * (30 - len(desc) - len(str(amnt)))
            print(desc + space + str(amnt))


def create_spend_chart(cat):
    print("Percentage spent by catergory")
    n = len(cat)
    names = []
    percentages = []
    for item in cat:
        names.append(item.name)

        dep = 0
        remainder = item.get_balance()
        # print(remainder)
        for i in item.ledger:
            if i['amount'] > 0:
                dep += i['amount']
        percent = round((1 - remainder / dep)*10)
        percentages.append(percent)
        # print(percent)
    # print(names)
    data = {"100": [], " 90": [], " 80": [], " 70": [], " 60": [],
            " 50": [], " 40": [], " 30": [], " 20": [], " 10": [], "  0": []}

    # print(percentages)
    for item in percentages:

        if item == 10:
            data["100"].append(" o ")
        else:
            data["100"].append("   ")
        if item >= 9:
            data[" 90"].append(" o ")
        else:
            data[" 90"].append("   ")
        if item >= 8:
            data[" 80"].append(" o ")
        else:
            data[" 80"].append("   ")
        if item >= 7:
            data[" 70"].append(" o ")
        else:
            data[" 70"].append("   ")
        if item >= 6:
            data[" 60"].append(" o ")
        else:
            data[" 60"].append("   ")
        if item >= 5:
            data[" 50"].append(" o ")
        else:
            data[" 50"].append("   ")
        if item >= 4:
            data[" 40"].append(" o ")
        else:
            data[" 40"].append("   ")
        if item >= 3:
            data[" 30"].append(" o ")
        else:
            data[" 30"].append("   ")
        if item >= 2:
            data[" 20"].append(" o ")
        else:
            data[" 20"].append("   ")
        if item >= 1:
            data[" 10"].append(" o ")
        else:
            data[" 10"].append("   ")
        if item > 0:
            data["  0"].append(" o ")
        else:
            data["  0"].append("   ")

    for k, v in data.items():
        string = k+"|"
        for item in v:
            string += item
        print(string)
    print("    "+"---"*n)

    max = 0

    li_of_lenghts = []
    li_of_letters = []

    for item in names:
        lenght = len(item)
        li_of_lenghts.append(lenght)
        if lenght > max:
            max = lenght
        for i in item:
            li_of_letters.append(i)

    li_of_lenghts = li_of_lenghts[:(len(li_of_lenghts)-1)]
    #print("letters: ", li_of_letters)
    #print("word breaks: ", li_of_lenghts)

    slc = 0
    iter = 1
    printed_li = []
    while iter <= max:
        iter += 1
        line = "     "
        #print("printing letter: ", slc)
        if slc not in printed_li:
            line += li_of_letters[slc]+"  "
        else:
            line += "   "

        pc = slc
        for item in li_of_lenghts:

            printed_li.append(pc)
            pc += item

            if pc < len(li_of_letters):
                #print("printing letter: ", pc)
                if pc not in printed_li:
                    line += li_of_letters[pc] + "  "
                else:
                    line += "   "
            else:
                line += "   "
        slc += 1
        printed_li.append(pc)
        print(line)
        #print("letters printed: ", printed_li)
