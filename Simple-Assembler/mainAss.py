# CO assignment by Vibhor Agarwal, Tejdeep Chippa and Pranav Bhaskar
# Description: This program is a simple 16bit assembler.

"""
Initialization of the assembler componenets
"""

RegisterTable = {
    "reg0":"000",
    "reg1":"001",
    "reg2":"010",
    "reg3":"011",
    "reg4":"100",
    "reg5":"101",
    "reg6":"110",
    "FLAGS": "111"}

OPcodeTable ={
    "add" :("00000","A") ,
    "sub" :("00001","A") ,
    "mov":(("00010","B"),("00011","C")),
    "ld":("00100","D"),
    "st":("00101","D"),
    "mul":("00110","A"),
    "div":("00111","C"),
    "rs":("01000","B"),
    "ls":("01001","B"),
    "xor":("01010","A"),
    "or":("01011","A"),
    "and":("01100","A"),
    "not":("01101","C"),
    "cmp":("01110","C"),
    "jmp":("01111","E"),
    "jlt":("10000","E"),
    "jgt":("10001","E"),
    "je":("10010","E"),
    "hlt":("10011","F"),
    "var":"variable"}


"""
below section contains the binary encoding tables
"""
binaryEncoding ={
"A":{
    "commandSize": 4,
    "opcode":5 ,
    "unused": 2 ,
    "reg1":3 ,
    "reg2":3 ,
    "reg3":3 },
"B":{
    "commandSize": 3,
    "opcode":5 ,
    "reg1":3 ,
    "immediate":8 },

"C":{
    "commandSize": 3,
    "opcode":5 ,
    "unused": 5 ,
    "reg1":3 ,
    "reg2":3 ,
    },

"D":{
    "commandSize": 3,
    "opcode":5 ,
    "unused": 3 ,
    "memoryAdress":8 },

"E":{
    "commandSize": 2,
    "opcode":5 ,
    "unused": 3 ,
    "memoryAdress":8 },

"var" :{
    "commandSize": 2,
}

}

"""
Flag Register Properties
"""
"""
Flag[0] = equal flag
Flag[1] = greater than flag
Flag[2] = less than flag
Flag[3] = overflow flag
"""
FLAG =[0,0,0,0]

#Following function intialise the Flag register to initial value 0
def InitialiseFlag(FLAG):
    FLAG[0] = 0
    FLAG[1] = 0
    FLAG[2] = 0
    FLAG[3] = 0


"""
use the following functions to set
the value of flag register
"""
def setEqualFlag(FLAG,val):
    FLAG[0] = val

def setGreaterFlag(FLAG,val):
    FLAG[1] = val

def setLessFlag(FLAG,val):
    FLAG[2] = val

def setOverflowFlag(FLAG,val):
    FLAG[3] = val

"""
use the following functions to get the
value of the flag registers
"""
def getEqualFlag(FLAG):
    return(FLAG[0])

def getGreaterFlag(FLAG):
    return(FLAG[1])

def getLessFlag(FLAG):
    return(FLAG[2])

def getOverflowFlag(FLAG):
    return(FLAG[3])


"""
some general variable required for the code flow are implemented below
"""
# counter counts the number of non empty lines executed so far
lineCounter = 0

"""
Input Part
In this part we take the input from the console
Since we are using split function extra white space in beginning
are ignored and the input is splitted into a list
the whole logic would be put in this while loop
"""
commandInput = input()
while(commandInput != "hlt"):
    # if blank line is entered then continue further
    if(commandInput==""):
        commandInput=input()
        continue

    else:
        lineCounter = lineCounter + 1

        commandList = commandInput.split()

        """
        the whole logic would be below
        """

        """
        below code handles the case for labels
        """
        if(commandList[0][-1]!= ":"):
            OPname = commandList[0]
        else:
            OPname= commandList[1]

        # Check whether the command is valid or not

        if(OPname in OPcodeTable):
            # logic if the command is valid is implemented below
            instructionCheck= OPcodeTable[OPname][0]
            # if opname is move then perform required check
            if(OPname != "mov"):
                insType= OPname[-1]
                # code for operations other than mov is implemented below



            else:
                # since mov has two data types, we need to check which it is referring to
                if(commandList[-1][0] == "$"):
                    insType= "B"
                else:
                    insType= "C"

            commandInput=input()

        else:
            # if the command is invalid then print the error message
            print("Invalid command")
            commandInput=input()
            continue


    

