# NVDA Price Prediction

> Using univariate time-series price data, we aim to predict a stock's price in the following 14 days. We examine the efficacy of both ARIMA and LGBM models in their prediction accuracy with validation via RMSE.


**what** are we doing? predicting the stock price of NVDA across 14 days given as far lookback as we can
- should we necessarily use all available data? 
- what timespan should we analyse?

what data are we **sourcing** and how? yfinance data.

how are we **cleaning/pre-processing** our data?

what is our **approach to analysis**? primary data source is price so we shall hence assume that **all necessary information is already impounded in the market price, and other inputs are futile**.

how then do we form our **methodology**? 
- what we want: exact price predictions
	- linear regression works fine
- ARIMA
- LGBM

what **features** do we consider? univariate timeseries data.

## Conclusion

> In trying to predict future prices over 14 days, we have determined that the ARIMA and LGBM models perform equal to or worse than a naive forecast given daily time-series data.
