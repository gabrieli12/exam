def func(a, b):
    
    # დავყავი მრიცხველი და მნიშვნელი
    num1 = a[0]
    denominator1  = a[1]
    
    num2 = b[0]
    denominator2  = b[1]
    
    
    # შევქმენი უდიდესი საერთო გამყოფი
    def gcd(x, y):
        return y == 0 and x or gcd(y, x % y)
    
    # შევქმენით უდიდესი საერთო ჯერადი
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    
    
    # შევაჯამეთ უდიდესი საერთო ჯერადები
    lcm_den =  lcm(denominator1 , denominator2)
    
    # გავიგეთ მრიცხველის მნიშვნელობები
    num1_adj = num1 * (lcm_den // denominator1)
    num2_adj = num2 * (lcm_den // denominator2)
    
    # დავაჯამეთ მრიცხველები
    numerator_sum = num1_adj + num2_adj
    
    # დავაბრუნეთ საბოლოო შედეგი
    return (numerator_sum, lcm_den)



    
print(func((1, 4), (1, 4)))