def star_flag(n: int) -> None:
    if n <= 0:
        print("n must be a positive number.")
        return
    
    for i in range(n):
        print('*' * (i + 1))
    
    for i in range(n - 1, 0, -1):
        print('*' * i)



        

        
