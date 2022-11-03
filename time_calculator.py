def daynightconverter(AMPM):
    if AMPM == "AM":
        AMPM = "PM"
    else:
        AMPM = "AM"
    return(AMPM)


def datecal(newhour, newmin, AMPM, hours):
    if AMPM == "AM":
        starter = 0
    else:
        starter = 1

    d_option = starter + hours//12
    c_option = hours//12

    if c_option % 2 == 1:
        AMPM = daynightconverter(AMPM)

    if newhour == 0:
        newhour = 12

    newtime = str(newhour) + ":" + str(newmin)
    if d_option == 0:
        return(str(newtime), AMPM, "")

    elif d_option == 1:
        return(str(newtime), AMPM, "")

    elif d_option == 2 or d_option == 3:
        return(str(newtime), AMPM, "(next day)")

    else:
        nodays = d_option//2
        return(str(newtime), AMPM, ("("+str(nodays)+" days later)"))


def daycal(date, day):
    w_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    index = w_list.index(day)

    if date == "(next day)":
        nodays = 1
    else:
        list = date.split()
        nodays = int(list[0].translate({ord('('): None}))

    index += nodays
    i = index % 7
    return(w_list[i])


def cal(start, duration, AMPM, day):
    starthour = int(start[0])
    startmin = int(start[1])
    durationhour = int(duration[0])
    durationmin = int(duration[1])

    newmin = startmin + durationmin
    if newmin > 60:
        newmin -= 60
        durationhour += 1

    if newmin < 10:
        newmin = "0" + str(newmin)

    hour = starthour + durationhour
    newhour = hour % 12

    if day == "":
        newtime, AMPM, date = datecal(newhour, newmin, AMPM, hour)
        if date == "":
            return(newtime + " " + AMPM)
        else:
            return(newtime + " " + AMPM + " " + date)

    else:
        day = day.lower()
        day = day.capitalize()
        newtime, AMPM, date = datecal(newhour, newmin, AMPM, hour)
        if date == "":
            return(newtime + " " + AMPM + ", " + day)
        else:
            day = daycal(date, day)
            return(newtime + " " + AMPM + ", " + day + " " + date)


def add_time(start, duration, day=""):

    sstart = start.split()
    ssstart = sstart[0].split(":")
    AMPM = sstart[1]
    sduration = duration.split(":")
    newtime = cal(ssstart, sduration, AMPM, day)

    return newtime


print(add_time("11:59 PM", "24:05"))
