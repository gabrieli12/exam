def func(start, end):
    final_arr = []
    not_prime_numbers = []
    
    # მოკლედ მივწვდი რიცხვებს სტარტიდან ენდამდე და შევამოწმე ყველა რიცხვი თუ რომელიმეზე იყოფა 1 ის და თავის თავის გარდა დავამატეთ Not prime ში და შემდეგ რომლებიც ამ სიაში არიქნება იმეებს დავბეჭდავ
    for i in range(start, end):
        for j in range(2, i):
            if i % j == 0:
                not_prime_numbers.append(i)
                break
            
    for i in range(start, end):
        if i not in not_prime_numbers:
            final_arr.append(i)
                
    if 1 in final_arr:
        final_arr.remove(1)
        
    return final_arr
    
    
print(func(1, 10))