def pretty_function(string_to_count):
    raise NotImplementedError()


def Ugly_Function(string_to_count):
    Cpy_Of_String = str(string_to_count)
    Result        = {}#holds result
    
    
    for c in Cpy_Of_String:
        if (c in Result.keys()) == False:
            Result[c] = [c]
        elif (c in Result.keys()) == True:
            a = Result[c]
            a.append(c)
            Result[c] = a
            
    NormalResults = {}
    for r, v in Result.items():
        i = 0
        for item in v:
            i += 1
        NormalResults[r] = i
                
    print(NormalResults)
    
    
    
    
    Result2= {}    
    for c in Cpy_Of_String:
        if (c.lower() in Result2.keys()) == False:
            Result2[c.lower()] = [c.lower()]
        elif (c.lower() in Result2.keys()) == True:
            a = Result2[c.lower()]
            a.append(c.lower())
            Result2[c.lower()] = a
            
    smallresult = {}
    for r, v in Result2.items():
        i = 0
        for item in v:
            i += 1
        smallresult[r] = i
                
    print(smallresult)


if __name__ == '__main__':
    string_to_count = 'Otters are COOL animals! The coolest!'
    Ugly_Function(string_to_count)
    # pretty_function(string_to_count)
