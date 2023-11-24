def o_que_faco(n):
    if n == 1 or n == 0:
        
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print("False")
            return False
 
    return True