from menu_item import MenuItem

class Food(MenuItem):
    def __init__(self, name, price, calorie):
        super().__init__(name, price)
        self.calorie = calorie
    
# "食べ物メニュー名: ¥値段 (カロリーkcal)"を返す
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'

# "カロリーkcalです"と表示    
    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')
