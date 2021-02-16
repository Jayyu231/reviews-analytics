data = []
count = 0
with open('reviews.txt', 'r') as f :
	for line in f :  #每個\n 為一筆
		data.append(line)
		count += 1 #count=count+1
		if count % 1000 == 0:
			print(len(data))

print(data[0])


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


for index, item in enumerate(data):
	if len(item) < 10:
		#if    #想只要show 出10 筆

		print('The No ', index , '是小於10個字')

print(data[index])


print('一共有', len(new) , '筆留言長度小於100個字')
		
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good) ,'筆留言提到good')
print(good[0])



#文字計數
wc = {} #word count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key 進wc 字典
for word in wc:
	if wc[word] >1000000:
		print(word, wc[word])

print(len(wc))
print('Allen in it', wc['Allen'])

while True:
	word = input('請問你想找甚麼字')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:' , wc[word])
	else:
		print('這個字沒又出現過歐!')
	print(word, '出現過的次數為: ', wc[word])

print('感謝使用本查詢功能')

