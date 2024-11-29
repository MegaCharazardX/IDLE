
def validateExp(_exp):
    _isValid = True

    #print(str(eval(("45*5"))))

    _tmpExp = _exp
    par_index_start = 0
    par_index_end = 0
    num_par_start = 0
    num_par_end = 0

    br_index_start = 1
    br_index_end = 0

    cur_index_start = 1
    cur_index_end = 0
    j = 0
    while j <= (len(_exp)):
        if _exp[j] == "(" :
            par_index_start = j 
            num_par_start += 1
        if _exp[j] == ")":
            par_index_end = j 
            num_par_end += 1
            _tmpExp_slice = exp[par_index_start  : par_index_end +1]
            #_tmpExp_eval = str(eval(_tmpExp_slice))
            #_tmpExp.replace(_tmpExp_slice,  str(eval(_tmpExp_slice)))
            var = _tmpExp_slice.replace(_tmpExp_slice,  str(eval(_tmpExp_slice)))
            tmplst = _tmpExp.split(_tmpExp_slice)
            tmplst.insert(1, f"*{var}")
            _tmpStr = ""
            for i in tmplst:
                _tmpStr += i
                print(i)
            print(_tmpStr)
            j += 1

    if num_par_start != num_par_end:
        _isValid = False

    print(par_index_start, par_index_end, num_par_start, num_par_end)         

    return _isValid


exp = "566{23(5(45*5)+3)-4}[5454-7]" #input("Enter your expression : ")

if validateExp(exp) == True: 
    print("Valid Expression")
else:
    print("Please Enter The Valid Expression.\n Eg., \n '566{23(5(45*5)+3)-4}[5454-7]'.")

"""while True :
    if "[" in exp and "]" not in exp :
        print("--Expression Not Valid--\n")
        continue

    if  "]" in exp and "[" not in exp :
        print("--Expression Not Valid--\n")
        continue
    
    if "{" in exp and "}" not in exp :
        print("--Expression Not Valid--\n")
        continue

    if  "}" in exp and "{" not in exp :
        print("--Expression Not Valid--\n")
        continue
    
    if "(" in exp and ")" not in exp :
        print("--Expression Not Valid--\n")
        continue

    if  ")" in exp and "(" not in exp :
        print("--Expression Not Valid--\n")
        continue

    if exp.isalpha() :
        print("--Expression Not Valid--\n")
        continue
    
    
    break






par_index_first = exp.find("(")
par_index_second = exp.find(")")
resut = exp[par_index_first + 1 : par_index_second]
eval_split = eval(resut)
replaced = exp.replace(resut, str(eval_split))
print(resut, eval_split, replaced)#, eval(replaced)
"""
"""lst = ""

if "(" in exp :
    if len(lst) == 0:
        par_index_first = exp.find("(")
        par_index_second = exp.find(")")
    else: 
        par_index_first = lst.find("(")
        par_index_second = lst.find(")")

    par_split = exp[par_index_first + 1 : par_index_second]
    eval_split = eval(par_split)
    if len(lst) == 0 :
        replaced = exp.replace(par_split, str(eval_split))
        if exp[par_index_first-1] != "-" or exp[par_index_first-1] != "+" or exp[par_index_first-1] != "*" or exp[par_index_first-1] != "/" or exp[par_index_first-1] != "%" :
            par_first = (replaced.replace("(", "*"))
            lst = par_first.replace(")", "")
        else :
            par_first = (replaced.replace("(", ""))
            lst = par_first.replace(")", "")
    else:
        replaced = lst.replace(par_split, str(eval_split))
        if exp[par_index_first-1] != "-" or exp[par_index_first-1] != "+" or exp[par_index_first-1] != "*" or exp[par_index_first-1] != "/" or exp[par_index_first-1] != "%" :
            par_first = (lst.replace("(", "*"))
            lst = par_first.replace(")", "")
        else :
            par_first = (lst.replace("(", ""))
            lst = par_first.replace(")", "")

if "{" in exp :
    if len(lst) == 0:
        cur_index_first = exp.find("{")
        cur_index_second = exp.find("}")
    else:
        cur_index_first = lst.find("{")
        cur_index_second = lst.find("}")

    cur_split = exp[cur_index_first + 1 : cur_index_second]
    eval_split = eval(cur_split)
    if len(lst) == 0 :
        replaced = exp.replace(cur_split, str(eval_split))
        if exp[cur_index_first-1] != "-" or exp[cur_index_first-1] != "+" or exp[cur_index_first-1] != "*" or exp[cur_index_first-1] != "/" or exp[cur_index_first-1] != "%" :
            curly_first = (replaced.replace("{", "*"))
            lst = curly_first.replace("}", "")
        else:
            curly_first = (replaced.replace("{", ""))
            lst = curly_first.replace("}", "")            
    else:
        replaced = lst.replace(cur_split, str(eval_split))
        if exp[cur_index_first-1] != "-" or exp[cur_index_first-1] != "+" or exp[cur_index_first-1] != "*" or exp[cur_index_first-1] != "/" or exp[cur_index_first-1] != "%" :
            curly_first = (lst.replace("{", "*"))
            lst = curly_first.replace("}", "")
        else: 
            curly_first = (lst.replace("{", ""))
            lst = curly_first.replace("}", "")      

if "[" in exp :
    if len(lst) == 0:
        br_index_first = exp.find("[")
        br_index_second = exp.find("]")
    else:
        br_index_first = lst.find("[")
        br_index_second = lst.find("]")
    br_split = exp[br_index_first + 1 : br_index_second]
    eval_split = eval(br_split)
    if len(lst) == 0 :
        replaced = exp.replace(br_split, str(eval_split))
        if exp[br_index_first-1] != "-" or exp[br_index_first-1] != "+" or exp[br_index_first-1] != "*" or exp[br_index_first-1] != "/" or exp[br_index_first-1] != "%" :
            bracket_first = (replaced.replace("[", "*"))
            lst = bracket_first.replace("]", "")
        else:
            bracket_first = (replaced.replace("[", "*"))
            lst = bracket_first.replace("]", "")
    else:
        ch = str(eval_split)
        replaced = lst.replace(br_split, ch)
        if exp[br_index_first-1] != "-" or exp[br_index_first-1] != "+" or exp[br_index_first-1] != "*" or exp[br_index_first-1] != "/" or exp[br_index_first-1] != "%" :
            bracket_first = (replaced.replace("[", "*"))
            lst = bracket_first.replace("]", "")
        else:
            bracket_first = (replaced.replace("[", ""))
            lst = bracket_first.replace("]", "")

print(eval(lst))
#result = eval(lst)
#print(result)"""
