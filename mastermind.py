import random
def tacM(a,b):
    brojac=0
    c = []
    d = []
    for i in b:d.append(i)

    for i in range(len(a)):
        if(a[i]==b[i]):
            brojac+=1
            d[i] = ""
        else:c.append(a[i])
    return [brojac,c,d]
def netM(a,b):
    brojac = 0
    for i in a:
        if(i in b):
            b[b.index(i)] = ""
            brojac+=1
    return brojac

def main():
    print("mastermind")
    moja = ["","","",""]
    pob = ["","","",""]
    znakovi = ["crvena","plava","zelena","zuta","ljubicasta"]
    for i in range(len(pob)):
        pob[i] = znakovi[random.randint(0,4)]
    pobeda = False
    korak = 0
    while (pobeda == False and korak<6):
        print("unesi svoju kombinaciju:")
        for i in range(len(moja)):
            moja[i] = input("unesi "+str(i)+". znak:")
        if(moja==pob):pobeda = True
        else:
            tacnost1 = []
            tacnost2 = []
            for i in range(tacM(moja,pob)[0]):tacnost1.append("#")

            for i in range(netM(tacM(moja,pob)[1],tacM(moja,pob)[2])):tacnost2.append("@")
            print("{0}{1}".format(tacnost1,tacnost2))
            korak+=1
    if(pobeda==True):print("pobedio si")
    else:print("luzeru")

main()