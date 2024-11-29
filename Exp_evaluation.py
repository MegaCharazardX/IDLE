while True :
    exp = input("Enter your expression : ")
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



# par_index_first = exp.find("(")
# par_index_second = exp.find(")")
# resut = exp[par_index_first + 1 : par_index_second]
# fun = eval(resut)
# fun1 = exp.replace(resut, str(fun))
# print(resut, fun, fun1)#, eval(fun1)

lst = ""

if "(" in exp :
    if len(lst) == 0:
        par_index_first = exp.find("(")
        par_index_second = exp.find(")")
    else: 
        par_index_first = lst.find("(")
        par_index_second = lst.find(")")

    resut = exp[par_index_first + 1 : par_index_second]
    fun = eval(resut)
    if len(lst) == 0 :
        fun1 = exp.replace(resut, str(fun))
        if exp[par_index_first-1] != "-" or exp[par_index_first-1] != "+" or exp[par_index_first-1] != "*" or exp[par_index_first-1] != "/" or exp[par_index_first-1] != "%" :
            par_first = (fun1.replace("(", "*"))
            lst = par_first.replace(")", "")
        else :
            par_first = (fun1.replace("(", ""))
            lst = par_first.replace(")", "")
    else:
        fun1 = lst.replace(resut, str(fun))
        if exp[par_index_first-1] != "-" or exp[par_index_first-1] != "+" or exp[par_index_first-1] != "*" or exp[par_index_first-1] != "/" or exp[par_index_first-1] != "%" :
            par_first = (lst.replace("(", "*"))
            lst = par_first.replace(")", "")
        else :
            par_first = (lst.replace("(", ""))
            lst = par_first.replace(")", "")

if "{" in exp :
    if len(lst) == 0:
        par_index_first = exp.find("{")
        par_index_second = exp.find("}")
    else:
        par_index_first = lst.find("{")
        par_index_second = lst.find("}")
    resut = exp[par_index_first + 1 : par_index_second]
    fun = eval(resut)
    if len(lst) == 0 :
        fun1 = exp.replace(resut, str(fun))
        if exp[par_index_first-1] != "-" or exp[par_index_first-1] != "+" or exp[par_index_first-1] != "*" or exp[par_index_first-1] != "/" or exp[par_index_first-1] != "%" :
            curly_first = (fun1.replace("{", "*"))
            lst = curly_first.replace("}", "")
        else:
            curly_first = (fun1.replace("{", ""))
            lst = curly_first.replace("}", "")            
    else:
        fun1 = lst.replace(resut, str(fun))
        if exp[par_index_first-1] != "-" or exp[par_index_first-1] != "+" or exp[par_index_first-1] != "*" or exp[par_index_first-1] != "/" or exp[par_index_first-1] != "%" :
            curly_first = (lst.replace("{", "*"))
            lst = curly_first.replace("}", "")
        else: 
            curly_first = (lst.replace("{", ""))
            lst = curly_first.replace("}", "")      

if "[" in exp :
    if len(lst) == 0:
        par_index_first = exp.find("[")
        par_index_second = exp.find("]")
    else:
        par_index_first = lst.find("[")
        par_index_second = lst.find("]")
    resut = exp[par_index_first + 1 : par_index_second]
    fun = eval(resut)
    if len(lst) == 0 :
        fun1 = exp.replace(resut, str(fun))
        if exp[par_index_first-1] != "-" or exp[par_index_first-1] != "+" or exp[par_index_first-1] != "*" or exp[par_index_first-1] != "/" or exp[par_index_first-1] != "%" :
            bracket_first = (fun1.replace("[", "*"))
            lst = bracket_first.replace("]", "")
        else:
            bracket_first = (fun1.replace("[", "*"))
            lst = bracket_first.replace("]", "")
    else:
        ch = str(fun)
        fun1 = lst.replace(resut, ch)
        if exp[par_index_first-1] != "-" or exp[par_index_first-1] != "+" or exp[par_index_first-1] != "*" or exp[par_index_first-1] != "/" or exp[par_index_first-1] != "%" :
            bracket_first = (fun1.replace("[", "*"))
            lst = bracket_first.replace("]", "")
        else:
            bracket_first = (fun1.replace("[", ""))
            lst = bracket_first.replace("]", "")

print(eval(lst))
#result = eval(lst)
#print(result)
