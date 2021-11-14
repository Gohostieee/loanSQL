from loanOBJS import loanOBJ
from loans import mycursor,db
from loanFunc import *
from switch import Switch
loan=[]
def row_exists(row):
    global mycursor
    query=("SELECT EXISTS(SELECT * from loan WHERE name= %s)")
    mycursor.execute(query,(row, ))
    return mycursor.fetchone()[0]
def create():
    loan.append(input("Give me a name:").strip())
    name=loan[len(loan)-1]
    globals()[name]=loanOBJ()
    globals()[name].name=name
    if row_exists(globals()[name].name):
        globals()[name].name=name_check()
        if globals()[name].name:
            pass
        else:
            exec("continue")
    globals()[name].rate=rate_check(input("what is the interest rate?:"))
    while True:
        globals()[name].type=input("'monthly' or 'annual' rates?:").strip()
        if globals()[name].type=='monthly' or globals()[name].type=='annual':
            break
        print("INPUT ERROR!!")

    globals()[name].deadline=date_check(input("input the deadline(formatted as m-d-y or 02-21-2004):").strip())
    globals()[name].amount=amount_check(input("How hard did you fuck yourself over?(amount):"))
    print(globals()[name].name," ",globals()[name].type," ",globals()[name].rate," ",globals()[name].deadline," ",globals()[name].amount)
    print(row_exists(globals()[name].name))
    mycursor.execute('INSERT INTO loan(name,amount,deadline,type,rate) VALUES (%s,%s,%s,%s,%s)', (globals()[name].name,globals()[name].amount,globals()[name].deadline,globals()[name].type,globals()[name].rate))
    print("data committed")
    db.commit()
def promiscuo(loanList,loanNames):
    count=0
    print("choose one:")
    for x in loanList:
        print(count,"-",x.name," ",end='')
        count+=1
        loanNames.append(x.name)
    print()
    while True:
        name=int(input(""))
        if name not in range(len(loanNames)):
            print("shitty choice, try again")
            pass
        else:
            break
    print("day")
    day=input()

    rateCalc=diff_dates(date(int(loanList[name].deadline.split('-')[2]),int(loanList[name].deadline.split('-')[0]),int(loanList[name].deadline.split('-')[1])),date(int(day.split('-')[2]),int(day.split('-')[0]),int(day.split('-')[1])))
    #i have zero clue how loans work so im pretty certain this thing doesnt work, its not a bug its just me genuinely having 0 clue what im even supposed to do
    if loanList[name].type == 'monthly':
        rateCalc=round(rateCalc/ 30.437)
        print(rateCalc)
        new_loan=loanList[name].amount
        decRate=loanList[name].rate
        print("huh",loanList[name].rate)
        while decRate>1:
            print("what",decRate)
            decRate/=10
            print("who",decRate)
        print("uhuh ",rateCalc)
        for x in range(rateCalc):
            print(new_loan*decRate," ",decRate)
            new_loan+=new_loan*decRate
            print(new_loan)
        new_loan/=2
    else:
        rateCalc=round(rateCalc/365)
        #nah
def query(type,query):
    with Switch(type) as case:
        if case('name'):
            mycursor.execute('select * from loan where name = %s',(query, ))
            return mycursor.fetchall()
