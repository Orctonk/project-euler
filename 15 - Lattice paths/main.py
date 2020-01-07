def latticePaths(width, height, mem):

    if (width,height) in mem:
        return mem[(width,height)]

    if(width == 1 and height == 1):
        return 2

    val = 0
    if(width == 1):
        val = latticePaths(1,height - 1,mem) + 1
    
    elif (height == 1):
        val = latticePaths(width - 1, 1,mem) + 1
        
    else:
        val = latticePaths(width,height-1,mem) + latticePaths(width-1,height,mem)

    mem[(width,height)] = val
    return val

mem = {}

print(latticePaths(20,20,mem))