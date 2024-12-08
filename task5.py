def func(str, num):
    # შევქმენი ალფაბეტის სტრინგი და სია რომელშიც არის ისეთი ელემენტები რომლებიც არშედის ალფაბეტში
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    not_alphabet = [" ", "!", ","]
    
    final_str = ""
    final_result = ""
    
    
    # მოვძებნი ალფაბეტში მომხმარებლის სტრინგის ასოებს და num იდან გამომდინარე დავაბრუნებ ალფაბეტის სიიდან შესაბამის ქერექთერს
    for char in str.lower():
        if char in not_alphabet:
            final_str += char
        else:
            if (alphabet.index(char) + num) > len(alphabet) -1:
                final_str += alphabet[(alphabet.index(char) + num) % len(alphabet)]
            else:
                final_str += alphabet[alphabet.index(char) + num]
    
    filtered_arr = []
    for char in final_str:
        filtered_arr.append(char)
        

    # აქ უკვე დიდ ასოებს ვეძებ და ვცვლი
    for char in str:
        if char.upper() == char:            
            filtered_arr[filtered_arr.index(final_str[str.index(char)])] = final_str[str.index(char)].upper()

    for element in filtered_arr:
        final_result += element
    
    return final_result


print(func("Hello, World!", 5))