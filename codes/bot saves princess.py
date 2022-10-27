#!/usr/bin/python

def displayPathtoPrincess(n, grid):
    if grid[0][0] == "p":
        print("UP\nLEFT")
    elif grid[0][2] == "p":
        print("UP\nRIGHT")
    elif grid[2][0] == "p":
        print("DOWN\nLEFT")
    else:
        print("DOWN\nRIGHT")

m = int(input())
grid = []

for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m, grid)