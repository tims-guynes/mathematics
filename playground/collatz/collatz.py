

def collatz(n):
    x = int(n)
    num_list = [x]

    while x != 1:
        if x == 1:
            break
            
        elif x % 2 == 1:
            #num_list.append(x)
            x = (3 * x) + 1
            #print(int(x))
        else:
            x = x / 2
            #print(int(x))
        num_list.append(int(x))
    #print(num_list)
    return num_list

#collatz(640)