"""number_types = dict({'B': 'Binary', 'D': 'Decimal'}, two=2)
input_type = 'D'
con_type = 'B'
print('Converting from',number_types[input_type],'to',number_types[con_type],'.')"""


class Conversion:
    
    def __init__(self):
        self.number_types = dict({'B': 'Binary', 'D': 'Decimal'})
        self.input_type = ''
        self.con_type = ''
        self.input_value = 0

    def setValues(self,_input_type,_con_type,_input_value):
        self.input_type = _input_type
        self.con_type = _con_type
        self.input_value = _input_value
        

    def printValues(self):
        retVal = ''
        match self.con_type:
            case 'B':
                retVal = self.convertToBinary()                
            case 'D':
                retVal = self.convertToDecimal() 
                
        print('Converting ',self.input_value,'to',self.number_types[self.con_type],'is',retVal,'.')     

    def convertToBinary(self):
        _result = ''
        if self.input_value < 2 :
            _result = self.input_value
        else :
            _quotient = int(self.input_value)
            while _quotient > 1:
                _result = str(_quotient%2)+_result
                _quotient = int(_quotient/2)
                if _quotient >= 2:
                    continue
                else :
                    _result = str(_quotient)+_result
        return _result
    def convertToDecimal(self):
        _result = 0
        _input_value = str(self.input_value)
        _noOfDigits = len(_input_value)
        #print (_noOfDigits)
        for index in range (0,_noOfDigits) :
            _result = _result + int(_input_value[index]) * 2**(_noOfDigits - (index + 1))
        return _result
        
        


objConvert = Conversion()
objConvert.setValues('D','B', int(input("Enter the number to convert")))
objConvert.printValues()
