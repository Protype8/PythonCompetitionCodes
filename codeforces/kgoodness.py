cases = int(input(""))
for i in range(cases):
    length,goodness = [int(a) for a  in input("").split(" ")]
    string = input("")
    opreations  = 0
    for j in range(length//2):
        print(j,length-(j+1))
        if(string[j] != string[length-(j+1)]):
            opreations += 1
    min_opreations = abs(goodness-opreations)
    print(f"Case #{i+1}: {min_opreations}")