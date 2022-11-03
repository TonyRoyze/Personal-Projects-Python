# fname = input('Enter file name : ')
showname = input('Enter show name : ')
sno = input('Enter season number :')
epno = input('Enter episode number :')
epname = input('Enter episode name :')
res = input('Enter resolution :')

# pos1 = fname.find("E")
# pos2 = fname.find("480p")

# pos1 = pos1 + 4
# pos2 = pos2 - 1
# print(fname)
# fname = fname[pos1:pos2]
# fname = fname.replace(' ', ".")
# fname = fname.lower()
# print(fname)

epname = epname.replace(' ', ".")
epname = epname.lower()
print(epname)

# sname = "game.of.thrones."
showname = showname.replace(' ', ".")
showname = showname.lower()
print(showname)

ename = "px264-MLWBD.com"

x = int(sno)
if x < 10:
    sno = "s0" + sno + "."
else:
    sno = "s" + sno + "."
y = int(epno)
if y < 10:
    epno = "e0" + epno + "."
else:
    epno = "e" + epno + "."

nname = showname + "." + sno + epno + epname + "." + res + ename
nname = nname.strip()
print(nname)
