#this is the main way to validate the input user has entered 
# I have decided to build an ll1 grammar and use this grammar to parse user input
# this was beneficial to the user as he/ she can view where she/he was wrong while writing input

import ParsingT
import re
def token(x):
    tokens =list(list())
    x+="_"
    xsize=len(x)
    i=0
    print(x)
    while(i<xsize):
        if (x[i]== 'x'):
            tokens.append(['x','x'])
            i+=1
        elif (x[i].isnumeric()):
            t=""
            while(i<xsize):
                if (x[i].isnumeric()):
                    t+=str(x[i])
                    i+=1
                else:
                    tokens.append(['num',t])
                    break
        elif (x[i]== '(') :
                tokens.append(['(','('])
                i+=1
        elif (x[i]== ')') :
                tokens.append([')',')'])
                i+=1
        elif (x[i]== '-') :
                tokens.append(['-','-'])
                i+=1
        elif (x[i]== '+') :
                tokens.append(['+','+'])
                i+=1
        elif (x[i]== '/') :
                tokens.append(['/','/'])
                i+=1
        elif (x[i] == '*') :
                tokens.append(['*','*'])
                i+=1
        elif (x[i]== '^') :
                tokens.append(['^','^'])
                i+=1
        elif(x[i]=='_'):
                break
        else:
                return ["zzz",i] 
    return tokens

print(token("014514*x*+-/^365746"))
def checkForNumbers(inputstring):
    try:
        val = float(inputstring)
        return True
    except ValueError:
        return False

def checkForValidity(inputstring):
     intokenlist=token(inputstring)
     if intokenlist[0]==f"zzz":
           return "refused",inputstring[:intokenlist[1]]
     intokenlist.append("$")
     intokenlist.reverse()  
     currstate="EXP"
     nextstate=None
     statelist=["$","EXP"]
     rightlist=""
     tmp=""
     while True:
         
         if len(statelist)==1 and len(intokenlist)==1 and statelist[0]=="$" and intokenlist[0]=="$" :
             return "accepted",rightlist
         tupeoftokenizer=intokenlist[-1]
         typeofstart=tupeoftokenizer[0] 
         currstate=statelist.pop()
         if currstate==typeofstart:
             tmp=tupeoftokenizer[1] 
             rightlist+=tmp
             intokenlist.pop()
             continue
         nextstate=ParsingT.ruletranslation(ParsingT.parsingTable(currstate,typeofstart))
         if nextstate=="EPI":
              print(statelist)
              continue
         if nextstate==-1:
              print(currstate)
              return "refused",rightlist
         templist=nextstate.split(" ")
         templist.reverse()
         for i in range(len(templist)):
             statelist.append(templist[i])
         templist.reverse()
         templist.reverse()
         print(statelist)
         print("right",rightlist)
         print(intokenlist)
         i+=1

