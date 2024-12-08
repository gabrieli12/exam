def func(str):
    # გავსპლიტე სტრინგი და გადავაქციე სიად შევქმენი თავდაპირველად ცარიელი სტრინგი რომელშიც შემდეგ ჩავამატებ ტექსტს
    splited_arr = str.split()
    final_str = ""
    
    # სია შემოვაბრუნე
    splited_arr.reverse()
    
    # და სიის თითოეული ელემენტი ჩავამატე სტრინგში
    for element in splited_arr:
        final_str += element + ' '
        
    # ბოლოს ზედმეტი სფეისი იყო და მოვაცილე
    return final_str[0: -1]
    

print(func("hello world"))