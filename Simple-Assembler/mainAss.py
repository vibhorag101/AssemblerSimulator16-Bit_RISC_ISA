# CO assignment by Vibhor Agarwal, Tejdeep Chippa and Pranav Bhaskar
# Description: This program is a simple 16bit assembler.
from sys import stdin
"""
Initialization of the assembler componenets
"""

"""all the variables are implemented below
"""
FLAG = [0, 0, 0, 0]
# lineCounter used for assigning the value to the variable and count total instructions
lineCounter = 0
# errorLineCounter is used to tell which line is causing the error
errorLineCounter=0
errorFlag = False
mainList = []
labelDict= {}

RegisterTable = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111"}

OPcodeTable = {
    "add": ("00000", "A"),
    "sub": ("00001", "A"),
    "mov": (("00010", "B"), ("00011", "C")),
    "ld": ("00100", "D"),
    "st": ("00101", "D"),
    "mul": ("00110", "A"),
    "div": ("00111", "C"),
    "rs": ("01000", "B"),
    "ls": ("01001", "B"),
    "xor": ("01010", "A"),
    "or": ("01011", "A"),
    "and": ("01100", "A"),
    "not": ("01101", "C"),
    "cmp": ("01110", "C"),
    "jmp": ("01111", "E"),
    "jlt": ("10000", "E"),
    "jgt": ("10001", "E"),
    "je": ("10010", "E"),
    "hlt": ("10011", "F"),
    "var": "variable"}


"""
below section contains the binary encoding tables
"""
binaryEncoding = {
    "A": {
        "commandSize": 4,
        "opcode": 5,
        "unused": 2,
        "R1": 3,
        "R2": 3,
        "R3": 3},
    "B": {
        "commandSize": 3,
        "opcode": 5,
        "R1": 3,
        "immediate": 8},

    "C": {
        "commandSize": 3,
        "opcode": 5,
        "unused": 5,
        "R1": 3,
        "R2": 3,
    },

    "D": {
        "commandSize": 3,
        "opcode": 5,
        "unused": 3,
        "memoryAdress": 8},

    "E": {
        "commandSize": 2,
        "opcode": 5,
        "unused": 3,
        "memoryAdress": 8},

    "var": {
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


# Following function intialise the Flag register to initial value 0


def InitialiseFlag(FLAG):
    FLAG[0] = 0
    FLAG[1] = 0
    FLAG[2] = 0
    FLAG[3] = 0




"""
use the following functions to set
the value of flag register
"""


def setEqualFlag(FLAG, val):
    FLAG[0] = val


def setGreaterFlag(FLAG, val):
    FLAG[1] = val


def setLessFlag(FLAG, val):
    FLAG[2] = val


def setOverflowFlag(FLAG, val):
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
Type A functions are implemented here
"""


def add(reg1, reg2, reg3):
    opcode = OPcodeTable["add"][0]
    unused = "00"
    try:
        r1 = RegisterTable[reg1]
        r2 = RegisterTable[reg2]
        r3 = RegisterTable[reg3]
    except KeyError:
        print("Error in line "+str(errorLineCounter)+ " Invalid Register")
        exit()
    except:
        print("Error in line "+str(errorLineCounter)+" General Syntax error")
        exit()
    print(opcode+unused+r1+r2+r3)


def sub(reg1, reg2, reg3):
    opcode = OPcodeTable["sub"][0]
    unused = "00"
    try:
        r1 = RegisterTable[reg1]
        r2 = RegisterTable[reg2]
        r3 = RegisterTable[reg3]
    except KeyError:
        print("Error in line "+str(errorLineCounter)+ " Invalid Register")
        exit()
    except:
        print("Error in line "+str(errorLineCounter)+" General Syntax error")
        exit()
    
    print(opcode+unused+r1+r2+r3)


def mul(reg1, reg2, reg3):
    opcode = OPcodeTable["mul"][0]
    unused = "00"
    try:
        r1 = RegisterTable[reg1]
        r2 = RegisterTable[reg2]
        r3 = RegisterTable[reg3]
    except KeyError:
        print("Error in line "+str(errorLineCounter)+ " Invalid Register")
        exit()
    except:
        print("Error in line "+str(errorLineCounter)+" General Syntax error")
        exit()
    print(opcode+unused+r1+r2+r3)


def xor(reg1, reg2, reg3):
    opcode = OPcodeTable["xor"][0]
    unused = "00"
    try:
        r1 = RegisterTable[reg1]
        r2 = RegisterTable[reg2]
        r3 = RegisterTable[reg3]
    except KeyError:
        print("Error in line "+str(errorLineCounter)+ " Invalid Register")
        exit()
    except:
        print("Error in line "+str(errorLineCounter)+" General Syntax error")
        exit()
    print(opcode+unused+r1+r2+r3)


def doOR(reg1, reg2, reg3):
    opcode = OPcodeTable["or"][0]
    unused = "00"
    try:
        r1 = RegisterTable[reg1]
        r2 = RegisterTable[reg2]
        r3 = RegisterTable[reg3]
    except KeyError:
        print("Error in line "+str(errorLineCounter)+ " Invalid Register")
        exit()
    except:
        print("Error in line "+str(errorLineCounter)+" General Syntax error")
        exit()
    print(opcode+unused+r1+r2+r3)


def doAnd(reg1, reg2, reg3):
    opcode = OPcodeTable["and"][0]
    unused = "00"
    try:
        r1 = RegisterTable[reg1]
        r2 = RegisterTable[reg2]
        r3 = RegisterTable[reg3]
    except KeyError:
        print("Error in line "+str(errorLineCounter)+ " Invalid Register")
        exit()
    except:
        print("Error in line "+str(errorLineCounter)+" General Syntax error")
        exit()
    print(opcode+unused+r1+r2+r3)


"""
Type B instructions
"""


def mov(reg1, imm):
    opcode = OPcodeTable["mov"][0][0]
    r1 = RegisterTable[reg1]
    try:
        imm = bin(int(imm[1::]))[2:].zfill(8)
    except NameError:
        print("Error in line "+str(errorLineCounter)+ " Invalid Immediate")
        exit()
    except ValueError:
        print("Error in line "+str(errorLineCounter)+ " Invalid Immediate")
        exit()

    print(opcode+r1+imm)


def rs(reg1, imm):
    opcode = OPcodeTable["rs"][0][0]
    r1 = RegisterTable[reg1]
    try:
        imm = bin(int(imm[1::]))[2:].zfill(8)
    except NameError:
        print("Error in line "+str(errorLineCounter)+ " Invalid Immediate")
        exit()
    except ValueError:
        print("Error in line "+str(errorLineCounter)+ " Invalid Immediate")
        exit()
    print(opcode+r1+imm)


def ls(reg1, imm):
    opcode = OPcodeTable["ls"][0][0]
    r1 = RegisterTable[reg1]
    try:
        imm = bin(int(imm[1::]))[2:].zfill(8)
    except NameError:
        print("Error in line "+str(errorLineCounter)+ " Invalid Immediate")
        exit()
    except ValueError:
        print("Error in line "+str(errorLineCounter)+ " Invalid Immediate")
        exit()
    print(opcode+r1+imm)


"""
type C instructions
"""

def moveC(reg1, reg2):
    opcode= OPcodeTable["mov"][1][0]
    r1 = RegisterTable[reg1]
    r2 = RegisterTable[reg2]
    unused= "00000"
    print(opcode+unused+r1+r2)

def div(reg1,reg2):
    opcode= OPcodeTable["div"][0]
    r1 = RegisterTable[reg1]
    r2 = RegisterTable[reg2]
    unused= "00000"
    print(opcode+unused+r1+r2)

def doNot(reg1,reg2):
    opcode= OPcodeTable["not"][0]
    r1 = RegisterTable[reg1]
    r2 = RegisterTable[reg2]
    unused= "00000"
    print(opcode+unused+r1+r2)

def cmp(reg1,reg2):
    opcode= OPcodeTable["cmp"][0]
    r1 = RegisterTable[reg1]
    r2 = RegisterTable[reg2]
    unused= "00000"
    #TODO implement the comparison logic
    print(opcode+unused+r1+r2)


"""
type D instruction
"""
def load(reg1,var):
    opcode = OPcodeTable["ld"][0]
    r1 = RegisterTable[reg1]
    address = bin(var)[2::].zfill(8)
    print(opcode+r1+address)

def store(reg1,var):
    opcode = OPcodeTable["st"][0]
    r1 = RegisterTable[reg1]
    address = bin(var)[2::].zfill(8)
    print(opcode+r1+address)


"""
type E instructions
"""
#TODO fix the branch label TYPE_CHECKING

def jmp(var):
    opcode = OPcodeTable["jmp"][0]
    unused = "000"
    try:
        address = bin(var)[2::].zfill(8)
        print(opcode+unused+address)
    except KeyError:
        print("Error in line "+str(errorLineCounter)+" variable used without define")
    except:
        print("Error in line "+str(errorLineCounter)+" General Syntax error")

def jlt(var):
    opcode = OPcodeTable["jlt"][0]
    unused = "000"
    try:
        address = bin(var)[2::].zfill(8)
        print(opcode+unused+address)
    except KeyError:
        print("Error in line "+str(errorLineCounter)+" variable used without define")
    except:
        print("Error in line "+str(errorLineCounter)+" General Syntax error")


def jgt(var):
    opcode = OPcodeTable["jgt"][0]
    unused = "000"
    try:
        address = bin(var)[2::].zfill(8)
        print(opcode+unused+address)
    except KeyError:
        print("Error in line "+str(errorLineCounter)+" variable used without define")
    except:
        print("Error in line "+str(errorLineCounter)+" General Syntax error")

def je(var):
    opcode = OPcodeTable["je"][0]
    unused = "000"
    try:
        address = bin(var)[2::].zfill(8)
        print(opcode+unused+address)
    except KeyError:
        print("Error in line "+str(errorLineCounter)+" variable used without define")
    except:
        print("Error in line "+str(errorLineCounter)+" General Syntax error")



"""
some general variable required for the code flow are implemented below
"""
# this functions checks the argument length given
def checkArgLength(opType,commandList,label):
    checkLength = len(commandList)
    if(label == True):
        if(checkLength != binaryEncoding[opType]["commandSize"]+1):
            print("Error in line: "+errorLineCounter+" Invalid number of arguments for type",opType,"operation")
            exit()
    else:
        if(checkLength != binaryEncoding[opType]["commandSize"]):
            print("Error in line: "+str(errorLineCounter)+" Invalid number of arguments for type",opType,"operation")
            exit()

    

"""
Input Part
In this part we take the input from the console
Since we are using split function extra white space in beginning
are ignored and the input is splitted into a list
the whole logic would be put in this while loop
"""

# while(commandInput != "hlt"):
for commandInput in stdin:
    if(commandInput != ""):
        commandInput=commandInput.strip()
        if(commandInput==""):
            continue
        command= commandInput.split()
        mainList.append(command)
        if("var" not in command):
            if(command[0][-1] == ":"):
                labelDict[command[0][:-1]] = lineCounter
            lineCounter += 1
    else:
        break
#REVIEW
"""
An additional input is created
if we have reached the end of file then an eoferror is raised which
is catched
But if there are pending commands after first halt then no such error
is raised indicating halt is not the last statement
Although when running without automated testing we need an additional enter
"""

if(lineCounter >256):
    print("instruction count exceeds 256")
    exit()

"""
following code assign the value to the variable
"""
varDict= {}
varDict = labelDict.copy()
varErrorCounter=0
for varList in mainList:
    label = False
    labelCorrect = 0
    """
    below code handles the case for labels
    """
    if(varList[0][-1] != ":"):
        OPname = varList[0]
    else:
        try:
            OPname = varList[1]

            labelCorrect=1
        except IndexError:
            print("Error in line "+str(varErrorCounter)+" Invalid number of arguments for label or variable")
            exit()
    
    if(OPname == "var"):
        try:
            varDict[varList[1+labelCorrect]] = lineCounter
            lineCounter=lineCounter+1
        except IndexError:
            print("Error in line "+str(varErrorCounter)+" Invalid number of arguments for variable")
            exit()
    varErrorCounter=varErrorCounter+1
#NOTE
# below variable counts the line to give out the error line number


for commandList in mainList:
    
    lineCounter = lineCounter + 1
    # below checks the label
    label = False
    labelCorrect = 0
    """
    below code handles the case for labels
    """
    if(commandList[0][-1] != ":"):
        OPname = commandList[0]
    else:
        try:
            OPname = commandList[1]
            label = True
            labelCorrect = 1
        except IndexError:
            print("Error in line "+str(errorLineCounter)+" incomplete arguments after label")
            exit()
        except:
            print("Error in line "+str(errorLineCounter)+" General Syntax error")
            exit()

    """
    the whole logic would be below
    """
    # Check whether the command is valid or not

    if(OPname in OPcodeTable):
        # logic if the command is valid is implemented below
        instructionCheck = OPcodeTable[OPname][0]
        # if opname is move then perform required check
        if(OPname != "mov"):
            insType = OPcodeTable[OPname][-1]
            # REVIEW possible error for var
            # TODO add the type specific length check
            # TODO var instructions
            #TODO create the errors at various parts

            # code for operations other than mov is implemented below
            """
            the following are the type A operations
            """
            
            if(OPname == "add"):
                checkArgLength("A",commandList,label)
                add(commandList[1+labelCorrect], commandList[2 +
                    labelCorrect], commandList[3+labelCorrect])
            elif(OPname == "sub"):
                checkArgLength("A",commandList,label)
                sub(commandList[1+labelCorrect], commandList[2 +
                    labelCorrect], commandList[3+labelCorrect])
            elif(OPname == "mul"):
                checkArgLength("A",commandList,label)
                mul(commandList[1+labelCorrect], commandList[2 +
                    labelCorrect], commandList[3+labelCorrect])
            elif(OPname == "xor"):
                checkArgLength("A",commandList,label)
                xor(commandList[1+labelCorrect], commandList[2 +
                    labelCorrect], commandList[3+labelCorrect])
            elif(OPname == "or"):
                checkArgLength("A",commandList,label)
                doOR(commandList[1+labelCorrect], commandList[2 +
                        labelCorrect], commandList[3+labelCorrect])
            elif(OPname == "and"):
                checkArgLength("A",commandList,label)
                doAnd(commandList[1+labelCorrect], commandList[2 +
                        labelCorrect], commandList[3+labelCorrect])

            # type B instructions are implemented below
            elif (OPname == "rs"):
                checkArgLength("B",commandList,label)
                rs(commandList[1+labelCorrect],
                    commandList[2+labelCorrect])

            elif (OPname == "ls"):
                checkArgLength("B",commandList,label)
                ls(commandList[1+labelCorrect],
                    commandList[2+labelCorrect])
            
            #type C instructions are implemented below
            elif(OPname == "div"):
                checkArgLength("C",commandList,label)
                div(commandList[1+labelCorrect],
                commandList[2+labelCorrect])
            
            elif(OPname == "not"):
                checkArgLength("C",commandList,label)
                doNot(commandList[1+labelCorrect],
                commandList[2+labelCorrect])
            
            elif(OPname == "cmp"):
                checkArgLength("C",commandList,label)
                cmp(commandList[1+labelCorrect],
                commandList[2+labelCorrect])

            # type D instructions are implemented below

            elif(OPname == "ld"):
                checkArgLength("D",commandList,label)
                try:
                    load(commandList[1+labelCorrect],
                varDict[commandList[2+labelCorrect]])
                except KeyError:
                    print("Error in line "+str(errorLineCounter)+" variable used without define")
                    exit()
            elif(OPname == "st"):
                checkArgLength("D",commandList,label)
                try:
                    store(commandList[1+labelCorrect],
                    varDict[commandList[2+labelCorrect]])
                except KeyError:
                    print("Error in line "+str(errorLineCounter)+" variable used without define")
                    exit()
            

            # type E instructions are implemented below
            elif(OPname == "jmp"):
                checkArgLength("E",commandList,label)
                try:
                    jmp(varDict[commandList[1+labelCorrect]])
                except KeyError:
                    print("Error in line "+str(errorLineCounter)+" variable used without define")
                    exit()

            elif(OPname == "jlt"):
                checkArgLength("E",commandList,label)
                try:
                    jlt(varDict[commandList[1+labelCorrect]])
                except KeyError:
                    print("Error in line "+str(errorLineCounter)+" variable used without define")
                    exit()

            elif(OPname == "jgt"):
                checkArgLength("E",commandList,label)
                try:
                    jgt(varDict[commandList[1+labelCorrect]])
                except KeyError:
                    print("Error in line "+str(errorLineCounter)+" variable used without define")
                    exit()
                
            elif(OPname == "je"):
                checkArgLength("E",commandList,label)
                try:
                    je(varDict[commandList[1+labelCorrect]])
                except KeyError:
                    print("Error in line "+str(errorLineCounter)+" variable used without define")
                    exit()


        else:
            # since mov has two data types, we need to check which it is referring to
            if(commandList[-1][0] == "$"):
                insType = "B"
                checkArgLength(insType,commandList,label)
                mov(commandList[1+labelCorrect],
                    commandList[2+labelCorrect])
            else:
                insType = "C"
                checkArgLength(insType,commandList,label)
                moveC(commandList[1+labelCorrect],
                commandList[2+labelCorrect])


    else:
        # if the command is invalid then print the error message
        print("Error in line "+str(errorLineCounter)+" Invalid command")
        exit()
    errorLineCounter=errorLineCounter+1

print("1001100000000000")

#TODO error line counter