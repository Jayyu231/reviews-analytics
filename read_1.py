data = []
count = 0
with open('reviews.txt', 'r') as f :
	for line in f :  #每個\n 為一筆
		data.append(line)
		count += 1 #count=count+1
		if count % 1000 == 0:
			print(len(data))

print(len(line))
print(len(data))
print(data[0])
print('------------------------------')
print(data[1])



sum_len = 0
for d in data:
	sum_len = len(d) + sum_len
average = sum_len/ len(data)
print('留言的平均長度是',average)


		



