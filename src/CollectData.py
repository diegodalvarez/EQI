# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:57:10 2026

@author: Diego
"""

import os
import pandas as pd
import yfinance as yf
import datetime as dt

class DataCollector:
    
    def __init__(self) -> None: 
        
        self.start_date = dt.date(year = 1950, month = 1, day = 1)
        self.end_date   = dt.date(year = 2026, month = 1, day = 1)
        self.tickers    = [
            "SPY", "QQQ", "IYY", "XLI", "XLV", "XLF", "XLE", "XLU", "XLK", 
            "XLB", "XLP", "XLY", "XLC"]
        
        self.repo_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
        self.data_path = os.path.join(self.repo_path, "data")
        
    def get_yf_data(self, verbose: bool = True) -> None: 
        
        if verbose: print("Getting Raw YF Data")
        out_path = os.path.join(self.data_path, "RawPX.parquet")
        
        if os.path.exists(out_path):
            if verbose: print("Already have YF Data\n")
            return None
        
        df_raw = (yf
                  .download(
                      tickers     = self.tickers,
                      start       = self.start_date,
                      end         = self.end_date,
                      auto_adjust = False)
                  .reset_index())
        
        df_out = (df_raw
                  .melt(id_vars = [("Date", "")])
                  .rename(columns = {("Date", ""): "date"}))
        
        if verbose: print("Saving data\n")
        df_out.to_parquet(path = out_path, engine = "pyarrow")
        
        
if __name__ == "__main__": 
    DataCollector().get_yf_data()