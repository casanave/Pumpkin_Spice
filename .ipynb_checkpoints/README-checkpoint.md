# Pumpkin_Spice
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

# Conclusion
We've proved that pumpkin spice popularity on Google is very seasonal and can be predicted. Between naive, SARMA models, and ETS models, ETS was better able to capture the relationship between time and Pumpkin Spice popularity. The multiplicative relationship of pumpkin spice to time implies that pumpkin spice's popularity is based on more than one independant variable besides time in the expression time * unknown_independant_var = pumpkin_spice_popularity. It also could represent the exponential influence that current pumpkin spice users are having on non pumpkin spice users to become pumpkin spice users, as it's more likley than the amount of pumpkin spice users remaining constant and googling pumpkin spice at exponentially increasing rates.

# Next steps
I'll come back to this project again in 2 weeks time and run a validation set on those two weeks of data.

# What I learned
In the future, if the seasonal decomposition is showing lower residuals for either a multiplicative or exponential model, I'll try an ETS before I try a SARIMA type of model, which are optimised for data where an additive model had lower residuals than the other two types. It will probably save me time and effort in the future.
