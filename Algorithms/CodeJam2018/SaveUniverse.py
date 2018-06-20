def getDamage(instruction):
    d = 0
    power = 1
    has_c = []
    has_s = []
    print(instruction)
    for index,i in enumerate(instruction) :
        if i == 'C':
            power *= 2
            has_c.append(index)
        elif i == 'S':
            d += power
            has_s.append(index)
    return d, has_c, has_s

def get_swaps(target_damage, instruction, max_damage):
    power = 1
    d = 0
    c = 0
    for i in range(0,len(instruction)):

        pass
    return c

a = input()
for i in range(a):
    target_damage, instruction = raw_input().split(' ')
    target_damage = int(target_damage)
    max_damage, has_c, has_s = getDamage(instruction)

    if max_damage <= target_damage :
        print( 'Case #'+ str(i)+ ": 0")
    elif max_damage > target_damage and (len(has_c)==0 or len(has_s)==0):
        print('Case #' + str(i) + ": IMPOSSIBLE")
    elif target_damage == len(has_s) :
        min_swaps = 0
        for index, k in enumerate(has_s):
            min_swaps += (k-index)
        print('Case #' + str(i) + ": "+str(min_swaps))
    else:
        min_swaps = get_swaps(target_damage, instruction, max_damage)
        print('Case #' + str(i) + ": "+str(1000))
        pass





