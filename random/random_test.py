from random_num import Die

#6面的骰子
die_100 = Die(6)

#投掷100次并储存
save_num=list(str(die_100.roll_die()) for num in range(100))




#1到6的出现次数
count_num=[]
for num in range(1,7):
    count_num.append(save_num.count(str(num)))

print (count_num)