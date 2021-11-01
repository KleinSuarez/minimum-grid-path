#import math

def calc_min_cost(c_i, n_grid):
    rigth_min_cost = up_min_cost = 1e9
    rigth_cost = [0] * n_grid
    up_cost = [0] * n_grid
    
    for index in range(n_grid):
        if index % 2 == 0:
            up_min_cost = min(c_i[index], up_min_cost)        
        else:
            rigth_min_cost = min(c_i[index], rigth_min_cost)
        
        up_cost[index] = up_min_cost
        rigth_cost[index] = rigth_min_cost
    
    min_cost = 1e5
    up_sum_cost = 0
    rigth_sum_cost = 0
    
    for index in range(n_grid):
        up_next = (index + 2) // 2
        rigth_next = index + 1 - up_next
        if index % 2 == 0:
            up_sum_cost += c_i[index]
        else:
            rigth_sum_cost += c_i[index]
            
        total_cost = up_cost[index] * (n_grid - up_next) + up_sum_cost + rigth_cost[index] * (n_grid - rigth_next) + rigth_sum_cost
        min_cost = min(total_cost, min_cost)
    
    return min_cost

num_tests = int(input())
for index in range(num_tests):
    n_grid = int(input())
    c_i = list(map(int, input().split()))
    result = calc_min_cost(c_i, n_grid)
    print(result)