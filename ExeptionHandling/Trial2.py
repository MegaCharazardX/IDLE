try:
    ar_int = [[1,2,3],[1,2]]
    ar_char = [['a','s'],[1,2,3]]
    ar_jagged = [[1,2,3],2,3]
    f = open('myfile12.txt')
    s = f.readline()
    i = int(s.strip())
except ValueError:
    print("Could not convert data to an integer.")
except OSError as err:
    print("OS error:")
    print("OS error:", err)
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

finally:
    f.close()
    
