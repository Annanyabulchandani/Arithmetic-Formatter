def arthemetic_arranger(lst, *args):
    if len(lst) > 5:
        return "Error: Too many problems"
    
    #print(lst)
    ls = []
    for i in lst:
        ls.append(i.split())
    #print(ls)

    num = []
    opr = []
    for l in ls:
        num.append(l[0])
        num.append(l[2])
        opr.append(l[1])
    #print(num)
    #print(opr)
    for j in opr:
        if j not in ['+', '-']:
            return "Error: Operator must be '+' or '-'"
    
    for i in num:
        if not (i.isdigit()):
            return "Error: Numbers must only contain digits"
        elif len(i) > 4:
            return "Error: Numbers cannot be more than four digits"
    
    j = 0
    sols = []
    for i in range(0, len(num), 2):
        if opr[j] == '+':
            s = int(num[i]) + int(num[i+1])
        else:
            s = int(num[i]) - int(num[i+1])
        j += 1
        sols.append(s)
    #print(sols)
    
    problem = ""
    frst_row = ""
    scnd_row = ""
    dashes = ""
    sol = ""
    a = 0
    for i in range(0, len(num), 2):
        space = max(len(num[i]), len(num[i+1])) + 2
        frst_row += num[i].rjust(space)
        dashes += '-' * space
        sol += str(sols[a]).rjust(space)
        a += 1
        if i != len(num) - 2:
            frst_row += ' ' * 4
            dashes += ' ' * 4
            sol += ' ' * 4
    
    for i in range(1, len(num), 2):
        space = max(len(num[i-1]), len(num[i])) + 1
        scnd_row += opr[i//2]
        scnd_row += num[i].rjust(space)
        if i != len(num) - 1:
            scnd_row += ' ' * 4
    
    if args:
        problem = '\n'.join((frst_row, scnd_row, dashes, sol))
    else:
        problem = '\n'.join((frst_row, scnd_row, dashes))
    
    print(problem)
