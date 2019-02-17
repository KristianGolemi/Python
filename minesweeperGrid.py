import random
# Ask for input about the number of the mines
mines = int(input("How many mines do you want?\n\t"))
# Grid creation
grid = [0] * 100
# Placing mines randomly
for i in range(mines):
    j = random.randint(0,99)
    grid[j] = 'm'
# Distance from the mines
num = 0
i = 0
while i <= 99:
    if  grid[i] != 'm':
        # Corners
        # Up left
        if i == 0:
            if grid[1] == 'm':
                num = num + 1
            if grid[10] == 'm':
                num = num + 1
            if grid[11] == 'm':
                num = num +1
        # Up right
        elif i == 9:
            if grid[8] == 'm':
                num = num + 1
            if grid[18] == 'm':
                num = num + 1
            if grid[19] == 'm':
                num = num + 1
        # Down left
        if i == 90:
            if grid[80] == 'm':
                num = num + 1
            if grid[81] == 'm':
                num = num + 1
            if grid[91] == 'm':
                num = num +1
        # Down right
        elif i == 99:
            if grid[88] == 'm':
                num = num + 1
            if grid[89] == 'm':
                num = num + 1
            if grid[98] == 'm':
                num = num + 1
        # Sides
        # Up
        elif i >= 1 and i <= 8:
            if grid[i-1] == 'm':
                num = num + 1
            if grid[i+1] == 'm':
                num = num + 1
            if grid[i+9] == 'm':
                num = num + 1
            if grid[i+10] == 'm':
                num = num + 1
            if grid[i+11] == 'm':
                num = num + 1
        # Down
        elif i >= 91 and i <= 98:
            if grid[i-11] == 'm':
                num = num + 1
            if grid[i-10] == 'm':
                num = num + 1
            if grid[i-9] == 'm':
                num = num + 1
            if grid[i-1] == 'm':
                num = num + 1
            if grid[i+1] == 'm':
                num = num + 1
        # Left
        elif i % 10 == 0:
            if grid[i-10] == 'm':
                num = num + 1
            if grid[i-9] == 'm':
                num = num + 1
            if grid[i+1] == 'm':
                num = num + 1
            if grid[i+10] == 'm':
                num = num + 1
            if grid[i+11] == 'm':
                num = num + 1
        # Right
        elif (i+1) % 10 == 0:
            if grid[i-11] == 'm':
                num = num + 1
            if grid[i-10] == 'm':
                num = num + 1
            if grid[i-1] == 'm':
                num = num + 1
            if grid[i+9] == 'm':
                num = num + 1
            if grid[i+10] == 'm':
                num = num + 1
        # Κανονικές περιπτώσεις
        else:
            if grid[i-11] == 'm':
                num = num + 1
            if grid[i-10] == 'm':
                num = num + 1
            if grid[i-9] == 'm':
                num = num + 1
            if grid[i-1] == 'm':
                num = num + 1
            if grid[i+1] == 'm':
                num = num + 1
            if grid[i+9] == 'm':
                num = num + 1
            if grid[i+10] == 'm':
                num = num + 1
            if grid[i+11] == 'm':
                num = num + 1
        grid[i] = num
    i = i + 1
    num = 0
print(-grid[0],grid[1],grid[2],grid[3],grid[4],grid[5],grid[6],grid[7],grid[8],grid[9],"\n",\
      grid[10],grid[11],grid[12],grid[13],grid[14],grid[15],grid[16],grid[17],grid[18],grid[19],"\n",\
      grid[20],grid[21],grid[22],grid[23],grid[24],grid[25],grid[26],grid[27],grid[28],grid[29],"\n",\
      grid[30],grid[31],grid[32],grid[33],grid[34],grid[35],grid[36],grid[37],grid[38],grid[39],"\n",\
      grid[40],grid[41],grid[42],grid[43],grid[44],grid[45],grid[46],grid[47],grid[48],grid[49],"\n",\
      grid[50],grid[51],grid[52],grid[53],grid[54],grid[55],grid[56],grid[57],grid[58],grid[59],"\n",\
      grid[60],grid[61],grid[62],grid[63],grid[64],grid[65],grid[66],grid[67],grid[68],grid[69],"\n",\
      grid[70],grid[71],grid[72],grid[73],grid[74],grid[75],grid[76],grid[77],grid[78],grid[79],"\n",\
      grid[80],grid[81],grid[82],grid[83],grid[84],grid[85],grid[86],grid[87],grid[88],grid[89],"\n",\
      grid[90],grid[91],grid[92],grid[93],grid[94],grid[95],grid[96],grid[97],grid[98],grid[99])
