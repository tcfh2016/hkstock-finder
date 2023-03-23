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

## 增删改查

pandas 1.5.2之后支持了字符串`string`类型。PyCharm是Python用得最强大的IDE。