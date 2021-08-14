r1 = 00000000
r2 = 00000000
r3 = 00000000
r4 = 00000000
r5 = 00000000
r6 = 00000000
flags = 00000000
pc = 00000000
halted = False

while (not halted):
    code = input()
    code = str(code)
    opc = code[0:5]

    if opc = "00000" :
        add()
    elif opc == "00001":
        sub()
    elif opc == "00010":
        movimm()
    elif opc == "00011":
        movreg()
    elif opc == "00100":
        ld()
    elif opc == "00101":
        st()
    elif opc == "00110":
        mul()
    elif opc == "00111":
        div()
    elif opc == "01000":
        rtsf()
    elif opc == "01001":
        ltsf()
    elif opc == "01010":
        xor()
    elif opc == "01011":
        oor()
    elif opc == "01100":
        aand()
    elif opc == "01101":
        invert()
    elif opc == "01110":
        compare()
    elif opc == "01111":
        uncjmp()
    elif opc == "10000":
        jlt()
    elif opc == "10001":
        jgt()
    elif opc == "10010":
        je()
    elif opc == "10011":
        hlt()


