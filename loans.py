from switch import Switch
import mysql.connector
from loanFunc import *
from loanCommands import *
from loanOBJS import loanOBJ
global mycursor
from datetime import date


db = mysql.connector.connect(
host='localhost',
user='Gohost',
passwd='AscaxAnya!1313',
database='loanSQL'
)
mycursor = db.cursor(buffered=True)

def main():
    loanList=[]
    loanNames=[]
    cont=1
    count=0
    while cont:
        var = input("Enter your command:").upper()
        with Switch(var) as case:
            if case("EXIT"):
                cont=0
            if case("CREATE"):
                create()

            if case('QUERY'):
                typ=input()
                quer=input()
                loanList.append(objectifier(query(typ,quer)[0]))
                print(loanList)
            if case('CALCULATE'):
                promiscuo(loanList,loanNames)
            if case.default:
                print("INPUT ERROR!!")
                continue

if __name__ == "__main__": 
