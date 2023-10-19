# Pumpkin_Spice

![prchi-palwe-ZlSIjc_sPQ4-unsplash](https://github.com/casanave/Pumpkin_Spice/assets/8728172/1a44c2a9-0ad0-4285-9eb2-0f708ebe1e1b)

Photo by <a href="https://unsplash.com/@prachipalwe?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Prchi Palwe</a> on <a href="https://unsplash.com/photos/ZlSIjc_sPQ4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

 A project to try and predict the popularity of pumpkin spice using data from Google trends, SARIMA and ETS modeling. 


# Introduction:
To study different statistical models for predictive use in the search term "Pumkin Spice" on Google. I used data from Google Trends from the last 5 years. I will validate my predictions on a rolling basis for a double blind validation. Train/test split will be 80%/20%.

#### Hypothesis: Pumkin Spice is going to have strong seasonality, since it's associated with American Fall Holidays and seasonal food dishes. I can build a model to predict it's popularity that will perform better than either using last week's or last month's data. 

#### Null hypothesis: Using last week's data or last year's data will be more performative to predict this week's level of popularity for the search term "Pumpkin Spice."

# Data: 
5 year pull and export from Google Trends on 10/7/2023 to a csv.

### Disclaimers: 
I'll be using the term SARIMA as an umbrella term to mean any combination of seasonality, auto regressive terms, first differencing and/or moving average. However many of the models I will try won't have all of these components. SARIMA as a term will be used inclusinvely for the family of linear model.

### Feedback: 
I welcome feedback about my notebook, model or process. Please reach out to me via my linkedin if you have any positive or contructive feedback. I'm open to encorporating your perspective. https://www.linkedin.com/in/louis-casanave-78057aa0/

## Methods:
- To do a seasonal decomposition and analysis of the data.
- Train test split. 
- To make Autocorrelation and Partial Auto Correlation plots to inform a SARIMA model. 
- To get the MAPE score and RMSE of a naive model either using last weeks data as a direct prediction of this week's data, or last year's data as a direct predictions of this week's data.
- To try SARIMA terms based on inference in the ACF and PACF plots.
- To try auto arima to brute force SARIMA terms.
- To try an ETS model.
- To chose the model with the best combined scores of MAPE and RMSE and describe it's strengths. 
- To download the best model into a pickle file saved in this repo as pumpkin_spice_predictor. 
- To wait two weeks from the data pull (10/21/2023) and blind validate the model based on those two weeks of data.

# Raw Data: 
<img width="861" alt="Screenshot 2023-10-18 at 8 00 51 AM" src="https://github.com/casanave/Pumpkin_Spice/assets/8728172/740eecf2-84a6-4a3e-9844-9768cbb793b3">

#### Test Data shown in Blue
#### Predictions shown in Red
# Yearly Naive Model Performance: 
<img width="845" alt="Screenshot 2023-10-18 at 8 03 21 AM" src="https://github.com/casanave/Pumpkin_Spice/assets/8728172/1216ebd6-b5a6-4686-b1a4-7b22b847acfe">

# Best SARIMA Model Performance: 
<img width="840" alt="Screenshot 2023-10-18 at 8 04 29 AM" src="https://github.com/casanave/Pumpkin_Spice/assets/8728172/2c98f22d-6d98-4140-90b9-68691a05f658">

# Best Overall Model Performance (ETS): 
<img width="843" alt="Screenshot 2023-10-15 at 11 36 27 PM" src="https://github.com/casanave/Pumpkin_Spice/assets/8728172/0413d5d2-9d43-4e8e-b59d-3dd43f451357">

# Conclusion
We've proved that pumpkin spice popularity on Google is very seasonal and can be predicted. Between naive, SARMA models, and ETS models, ETS was better able to capture the relationship between time and Pumpkin Spice popularity. The multiplicative relationship of pumpkin spice to time implies that pumpkin spice's popularity is based on more than one independant variable besides time in the expression time * unknown_independant_var = pumpkin_spice_popularity. It also could represent the exponential influence that current pumpkin spice users are having on non pumpkin spice users to become pumpkin spice users, as it's more likley than the amount of pumpkin spice users remaining constant and googling pumpkin spice at exponentially increasing rates.

# Next steps
I'll come back to this project again in 2 weeks time and run a validation set on those two weeks of data.

# What I learned
In the future, if the seasonal decomposition is showing lower residuals for either a multiplicative or exponential model, I'll try an ETS before I try a SARIMA type of model, which are optimised for data where an additive model had lower residuals than the other two types. It will probably save me time and effort in the future.
