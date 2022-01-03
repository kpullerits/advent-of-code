# test input
x_min = 20
x_max = 30
y_min = -10
y_max = -5

# real input
x_min = 253
x_max = 280
y_min = -73
y_max = -46

#what is x_velo min?
x_velo_start = 1

min_x_velo = 1
found_min = False
while True:
    x_velo = x_velo_start
    step = 1
    x_pos = 0
    if not found_min:
        while True:
            x_pos += x_velo
            if x_pos >= x_min:
                min_x_velo = x_velo_start
                found_min = True
                break
            if x_velo == 0:
                if x_pos < x_min:
                    x_velo_start += 1
                    break
            

            if x_velo > 0:
                x_velo -= 1
            step += 1
    else:
        break
    
max_x_velo = x_max
min_y_velo = y_min
max_y_velo = abs(y_min)

max_y_val = 0
count_initial_velo = 0
initial_velo_success = []
for x_velo_start in range(min_x_velo,max_x_velo+1):
    for y_velo_start in range(min_y_velo, max_y_velo+1):
        step = 1
        curr_max_y_val = 0
        x_pos = 0
        y_pos = 0
        x_velo = x_velo_start
        y_velo = y_velo_start
        while True:
            x_pos += x_velo
            y_pos += y_velo
            if curr_max_y_val < y_pos:
                curr_max_y_val = y_pos
            
            if (x_pos >= x_min and x_pos <= x_max) and (y_pos >= y_min and y_pos <= y_max):
                count_initial_velo += 1
                initial_velo_success.append((x_velo_start, y_velo_start))
                if max_y_val < curr_max_y_val:
                    max_y_val = curr_max_y_val
                break
            if x_pos > x_max:
                break

            if y_pos < y_min:
                break
            if x_velo > 0:
                x_velo -= 1
            y_velo -= 1
            step += 1
print("Part 1: " + str(max_y_val))
print("Part 2: " + str(count_initial_velo))
