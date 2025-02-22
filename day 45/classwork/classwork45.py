#N1

def swap_values(args):
    temp = args[0]
    args[0] = args[1]
    args[1] = temp



#N2

def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"

    total_sum = 0

    for i in range(n, m, n):
        total_sum += i
    
    return total_sum