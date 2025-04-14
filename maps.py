def cube(x):
    return x * x * x

nums = [2, 3, 4]

cubes = list(map(cube, nums))
print(cubes)
