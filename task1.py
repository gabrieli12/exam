def func(str1, str2):
    arr1 = []
    arr2 = []
    
    # ჩავამატეთ სტრინგების თითოეული ელემენტი სიში
    for element in str1:
        arr1.append(element)
        
    for element in str2:
        arr2.append(element)
        
    # დავასორტირე ორივე სია
    arr1.sort()
    arr2.sort()
    
    # შემდეგ კი შევადარე
    return arr1 == arr2
    
    
print(func("triangle", "integral"))