
#计算列表内数字阶乘总和

class Add:
    def __init__(self, src: list):
        self.src = src
        self.mid = 0
        self.res = 0

    def add(self):
        b = sorted(self.src)
        for i in range(b[-1]+1):
            self.mid += i
            if i in self.src:
                self.res += self.mid
        return self.res


a = [2, 6, 4, 3, 20]
a1 = Add(a)
print(a1.add())

print([(item, count) for item, count in collections.Counter(a).items() if count > 1])






