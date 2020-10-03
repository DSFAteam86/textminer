from miner import TextMiner
import pandas as pd


class Data: 
  
  def __init__(self):
    text_miner = TextMiner()
  
  def convert_to_series(self, array):
    return pd.Series(array)