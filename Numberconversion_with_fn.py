print(" This program is for number conversion")
print(" =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Type'BD' for Binary-Decimal\nType'BH' for Binary-hexadecimal\nType'BO' for Binary-Octal")
print("Type'DB' for Decimal-Binary\nType'DH' for Decimal-hexadecimal\nType'DO' for Decimal-Octal")
print("Type'OB' for Octal-Binary\nType'OH' for Octal-hexadecimal\nType'OD' for Octal-Decimal")
print("Type'HB' for hexadecimal-Binary\nType'HD' for hexadecimal-Decimal\nType'HO' for hexadecimal-Octal")
#=-=-=-=-=-=-=-=-=-=-=-=
notoconvert='BD'
#typetoconvert=str(input("Enter the conversion type : "))
typetoconvert='BD'
result=''
#=-=-=-=-=-=-=-=-=-=-=-=
match typetoconvert:
    case 'BD':
        result =format(notoconvert, 'b')
    case 'BH':
        result =format(notoconvert, 'b')
    case 'BO':
        result =format(notoconvert, 'b')
    case 'DB':
        result = typetoconvert
    case 'DH':
        result = typetoconvert
    case 'DO':
        result = typetoconvert
    case _:
        inputvalue = 'Null'
print(f"the selected option is {result}")
      
