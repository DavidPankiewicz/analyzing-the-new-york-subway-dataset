# Analyzing and Drawing Conclusions from NYC Subway Ridership Data

## Executive Summary 
I analyzed data from the MTA on NYC subway ridership to test if more people ride the subway system on rainy days than dry days. Using statistical tests and graphic summaries, I conclude that while the distributions of ridership are different on a  statistically significant level (critical value of 0.05), the differences are very slight and do not make an appreciable difference on the subway system as a whole. It is worth noting that almost every other non-weather factor has a much stronger effect on ridership (e.g. location, time of day, etc.). Further segmenting of the data may be useful to test if specific stations are more affected by rain than others. 

## Objective
Note: This project was completed for a Udacity course. The PDF of the writeup for Udacity is contained in the folder above. The information contained in this README contains the context needed for those unfamiliar with the supporting Udacity course.   

As part of the Udacity course, I was asked to use this dataset to perform an analysis and writeup on the following question:
* *Does rain increase subway ridership?* 

While not examined in this analysis , there are a significant number of other questions one could explore with this dataset. Some examples:
* What times of day are the busiest?
* Is there a difference between weekday and weekend ridership?
* What are the most and least used subway stops?
* Do other factors have an effect on ridership?

## Data
The dataset comes from the NYC MTA. The raw data can be found on the MTA website here. An example file is uploaded at. The final clean csv file used for analysis can be found at [this Dropbox link](https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv). 

The dataset is limited to data collected from May 2011. Variables include day, time, subway data (subway station, number of riders entering a given station), and weather data from Weather Underground (rain, temperature, wind, and other weather factors).

## Hypothesis Testing
First, I wanted to see if ridership on rainy days follows a different distribution than ridership on dry days. I split the data based on the "rain" binary variable, and plotted a histogram of ridership for each sample. The histograms make it clear that ridership does not follow a normal distribution, ruling out the possibility of using a t-test to examine means.  Instead, I used the [Mann-Whitney U test](https://en.wikipedia.org/wiki/Mann–Whitney_U_test), a non-parametric test that makes no assumptions about the underlying distribution of the data. Using the SciPy library, 

Running the following code using the SciPy library, I got the following results:

Rain Day Mean: 1105.45
Dry Day Mean:  1090.28
1 sided p-value: 0.02499
2 sided p-value: 0.04998

Using a critical value of 0.05, we reject the null hypothesis that these two distributions are equal. It is noted that our p-value is only ever so slightly below 0.05. 

## Estimated Effects of Rain

Given that the distributions are different at a 0.05 critical value, I wanted to find out how much effect rain may be having on ridership. To do this, I built a linear regression with the data I had to model ridership. 

Given that we are seeing a statistically significant difference in the distributions of the two samples, I looked to estimate how much of a difference the presence of rain actually makes on ridership. To do this, I tested various linear regression models to estimate ridership. The best model achieved an R^2 of 0.4783. 

To check for multicollinearity, I removed variables I suspected to be correlated (e.g., "rain" and "precipi", the amount of precipitation). 

## Conclusions: Translating this Analysis to the Real World
An analysis of data must fit into context and a story. Our initial hypothesis (or story) is a situation where rain would cause people to take the subway who would otherwise be walking. However, based on the results of our regression, we see that the coefficient for rain is very small in comparison to other factors, meaning that the presence or lack of rain explains a tiny portion of variation in ridership compared to other factors. In other words, rain has little net effect on ridership. Reconsidering our story, this makes sense. Most New Yorkers take the subway as part of their normal routine regardless of the weather. Additionally, it would have to be raining very heavily for someone who would otherwise normally walk to instead pay and take the subway. Finally, while it seems there would be an increase in some people riding the subway because it's raining, some people may decide to stay home altogether if it's raining heavily enough, negating increased ridership. 

## Limitations and Caveats
* **Structure of analysis**: the subway system was analyzed as a whole, with the underlying assumptions that rain affects ridership equally across all stations. This is unlikely to be true in real life. Additionally, the scale of ridership wasn't adjusted for. Specifically, only changes in gross number of riders were analyzed, as opposed to measuring ridership against a benchmark for that specific station.  For example, it may not make sense to weigh the Times Square stop equally to an end of the line station.
* **Limited scope of time**: the dataset contained is only for May 2011. Given that (1) the weather in NYC changes greatly over the course of the entire year and (2) I am trying answer a general question about rain and subway ridership during all times (and not constricted to only May 2011), the data may not be representative for the question I am trying to answer. 

## Future Work
With more time, future work would include looking at more specific and niche questions. Are there certain subway stops that exhibit similar ridership? Why might that be? Is ridership different in Manhattan than Brooklyn? Does rain have a stronger effect at noon than 9pm? 

Although this data is very simple in nature, there are a number of significant questions one can answer with it. 

Most importantly, one should tie these questions back to real life: given what we learn from this analysis, what should we do about it?




