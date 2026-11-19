''''''
'''
数据读取与写入：基于pandas提供的api，可以实现各类文件（csv,Excel,数据库，网络数据等）的读取与写入
读取read
写入to

print(df.head()) 看前几行

'''
import pandas as pd
df = pd.read_csv("data/sales.csv",usecols = ["订单号",'产品类别','产品名称','销售数量','单价'])
print(df.head(3))
df['销售金额'] = df['销售数量'] * df['单价']
df

"""
数据的查看、选择和过滤
# 查看
df.head(3)  查看df前三行
df.tail(3)  查看df末尾3行
df.describe()   查看列的统计描述
df. info()  查看数据信息（列名、非空计数、数据类型）
df.shape    属性，查看数据维度，查看行列数
df.columns  查看列名

# 操作
df["列名"]    操作单列
df[["列1"，"列2”]]     操作多列
df.iloc[start:stop:step]    基于行号完成切片（不含stop），行号永远是0,1,2,3
df.loc[start:stop:step]     基于索引完成切片（包含stop），索引可以自定义

# 按条件筛选数据
df[df['销售数量'] >= 10]
df[df['产品类别'].isin(['服装','食品'])]
df[df['单价'].between(50,200)]
多条件： &(并且），|(或），每个条件单独加括号，必须，不能用and或者or

多条件用query()更合适，里面用and/or
df.query("销售数量 >= 10 and 单价 > 100")

"""