# CO assignment by Vibhor Agarwal, Tejdeep Chippa and Pranav Bhaskar
# Description: This program is a simple 16bit assembler.

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
    "hlt":("10011","F")}

