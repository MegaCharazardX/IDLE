class Conversion :
    #input_type = str()
    str1 = str()
    input_type = str1
    def _init__ (self) :
        self.numbertypes=dict({'B':'Binary','D':'Decimal'})
        self.input_type = ''
        self.conversion_type = ''
        self.input_value = 0

    def ValueInitialization (self,_input_type,_conversion_type,_input_value = 0,_another_value = 0,_another_value1 = 0) :
        self.input_type =_input_type
        self.conversion_type = _conversion_type
        self.input_value = _input_value
        print('_input_type',_input_type,
              '_conversion_type',_conversion_type,
              '_input_value',_input_value,
              '_another_value',_another_value)



    
    
        
obj = Conversion()
obj.ValueInitialization('b','d')
