print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Exit')

while True:
    x = input('Pick an Operation (1-5): ') 

    try:
        operation = int(x) 
    except:
        print('Invalid Entry')
        continue

    if not (1 <= operation <= 5):
        print("Invalid Entry")
        continue

    if operation == 5:
        print('Exiting Program')
        break

    y = input('Number 1: ')

    try:
        number_1 = float(y)
    except:
        print('Invalid Entry')
        continue

    z = input('Number 2: ')

    try:
        number_2 = float(z)
    except:
        print('Invalid Entry')
        continue

    if operation == 1:     
        print((number_1) + (number_2))
        
    elif operation == 2 : 
        print((number_1) - (number_2))

    elif operation == 3 :
        print((number_1) * (number_2))
        
    elif operation == 4: 
        if number_2 == 0:
            print('Cannot divide by zero')
        else:
            print((number_1) / (number_2))
        
    
    
    
        
    

    

    







