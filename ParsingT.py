## this is a representation for the parse table used to parse input string 
import pandas as pd
terminal_expr=['num','x','+','-','*','/','^','(',')','$']
#exp=>E exp'=>N term=>T term'=>N  Factor=>F Factor'=>M COMPOP=>C OPERAND=>O Z=>endstate badl (epi) 
nonterminal_expr=['E','N','T','W','F','M','C','O']
DF = pd.DataFrame(index=["EXP", "EXP'", "TERM", "TERM'", "FACTOR"],columns=["+", "-", "*", "/", "^","(",")", "num","x","$"])
DF["("]["EXP"] = 1
DF["num"]["EXP"] = 1
DF["x"]["EXP"] = 1
#######
DF["+"]["EXP'"] = 2
DF["-"]["EXP'"] = 3
DF[")"]["EXP'"] = 4
DF["$"]["EXP'"] = 4
#######
DF["("]["TERM"] = 5
DF["num"]["TERM"] = 5
DF["x"]["TERM"] = 5
#######
DF["+"]["TERM'"] = 8
DF["-"]["TERM'"] = 8
DF["*"]["TERM'"] = 6
DF["/"]["TERM'"] = 7
DF["^"]["TERM'"] = 9
DF[")"]["TERM'"] = 8
DF["$"]["TERM'"] = 8
#######
DF["x"]["FACTOR"] = 10
DF["num"]["FACTOR"] = 11
DF["-"]["FACTOR"] = 12
DF["("]["FACTOR"] = 13
# ########
# DF["^"]["FACTOR'"] = 14
# DF[")"]["FACTOR'"] = 15
# DF["$"]["FACTOR'"] = 15

# #######
# DF["+"]["P"] = 16
# DF["-"]["P"] = 17
# DF["*"]["P"] = 12
# DF["("]["P"] = 18
# DF["num"]["P"] = 19
# DF["x"]["P"] = 20
# ###############
# DF["num"]["N"] = 21 

print(DF)


def ruletranslation(num):
    arr=[0
         ,"TERM EXP'"
         ,"+ TERM EXP'"
         ,"- TERM EXP'"
         ,"EPI"
         ,"FACTOR TERM'"
         ,"* FACTOR TERM'"
         ,"/ FACTOR TERM'"
         ,"EPI"
         ,"^ FACTOR TERM'"
         , "x"
         , "num"
         , "- FACTOR"
         , "( EXP )"
       ]
    return -1 if pd.isna(num) else arr[num]
# for i in range (1,15):
#     print(i,ruletranslation(i))
def parsingTable(row,col):
    return DF[col][row]

#print(ruletranslation(DF["x"]["OPERAND"]))

