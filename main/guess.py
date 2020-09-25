import random

def generate_code():
    my_list=list(range(10))
    random.shuffle(my_list)
    return my_list[:3]

def check_match(code,user_Code):
    pattern=[]
    for index,el in enumerate(user_Code):
        if int(el) in code:
            if int(el)== code[index]:
                print('match')
                pattern.append('match')
            else:
                print('close')
                pattern.append('close')
    return pattern        
            
def check_results(user_Code):
    code=generate_code()
    print(code)
    result=(check_match(code, user_Code))
    print(result)
    
    

user_Code=input("input ur code")
check_results(list(user_Code))


#digits = list(range(10))
#print (digits)
#random.shuffle(digits)
#print(digits[:3])