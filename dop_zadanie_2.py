def digit_root(num):
    for i in range(10):
        if num < 10:
            break
            
        total_sum = 0
        for x in str(num):
            total_sum = total_sum + int(x)
            
        num = total_sum
        
    return num