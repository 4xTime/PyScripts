import random
import string

#23
Nick1 = ['Fa','Val','Tls','Zea','Dac','Lan','Dkro','Kol','Zir','Tar','Var'
,'Sard','Torn','Alad','Ccald','Vlad','Pow','Dtre','Doc','Mer','For','Ker','COS','Xx']
#23
Nick2 = ['sa','aw','we','hy','rcv','err1','rorr1','clas','sed','sx','eq','oip','.xyz','lpyt'
,'PASw','lq24w','ctr12','der','tor','con','kon','xX','PL','Fer']

#23
City = ['New York','Chicago','Los Angeles','Houston','Phoenix','Philadelphia','Austin','Jacksonville'
'San Francisco','Seattle','Oklahoma City','Boston','Las Vegas','Detroit','Albuquerque','Milwaukee','Atlanta'
,'Miami','Orlando','Oakland','Minneapolis','Cleveland',' Indianapolis','Colorado Springs','Tampa']

def GenerateRandomDATA(amount:int,PathName:str):
    Spaces = " "
    with open(PathName,'w') as File:
        if PathName.find(".csv") != -1:
            Spaces = ","
            File.write('id'+','+'Nickname'+','+'age'+','+'City')
            File.write('\n')
        else:
            pass
        for x in range(amount):
            File.write(
                str(x)
                +Spaces+
                Nick1[random.randint(0,23)]+Nick2[random.randint(0,23)]
                +Spaces+
                str(random.randint(18,80))
                +Spaces+
                City[random.randint(0,23)]
            )
            File.write('\n')
    File.close()
    return 1

def GenerateRandomChars(amount:int):
    with open("RandomChars.txt",'w') as File:
        for x in range(amount):
            File.write(chr(random.randint(33,127)))
            if random.randint(0,30) == random.randint(0,30):
                File.write('\n')
        File.close()
    return 1


print("-------------------------------------------")
print("1: Random characters")
print("2: Random DATA (id,nicknames,age,city)")
Answer = int(input("->"))
print("--------------------------------------------")


if Answer == 1:
    print("How much characters do you want")
    Answer = int(input("->"))
    GenerateRandomChars(Answer)
    print("DONE!")
if Answer == 2:
    print("How much data do you want")
    HowMuchData = int(input("->"))
    print("What name and extansion do you want (for example DATA.csv)")
    print("you can change path to file (example C:\Users\myuser\DATA.csv)")
    PathName = input("->")
    GenerateRandomDATA(HowMuchData,PathName)