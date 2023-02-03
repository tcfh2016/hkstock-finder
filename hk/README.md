## 港股

港股的一些常用接口课可以在“AKShare数据字典”-> “[港股](https://akshare.akfamily.xyz/data/stock/stock.html#id61)”里面查看。


 "stock_hk_eniu_indicator"  # 港股股个股市盈率、市净率和股息率指标
 "stock_hk_valuation_baidu"  # 百度股市通-港股-财务报表-估值数据

  参考：

 - [AKShare 快速入门](https://www.akshare.xyz/tutorial.html#akshare)
 
 ## 估值指标

使用`stock_hk_eniu_indicator`是从亿牛网获取港股个股指标: 市盈率, 市净率, 股息率, ROE, 市值。不过最新只到2022年7月13日的估值数据。

```
import akshare as ak

stock_hk_eniu_indicator_df = ak.stock_hk_eniu_indicator(symbol="hk01093", indicator="市净率")
print(stock_hk_eniu_indicator_df)
```

另外一个用法是使用`stock_hk_valuation_baidu`从百度股市通里面获取数据。`indicator`可取"总市值", "市盈率(TTM)", "市盈率(静)", "市净率", "市现率"中的任何一个。

```
stock_hk_valuation_baidu_df = ak.stock_hk_valuation_baidu(symbol="02358", indicator="总市值", period="近一年")
print(stock_hk_valuation_baidu_df)
```

参考：

 - [港股个股指标](https://akshare.akfamily.xyz/data/stock/stock.html#id246)
 - [港股估值指标](https://akshare.akfamily.xyz/data/stock/stock.html#id247)