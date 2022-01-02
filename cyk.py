def check_cnf_form(cfg):
    count = 0
    val = []
    for key,value in cfg.items():
        val += key
        val += value
    # checking cnf form
    for item in val:
        if ((len(item) <=2 and item.isupper()) or (len(item)==1) and item.islower()):
            count += 1
    return count == len(val)

# fungsi algoritma cyk
def cyk(cfg,string):
    n = len(string)
    table = [[0] * n for i in range(n)]
# fill first row
    temp = []
    strsplit = [item for item in string]
    for index in range(n):
        for key,value in cfg.items():
            for i in range(len(value)):
                if cfg[key][i] == strsplit[index]:
                    temp.append(key)
        table[0][index] = temp
        temp = []
# fill second row
    concate = []
    first = []
    second = []
    for i in range(n-1):
        first = table[0][i]
        second = table[0][i+1]
# remove brackets
        r1 = [i[0] for i in first]
        r2 = [i[0] for i in second]
# concate
        for j in range(len(r1)):
            for k in range(len(r2)):
                concate.append(r1[j]+r2[k])
        for key,value in cfg.items():
            for index in range(len(value)):
                for l in range(len(concate)):
                    if cfg[key][index] == concate[l]:
                        temp.append(key)
        table[1][i] = temp
        temp = []
        concate = []
# fill the rest
    l = 2
    x = 2
    concate = []
    pod1 = []
    pod2 = []
    temp = []
    
    skey = []
    for i in range(n-2):
        m = l-1
        for j in range(n-(i+2)):
            for k in range(l):
                pod1 = table[k][j]
                pod2 = table[m-k][j+k+1]
        # removing bracket
                r1 = [i[0] for i in pod1]
                r2 = [i[0] for i in pod2]
        # concate
                for ir1 in range(len(r1)):
                    for ir2 in range(len(r2)):
                        temp.append(r1[ir1]+r2[ir2])
                for key,value in cfg.items():
                    for p in range(len(value)):
                        for index in range(len(temp)):
                            if cfg[key][p] == temp[index]:
                                    skey.append(key)

                temp = []
            table[x][j] = skey
            skey = []
        l += 1
        x += 1
    # get the first key
    key_list = list(cfg.keys())
    first_key = key_list[0]
    return first_key in table[n-1][0], table