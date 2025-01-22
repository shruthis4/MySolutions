import csv
with open('testList.csv',mode='r',newline='',encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
with open('testList.txt',mode='r',newline='') as file:
    # content = file.read()
    # print(content)

    # for line in file:
    #     print(line.strip())

    lines =file.readlines()
    for line in lines:
        print(line.strip())

    