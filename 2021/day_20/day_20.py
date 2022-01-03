import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_20.txt") as file:
    input = np.array([[0 if c == '.' else 1 for c in line.rstrip()] for line in file.readlines()])
#test
imag_enhan_algo = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
#real
imag_enhan_algo = "##.....##.#.#####.#...###...#.##..#....##..#.##.#.#....##.....#.##.##.#.#.#...#.#.#.###.##..#.#.#.#..#.##.#...#..#.#.#..#####.##.#..#..##.#..#.#...#.....#.###..#..#####.##...#..##..##...#.#...##.##..##...##.##.#......#...##.##.#####.#....####....######.#.#.......#.############.###..#..#......####......#..##.####.##....#..#.#.###..#.####.####.#.##.##.##..###.#..#.......#....#..########....##..##.#...#.#.###.###.###..#..#.###..#....#.###..#.##.##..###.#.#####....###.##.###.....#######........#.#.##...##.#...."


iterations = 2 # Part 1
iterations = 50 # Part 2
padding = 2*iterations
new_image = np.zeros((len(input)+2*padding, len(input)+2*padding))
new_image[padding:padding+len(input), padding:padding+len(input)] = input

def get_pixel(grid):
    bin = ''
    for i in range(3):
        for j in range(3):
            bin += str(int(grid[i,j]))
    decimal = int(bin, 2)
    return 1 if imag_enhan_algo[decimal] == "#" else 0

current_edge = 0
for i in range(iterations):
    temp_image = new_image.copy()
    for row in range(1,len(new_image)-1):
        for col in range(1,len(new_image)-1):
            grid_to_check = temp_image[row-1:row+2, col-1:col+2]
            enhanced_pixel = get_pixel(grid_to_check)
            new_image[row,col] = enhanced_pixel
    if current_edge == 0:
        current_edge = 1
    else:
        current_edge = 0
    new_image[0,:] = current_edge
    new_image[-1,:] = current_edge
    new_image[:,0] = current_edge
    new_image[:,-1] = current_edge
    if i == 1:
        lit_pixels = len(new_image[new_image >= 1])
        print("Part 1: " + str(lit_pixels))


lit_pixels = len(new_image[new_image >= 1])

print("Part 2: " + str(lit_pixels))
