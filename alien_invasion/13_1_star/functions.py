from random import randint
from image import Ship


def get_list(setting_length,star_num):
		#传入随机数范围,返回内含50个不重复整数的列表
		num = []
		while len(num) < star_num:
			number = randint(0,setting_length)
			if number not in num:
				num.append(number)
			else:
				pass
		return num

def get_star(stars,setting):
	setting.x = get_list(setting.width,setting.star_num)
	setting.y = get_list(setting.height,setting.star_num)
	for x,y in zip(setting.x,setting.y):
		star = Ship()
		star.rect.x = x
		star.rect.y = y
		stars.add(star)
		