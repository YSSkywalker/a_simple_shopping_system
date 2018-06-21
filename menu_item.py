class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# "メニュー名: ¥値段"を返す
    def info(self):
        return self.name + ': ¥' + str(self.price)

# 合計金額を返す
    def get_total_price(self, count):
        total_price = self.price * count

        if count >= 3:
            total_price *= 0.9

        return round(total_price)
