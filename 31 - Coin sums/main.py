def countPerms(target,coins):
    if len(coins) == 0:
        return 0

    highcoin = coins[0]

    maxcs = int(target/highcoin)

    count = 0
    for cs in range(maxcs,-1,-1):
        if (cs * highcoin) == target:
            count = count + 1
        else:
            count = count + countPerms(target - cs * highcoin,coins[1:])
    
    return count

coins = [200,100,50,20,10,5,2,1]

print(countPerms(200,coins))