from cyk import check_cnf_form,cyk

cfg = {
    "U":["AB"],
    "A":["CD","CF"],
    "B":["c","EB"],
    "C":["a"],
    "D":["b"],
    "E":["c"],
    "F":["AD"]
}
string = 'aaabbbcc'
check_cnf = check_cnf_form(cfg)

if check_cnf:
    result,map = cyk(cfg,string)
    print('-------------------------------------------')
    print(f'can string derived from cfg ? {result}')
    print('-------------------------------------------')
    for i in map:
        print(i)
    print('-------------------------------------------')
