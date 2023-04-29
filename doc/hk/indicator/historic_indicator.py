import akshare as ak
import matplotlib
import matplotlib.pyplot as plt

stock_hk_valuation_pe_df = ak.stock_hk_valuation_baidu(symbol="06098", indicator="市盈率(TTM)", period="全部")
stock_hk_valuation_pe_df = stock_hk_valuation_pe_df.set_index("date")
stock_hk_valuation_pe_df.columns = ["市盈率(TTM)"]
stock_hk_valuation_pe_df["市盈率(TTM)"].plot()


#stock_hk_valuation_pe_df.to_csv("06098_pe.csv")
plt.show()
#print(stock_hk_valuation_pe_df)