import os
import time, datetime
import pandas as pd
import akshare as ak
import logging

db_path = os.path.join(os.getcwd(), "db", "indicator", "")

def multi_indicators(sym, inds, perd):
    inds_df = pd.DataFrame(columns=inds)
    for ind in inds:        
        df = ak.stock_hk_valuation_baidu(symbol=sym, indicator=ind, period=perd)        
        df.set_index("date", inplace=True)
        inds_df[ind] = df["value"]
    return inds_df

def create(sym, csv):
    indicators = ["市盈率(TTM)", "市盈率(静)", "市净率", "市现率", "总市值"]
    inds_df = multi_indicators(sym, indicators, "全部")

    inds_df.to_csv(csv)
    logging.info("HKGGT, created new csv for {}, contains {} rows.".format(sym, len(inds_df)))

def append(sym, csv):
    old_df = pd.read_csv(csv, index_col=0)
    last_date = old_df.index[-1]

    fmt = '%Y-%m-%d'
    last_date = datetime.datetime.strptime(last_date, fmt).date()

    indicators = ["市盈率(TTM)", "市盈率(静)", "市净率", "市现率", "总市值"]
    inds_df = multi_indicators(sym, indicators, "近一年")
    gap_df = inds_df[last_date:][1:]

    new_df = pd.concat([old_df, gap_df])
    new_df.to_csv(csv)

    logging.info("HKGGT, update exist csv for {}, added {} rows.".format(sym, len(gap_df)))

def update():
    # 获取港股通成分股，包含'序号', '代码', '名称'...
    ggt_df = ak.stock_hk_ggt_components_em()
    logging.info("HKGGT, have total {} stocks.".format(len(ggt_df)))

    count_create = 0
    count_append = 0
    start = time.time()
    for symbol in ggt_df["代码"][:201]:
        indicator_csv = db_path + symbol + ".csv"

        if os.access(indicator_csv, os.R_OK):
            append(symbol, indicator_csv)
            count_append += 1
        else:
            create(symbol, indicator_csv)
            count_create += 1
    
    stop = time.time()
    logging.info("HKGGT, create {} stocks, and update {} stocks, total cost {:.2f} seconds.".format(count_create, count_append, stop-start))
    
if __name__ == "__main__":
    update()
    #test()

