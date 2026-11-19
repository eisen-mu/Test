"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。
具体功能如下：
    1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
    5. 退出购物车
"""
# 定义商品类
class Goods:
    def __init__(self, name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount
    # 定义格式化输出
    def __str__(self):
        return f"商品名称：{self.name} | 商品单价：{self.price} | 商品数量{self.amount} | 合计： {self.price * self.amount}"
    # 定义修改商品
    def update_goods(self,name = None,price = None,amount = None):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if amount is not None:
            self.amount = amount
# 定义购物车管理系统
class ShoppingCar:
    version = 1.0
    def __init__(self):
        self.goods_list = []

    def add_goods(self):
        name = input("请输入商品名称")
        for i in self.goods_list:
            if i.name == name:
                print("商品已存在")
                return

        price = float(input("请输入商品单价"))
        amount = int(input("请输入商品数量"))
        good = Goods(name,price,amount)
        self.goods_list.append(good)

    def update_goods(self):
        name = input("请输入商品名称")
        for i in self.goods_list:
            if i.name == name:
                print(f"当前商品信息为：{i}")
                price = float(input("请输入商品价格"))
                amount =int(input("请输入商品数量"))
                i.update_goods(name,price,amount)
                print(f"当前商品信息为：{i}")
                return
        print("商品不存在")

    def delete_goods(self):
        name = input("请输入商品名称")
        for i in self.goods_list:
            if i.name == name:
                self.goods_list.remove(i)
                print("删除成功")
                return
        print("商品输入有误")

    def query_goods(self):
        for i in self.goods_list:
            print(i)

    def run(self):
        print(f"欢迎使用购物车系统，版本V{self.version}")
        while True:
            print()
            print("###############################")
            print("#1. 添加商品 2.修改商品 3. 删除删除 4. 查询商品 5. 退出系统#")
            print("###############################")
            choice = int(input("请输入操作选项，数字1-5"))
            match choice:
                case 1:
                    self.add_goods()
                case 2:
                    self.update_goods()
                case 3:
                    self.delete_goods()
                case 4:
                    self.query_goods()
                case 5:
                    break
                case _:
                    print("输入错误，请重新输入")


# 测试
if __name__ == "__main__":
    cart = ShoppingCar()
    cart.run()









