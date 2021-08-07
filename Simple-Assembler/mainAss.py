# CO assignment by Vibhor Agarwal, Tejdeep Chippa and Pranav Bhaskar
# Description: This program is a simple 16bit assembler.

"""
Initialization of the assembler componenets
"""

RegisterTable = {"R0":"000",
    "R1":"001",
    "R2":"010",
    "R3":"011",
    "R4":"100",
    "R5":"101",
    "R6":"110",
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
        continue

    commandList = input.split()

    """
    the whole logic would be below
    """
    OPname = commandList[0]

    # Check whether the command is valid or not

    if(OPname in OPcodeTable):
        # logic if the command is valid is implemented below
        print()

    else:
        # if the command is invalid then print the error message
        print("Invalid command")
        continue







    commandInput=input()

