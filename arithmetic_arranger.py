def arithmetic_arranger(problems, tocal=False):
    lol = []  # list of lists
    l1l = []  # list of line1
    l2l = []  # list of line2
    l3l = []  # list of line3
    l4l = []  # list of line4
    for problem in problems:  # iterating through the list
        # splitting the string at the white spaces
        li = list(problem.split(" "))
        lol.append(li)

    cont, error = errorhandling(lol, problems)

    if cont is True:
        for li in lol:
            if len(li[0]) > len(li[2]):
                dif = len(li[0]) - len(li[2])
                dif += 1
                line1 = "  " + li[0]
                line2 = li[1] + " "*dif + li[2]
                line3 = "-" * (len(li[0])+2)
                # making a list of lines
                l1l.append(line1)
                l2l.append(line2)
                l3l.append(line3)

                if tocal is True:
                    sum = cal(int(li[0]), int(li[2]), li[1])
                    sum = str(sum)
                    if len(sum) > len(li[0]):
                        line4 = " " + sum
                    else:
                        line4 = " "*2 + sum
                    l4l.append(line4)

            else:
                dif = len(li[2]) - len(li[0])
                line1 = "  " + " "*dif + li[0]
                line2 = li[1] + " " + li[2]
                line3 = "-" * (len(li[2])+2)
                # making a list of lines
                l1l.append(line1)
                l2l.append(line2)
                l3l.append(line3)
                if tocal is True:
                    sum = cal(int(li[0]), int(li[2]), li[1])
                    sum = str(sum)
                    if len(sum) > len(li[2]):
                        line4 = " " + sum
                    else:
                        line4 = " "*2 + sum
                    l4l.append(line4)

        soe1 = ""
        i = 1
        for item in l1l:
            soe1 += item
            if len(l1l) > i:
                soe1 += " "*4
            i += 1

        soe2 = ""
        i = 1
        for item in l2l:
            soe2 += item
            if len(l2l) > i:
                soe2 += " "*4
            i += 1

        soe3 = ""
        i = 1
        for item in l3l:
            soe3 += item
            if len(l3l) > i:
                soe3 += " "*4
            i += 1

        if tocal is True:
            soe4 = ""
            i = 1
            for item in l4l:
                soe4 += item
                if len(l4l) > i:
                    soe4 += " "*4
                i += 1

            return(soe1+"\n"+soe2+"\n"+soe3+"\n"+soe4)
        else:
            return(soe1+"\n"+soe2+"\n"+soe3)

    else:
        return error


def cal(x, y, op):
    if op == "+":
        cal = x + y
    elif op == "-":
        cal = x - y
    else:
        return 0

    return cal


def errorhandling(lol, problems):
    for i in lol:
        try:
            cstr1 = int(lol[lol.index(i)][0])
            cstr2 = int(lol[lol.index(i)][2])

        except(TypeError, ValueError):
            cstr1 = "Error"
            cstr2 = "Error"

        if len(problems) > 5:
            return(False, "Error: Too many problems.")

        elif lol[lol.index(i)][1] != "+" and lol[lol.index(i)][1] != "-":
            return(False, "Error: Operator must be '+' or '-'.")

        elif cstr1 == "Error" or cstr2 == "Error":
            return(False, "Error: Numbers must only contain digits.")

        elif cstr1 > 9999 or cstr2 > 9999:
            return(False, "Error: Numbers cannot be more than four digits.")

    return(True, "None")


print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'], True))
