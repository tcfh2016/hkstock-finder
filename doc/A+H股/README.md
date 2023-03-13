## 港股

港股的一些常用接口课可以在“AKShare数据字典”-> “[港股](https://akshare.akfamily.xyz/data/stock/stock.html#id61)”里面查看。



## 港股估值

使用`stock_hk_eniu_indicator`是从亿牛网获取港股个股指标: 市盈率, 市净率, 股息率, ROE, 市值。不过最新只到2022年7月13日的估值数据，不再使用。

另外一个用法是使用`stock_hk_valuation_baidu`从百度股市通里面获取数据。`indicator`可取"总市值", "市盈率(TTM)", "市盈率(静)", "市净率", "市现率"中的任何一个。

```
stock_hk_valuation_baidu_df = ak.stock_hk_valuation_baidu(symbol="02358", indicator="总市值", period="近一年")
print(stock_hk_valuation_baidu_df)
```

## A股估值

使用`stock_zh_valuation_baidu`从百度股市通里面获取指定 symbol 和 indicator 的所有历史数据。

```
import akshare as ak

stock_zh_valuation_baidu_df = ak.stock_zh_valuation_baidu(symbol="002044", indicator="总市值", period="近一年")
print(stock_zh_valuation_baidu_df)
```
55 1193 1625 544

## A+H名单

使用`stock_zh_ah_name`从腾讯财经获取A+H股票名单。

```
stock_zh_ah_name_dict = ak.stock_zh_ah_name()
print(stock_zh_ah_name_dict)
```

## 参考

 - [AKShare 快速入门](https://www.akshare.xyz/tutorial.html#akshare)
 - [港股个股指标](https://akshare.akfamily.xyz/data/stock/stock.html#id246)
 - [港股估值指标](https://akshare.akfamily.xyz/data/stock/stock.html#id247)
 - [A 股估值指标](https://akshare.akfamily.xyz/data/stock/stock.html#id249)
 - [A+H股票字典](https://akshare.akfamily.xyz/data/stock/stock.html#id50)