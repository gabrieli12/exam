def func(n):
    final_arr = []
    not_prime_numbers = []
    final_result = 1
    
    # იგივე კოდია რაც იყოს prime ში უბრალოდ ახლა ვითვლი ნამრავლს რიმე რიცხვების
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                not_prime_numbers.append(i)
                break
            
    for i in range(2, n+1):
        if i not in not_prime_numbers:
            final_arr.append(i)
                
    if 1 in final_arr:
        final_arr.remove(1)
        
    # აქ ვითვლი ნამრავლს
    for element in final_arr:
        final_result *= element
        
    return final_result


print(func(1))


