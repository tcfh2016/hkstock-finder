## 常用接口

## [港股估值指标](https://www.akshare.xyz/data/stock/stock.html#id256)

```
import akshare as ak

stock_hk_valuation_baidu_df = ak.stock_hk_valuation_baidu(symbol="02358", indicator="总市值", period="近一年")
print(stock_hk_valuation_baidu_df)
```

## [历史行情数据](https://www.akshare.xyz/data/stock/stock.html#id20)

```
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20210907', adjust="")
```

## [股票市场总貌](https://www.akshare.xyz/data/stock/stock.html#id1)

```
stock_sse_summary_df = ak.stock_sse_summary()
```