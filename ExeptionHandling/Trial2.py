try:
    ERR_LST = []
    ar_int = [[1,2,3],[1,2]]
    ar_char = [['a','s'],[1,2,3]]
    ar_jagged = [[1,2,3],2,3]
    f = open('myfile12.txt', "w+")
    s = f.readline()
    i = int(s.strip())
    
except FileNotFoundError:
    print("Couldn't find the file.")
    ERR_LST.append("FileNotFoundError")
    
except ValueError:
    print("Could not convert data to an integer.")
    ERR_LST.append("ValueError")
    
except OSError as err:
    print("OS error:")
    print("OS error:", err)
    ERR_LST.append("OSError")
    
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    ERR_LST.append(f"{type(err)=}")
    raise

finally:
    if "FileNotFoundError" in ERR_LST:
        pass
    else:
        f.close()
    
