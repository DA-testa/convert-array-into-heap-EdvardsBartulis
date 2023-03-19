# python3


def build_heap(rng,data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    # 5
    # 5 4 3 2 1
    for i in range(rng-1, 0, -1):
        chain = True
        parent = (i-1)//2
        child=i
        
        while chain:   
            if data[child]<data[parent] and parent>=0:
                data[child],data[parent]=data[parent],data[child]
                swaps.append([parent,child])
            else:  
                chain = False
                
            child=parent
            parent= (child-1)//2
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    i = input()
    if 'i' in i.lower():   
        n = int(input())
        data = list(map(int, input().split()))
    elif 'f' in i.lower():  
        file_name = input()
        if 'a' in file_name:
            return
        try:
            with open("./tests/"+file_name, mode='r',encoding="utf8") as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
        except FileNotFoundError:
            return
    else:
        return
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(n,data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
