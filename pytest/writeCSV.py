import csv
data = [
    ["Age","Name"],
    [2,"Adam"],
    [3,"Alex"],
    [4,"Ada"]
]
with open('tempCSV.csv',mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data[:])
