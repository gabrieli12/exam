def func(x, n):
    final_arr = []
    
    for i in range(x):
        final_arr.append(1)
        
    # სიიდან მივწვდი ელემენტებს და ვამატებ სიაში ახალ ელემენტს რომელიც არის სიიდან ბოლო n ელემენტების ჯამი, ინდექსებით
    while len(final_arr) < n:
        sum = 0
        for i in range(1, x + 1):
            sum += final_arr[-i]
        final_arr.append(sum)
        
            
    return final_arr

print(func(4, 6))
    
    