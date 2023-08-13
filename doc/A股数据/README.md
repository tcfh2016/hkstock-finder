## [个股信息](https://www.akshare.xyz/data/stock/stock.html#id8)

使用`ak.stock_individual_info_em(symbol="000001")`来查询个股信息：

```
  item                value
0   总市值  337468917463.220032
1  流通市值      337466070320.25
2    行业                   银行
3  上市时间             19910403
4  股票代码               000001
5  股票简称                 平安银行
6   总股本        19405918198.0
7   流通股        19405754475.0
```

## [关键指标](https://www.akshare.xyz/data/stock/stock.html#id182)

使用`ak.stock_financial_abstract(symbol="600004")`可以获取

```

```

## [财务报表-新浪](https://www.akshare.xyz/data/stock/stock.html#id171)

官方文档的示例中是使用`stock_financial_report_sina(stock="sh600600", symbol="资产负债表")`来获取资产负债表。测试之后发现获取到的数据是空的，之后发现是现在`stock`里面传递的股票代码不需要添加前缀，直接传入`600600`即可。
