sum = 0

while True:
    with open("task5.txt","r") as file:
        sum_list = file.read().split()
        for i in sum_list:
            sum += int(i)
            
    with open("task5_2.txt","w") as file3:
        if sum % 2 == 0:
            file3.write("1")
        else:
            file3.write("1")
        if len(sum_list) == 1:
            break
    with open("task5.txt","w") as file2:
        file2.write(str(sum))
    
