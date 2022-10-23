import yfinance as yf
import pandas as pd

nvda = yf.Ticker("NVDA")
hist = nvda.history(period="max")

hist.to_csv("nvda-history.csv")

