def seasonal_decomp(df, model):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    import seaborn as sns
    import pandas as pd
    from statsmodels.tsa.seasonal import seasonal_decompose 
    """
    A function that intakes a df and a model or method of seasonal decomposition and returns a     series of plots to enable the user to decide on what kinds of predictive model they'd like     to use. Model types include 'additive', 'multiplicative', and 'exponential'. 
    
    ** Requires:
    from statsmodels.tsa.seasonal import seasonal_decompose
    import matplotlib.pyplot
    import seaborn as sns** 
    """
    sns.set(rc={'figure.figsize':(11,9)})  
    
    decomposition = seasonal_decompose(df, model = model)                            
    
    fig, axes = plt.subplots(3, 1)
    sns.lineplot(ax = axes[0], data = decomposition.trend)      # plot the trend line, overall                                                                   tilt of the data
    sns.lineplot(ax = axes[1], data = decomposition.seasonal)   # plot the seasonal, a                                                                           reoccuring patterns 
    sns.lineplot(ax = axes[2], data = decomposition.resid);     # residuals represent the                                                                        noise in the data set that                                                                     is not explained 
    plt.tight_layout() 


def rmse(y_true, y_test):  
    from sklearn.metrics import mean_squared_error
    import numpy as np
    """
    A simple function that takes y_true and y_test to return the RMSE.
    ** Requires from sklearn.metrics import mean_squared_error **
    """
    return np.sqrt(mean_squared_error(y_true, y_test))

def seasonal_metrics_kpis(y_true, y_preds):
    from sklearn.metrics import mean_absolute_percentage_error 
    
    """
    A fucntion that intakes y_true and y_preds and spits out a readable version of the MAPE         score and RMSE.
    
    ** Requires rmse.py funciton AND 
    from sklearn.metrics import mean_absolute_percentage_error 
    from sklearn.metrics import mean_squared_error **
    """
    print(f'MAPE: {mean_absolute_percentage_error(y_preds, y_true) * 100} \nRMSE: {rmse(y_true, y_preds)}') 


def seasonal_metrics_graph(y_true, y_preds):
    import matplotlib.pyplot as plt
    import seaborn as sns
    """
    A function that intakes y_true and y_preds and spits out a plot that will show the true         data in a blue line, the predictions in a red line, the MAPE score and the RMSE score.          
    ** Requires:
    rmse.py 
    seasonal_metrics_kpis.py
    import matplotlib.pyplot as plt
    import seaborn as sns **
    """
    sns.lineplot(y_true)
    sns.lineplot(y_preds, palette = 'hls')
    plt.show()
    return seasonal_metrics_kpis(y_true, y_preds)

def sarima (train, y_true, order, seasonal_order):
    import pandas as pd
    from statsmodels.tsa.arima.model import ARIMA
    """" 
    A function that intakes a order and a SEASONAL order for a SARIMA model using                  statsmodels.tsa.api. It outputs four versions of that model, using the TREND parameter         iterate on no trend, a constant, a trendline, or a constant as well as a trend line. More      documentation about the TREND parameter here,
    https://www.statsmodels.org/dev/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html.    
    Having either a c, t or both will help a SARIMA model with data that's multiplicative in       decomposition. 

    **Requires:
    rmse.py
    seasonal_metrics_graph.py
    seasonal_metrics_kpis.py
    import matplotlib.pyplot as plt
    import seaborn as sns 
    from statsmodels.tsa.arima.model import ARIMA  **
    """
    trends = ['n', 'c', 't','ct', None]
    for trend_type in trends:
        print(f'_______________________________________________________________________________\n      Trend = {trend_type}')
        print(f' ORDER : {order}, {seasonal_order}')
        model = ARIMA(train, order = order, seasonal_order = seasonal_order, trend = trend_type).fit()
        preds = pd.DataFrame(model.forecast(52))
        seasonal_metrics_graph(y_true, preds)