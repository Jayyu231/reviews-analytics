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

new = []
for d in data:
	if len(d) < 100 :
		new.append(d)
	#print('第', s ,'筆 清單長度為', len(s) ,'清單長度大於100')	


print('一共有', len(new) , '筆留言長度小於100個字')
		
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good) ,'筆留言提到good')
print(good[0])


