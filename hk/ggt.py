import pandas as pd
import akshare as ak

class GgtPicker(object):
    def __init(self):
        self._all_stocks = pd.DataFrame()

    def store_all(self):
        em_df = ak.stock_hk_ggt_components_em()
        df = em_df[['序号', '代码', '名称', '最新价', '成交量', '成交额']]
        df.set_index("代码", inplace=True)        
        
        pe = []
        pb = []
        for code in df.index.values        :
            pe_baidu_df = ak.stock_hk_valuation_baidu(symbol=code, indicator="市盈率(TTM)", period="近一年")
            pe.append(pe_baidu_df['value'].iloc[-1])
            
            pb_baidu_df = ak.stock_hk_valuation_baidu(symbol=code, indicator="市净率", period="近一年")
            pb.append(pb_baidu_df['value'].iloc[-1])

        df['市盈率(TTM)'] = pe
        df['市净率'] = pb
        self._all_stocks = df
        
        print(self._all_stocks)
        self._all_stocks.to_csv("ggt_stocks_all.csv")

    def pick_low_pepb(self):        
        df = self._all_stocks
        df = df[(df['市盈率(TTM)'] < 5.0) & (df['市盈率(TTM)'] > 0.0) & (df['市净率'] < 0.5)]        
        
        print(df)
        df.to_csv("ggt_stocks_low_pepb.csv")

ggtPicker = GgtPicker()
ggtPicker.store_all()
ggtPicker.pick_low_pepb()



