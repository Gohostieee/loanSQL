from loanOBJS import loanOBJ
from datetime import date
def diff_dates(date1, date2):
    return abs(date2-date1).days
def name_check():
    while True:
        print("ENTRY ALREADY EXISTS USE ANOTHER NAME? N/Y")
        with Switch(input().upper()) as case:
            if case("N"):
                return 0
            if case("Y"):
                while True:
                    name=input("Give me a name!!!\n")
                    if row_exists(name):
                        print("NAME ERROR!!!")
                        continue
                    else:
                        return name 
def rate_check(rate):
    while True:
        if rate.isnumeric() and rate!=0:
            rate=rate.replace("%", "")

            return float(rate)
        else:
            rate=input("oop rate error, gimme another:")
def date_check(date):
    while True:
        for x in date.split("-"):
            if not x.isnumeric():
                date=input("error, 1go again(format==02-21-2004):")
                continue

        try:
            if int(date.split("-")[0])>12 or int(date.split("-")[1])>31 or len(date.split("-"))==2:
                    date=input("error, 2go again(format==02-21-2004):")
                    continue
        except:
                date=input("error, go 3again(format==02-21-2004):")
                continue
        return date
def amount_check(amount):
    while True:
        try:
            if amount.isnumeric():
                return int(amount)
        except:
            pass
        amount=input("something aint quite right, do it again:")
def objectifier(list):
    listOBJ=loanOBJ()
    listOBJ.name=list[0]
    listOBJ.rate=list[1]
    listOBJ.deadline=list[2]
    listOBJ.amount=list[3]
    listOBJ.type=list[4]
    return listOBJ
