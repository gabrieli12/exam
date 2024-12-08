def func(arr, k):
    arr.sort()
    # დავასორტირე და ინდექსით მივწვდი ელემენტს
    return arr[k-1]

print(func([7, 10, 4, 3, 20, 15], 3))