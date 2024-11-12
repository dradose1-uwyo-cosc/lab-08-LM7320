# Luke Jackson
# UWYO COSC 1010
# Submission Date 11/12/24
# HW 04
# Lab Section:14
# Sources, people worked with, help given to:
# your
# comments
# here


from pathlib import Path
path = Path('prompt.txt')
contents = path.read_text()

pairs = contents.splitlines("\t")
while len(pairs) != 0:
    print_li = []
    pair  = [1]
    pair[0] = pairs[0]
    par = pair[0].split(" ")
    #print(f"par is {par}")
    while len(pair) != 0:
        p_p = [1, 2]
        pa = par[0].split(":")
        #print(f"pa is {pa}")
        if "\n" in pa[1]:
            p_p[0] = pa[0]
            pp = (pa[1].split("\n"))
            p_p[1] = pp[0]
        else:
            p_p[0] = pa[0]
            p_p[1] = pa[1]
        #print(f"p_p is {p_p}")
        #print(f"p_p int = {int(p_p[1])}")
        while True:
            if p_p[0] == "w":
                string_val = " "*int(p_p[1])
                print_li.append(string_val)
                #print(f"w string with {int(p_p[1])} is {string_val} !!")
            elif p_p[0] == "*":
                string_val = "*"*int(p_p[1])
                print_li.append(string_val)
                #print(f"* string with {int(p_p[1])} is {string_val}")
            del par[0]
            break
        if len(par) == 0:
            break
        else:
            continue
    print(print_li)
    del pairs[0]
    continue



