## 数据类型

Python里面的原生类型有`int`, `float`等，但没有pandas中的`float64`, `int64`等类型。

Pandas中常用的类型为`float64`, `int64`和`object`三种类型。简单理解就是浮点数、整数和字符类。

## 查看类型

可以通过`df.dtypes`或者`df.info()`来查看。

## 类型转换

在创建的时候可以通过指定`dtype`参数来确定类型，转换的时候可以使用`df.astype("type")`来进行转换，*当碰到无法转换的类型时会报错*。

另外一种高级的是使用自定义的函数来完成类型的转换，比如：

```
def my_convert_func(value) -> float:
    if isinstance(value, str):    
        new_value = value.replace(value, '123')
    else:
        new_value = value

    return np.float64(new_value)

temp_df['close'] = temp_df['close'].apply(my_convert_func)
```

## 增删改查 - 数据游览

pandas 1.5.2之后支持了字符串`string`类型。PyCharm是Python用得最强大的IDE。

1）数据游览，直接查看变量的值。太长的可以用Pycharm的sciview来查看。可以用`df.head(5)`, `df.tail(5)`来查看。

- `pd.set_option('display.max_rows', None)`
- `pd.set_option('display.max_columns', None)`
- `pd.set_option('display.precision', 2)`
- `pd.set_option('display.float_format', "{:.2f}".format)`

2）数据描述

- 使用`df.info()`来查看摘要。
- 使用`df.describe()`打印常用的数据统计功能。


## 增删改查 - 筛选数据

print(stock_zh_a_hist_df.index)
print(stock_zh_a_hist_df.columns)

- 查看某列的数据
- `df[col]`为`Series`，`df[[col]]`为`DataFrame`
- 查看多列的数据：`df[[col1, col2...]]`
- 查看多行的数据：`df[row1:row2]`左右都是闭区间，`df[:10]`左闭右开区间

以上的筛选意义不是很明确，更加推荐：

- `df[row]`筛选出列，`df.loc[row]`筛选出行
- `df.loc[[row1,row2]]`，`df.loc[row1:row2]`筛选出多行。
- `df.loc[row1:row2, col1:col2]`, `df.loc[[row1,row2], [col1, col2]]`, `df.iloc[row_s:row_e, 1:2]`筛选出多行多列

筛选单个值：

- `df.at[row, col]`, `df.iat[row_index, col_index]`

带`i`的效率较高，但是编程的时候使用较少，因为难快速定位具体的行或列的数值索引。

布尔索引：

- df[df['开盘'] > 60]
- df[(df['开盘'] < 60) & (df['开盘'] > 50)]


## 增删改查 - 增加列

增加列，直接通过`df[new_col] = new_column`即可。如果要在特别列之前添加，需要使用`insert()`函数。

## 增删改查 - 修改行列

1）修改列/行标签

使用`rename()`传入一个字典，里面包含了修改信息。比如：

- `rename(columns={A1:A2, B1:B2})`会将列A1替换为A2，B1替换为B2。
- `rename(index={A1:A2, B1:B2})`会将行A1替换为A2，B1替换为B2。

2）修改单元值

3）重设索引

使用`reset_index()`。


## 删除行列

- df.drop(columns=[col1, col2], inplact=True)
- df.drop(index=[0, 1], inplact=True)


## 缺失值处理

- df.fillna(0, inplace=True)
- df.fillna(method="ffill")，填充上一行的值。
- df.dropna(inplace=True, axis=0) 删除有缺失值的行。
- df.dropna(inplace=True, axis=1) 删除有缺失值的列。很少删除字段。


## 数据合并

在行的方向上扩展，使用`pd.concat([df1, df2])`（早期使用append，之后淘汰了），再使用`df.reset_index(inplace=True, drop=Ture)更新索引`。

另外用`merge`和`join`也可以使用。