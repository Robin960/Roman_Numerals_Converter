class IntToRomans:
    def int_to_romans(self, n):
        
        ''' 
            Please change the value of 'n' that you want to see as a Roman Numeral at the end of this program

            'Code Explanation'
            There are three lists and two variable used in order to create a solution for 
            converting integer input to roman numerals.

            The first list holds the Roman Numerals, Second list holds the numeric values which help the conversion of Integeres into Roman Numerals.
            
            The Roman Numerals are mapped with the same index order og numeric list values. e.g 'M' = 1000. 
            
            The third list is just to append the values of each iteration output.
            
            The index varible is for iteration purpose to access the elements from list
            and result variable is for storing the final output of the converted value.
            
            Please Note: This solution converts the integer values into Roman Numerals between 1 to 3999 not more than 3999.

            Correct Use Case:   input = 10  ouput should be = X
            Incorrect Use Case: input = 2.1, '2.2', -2  Ouput with exception message

       
        '''

        roman_numerals = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        numerics = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        index = 0
        numeral = []

        #To check the input number, it should be greater than 0 and less than 3999 based on the rule of Roman Numerals. 
        # and also type of number should be int.
        try:
            if n <= 0 or n > 3999 and type(n) != int and type(n) == float:
                print(n,'Does not have the Roman Numerals, Please provide a integer number between 1 to 3999')
        
        # Exception handling for input type.
        except TypeError:
            print('Only Int type is allowed')
        
        else:
            try:
                while(n > 0):
                    if(n - numerics[index] >= 0):
                        numeral.append(roman_numerals[index])
                        n -= numerics[index]
                    else:
                        index +=1
            
            #Concatenate the list values to make a single string
                result = ''.join(numeral)
                return result
            # Exception handling for list index out of bound.
            except IndexError:
                print('Please provide the correct input value to the function')

#creation of class object
itr = IntToRomans()    

#Please pass your input here, the default input is 2:
n = 2

#Calling a int_to_romans() function with parameter inside the print() function, to see the ouput on console.
#If there is no output value based on your then print() will return None.
print(itr.int_to_romans(n))
