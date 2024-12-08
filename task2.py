def func(str):
    # გავსპლიტე სტრინგი და შევქმენი ცარიელი სია რომელშიც შემდგომ ჩავამატებდი ელემენტებს
    splited_arr = str.split()
    filtered_arr = []
    
    # მივწვდი გასპლიტული სიის თითოეულ ელემენტს 
    for element in splited_arr:
        # შევამოწმე ელემენტი თუარარის გაფილტრულ სიაში და თუ ეს ასე დავამატე ამ სიაში
        if element not in filtered_arr:
            filtered_arr.append(element.lower())
    
    # იმ სიაში დაემატება ყველა ელემენტი მხოლოდ ერთხელ ხოლო საბოლოოდ დავაბრუნე მისი სიგრძე
    return len(filtered_arr)

    
    
print(func("Hello hello world!"))