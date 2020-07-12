products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []      #p = [name, price] = 7-9行
	p.append(name)
	p.append(price)
	products.append(p)  # products.append([name, price]) = 7-10行
print(products)