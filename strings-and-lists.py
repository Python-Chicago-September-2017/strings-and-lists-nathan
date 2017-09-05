words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
print words.replace(" day"," month")

min_max = [2,54,-2,7,12,98]
print min(min_max)
print max(min_max)

first_last = ["hello",2,54,-2,7,12,98,"world"]
new_list = [first_last[0],first_last[-1]]
print new_list

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
half_length = len(x)/2
new_x = []
for i in range(0, half_length):
    new_x.append(x[i])
for i in range(0, half_length):
    x.pop(0)
x.insert(0,new_x)
print x