count = 0
for coin10 in range(2):
    for coin5 in range(3):
        for coin2 in range(6):
            for coin1 in range(11):
                if(coin10*10 + coin5*5 + coin2*2 + coin1*1) == 10:
                    count=count+1
                    print("ways",count, ":", coin10,coin5,coin2,coin1)
print("Total number of ways: ",count)