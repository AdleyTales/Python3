
# 计算1-x之间所有奇数的和

def addJS(x,y):
    sum = 0
    while x < y:
        sum = sum + x
        x = x + 2
    return sum

ch = addJS(1,100)
print(ch)