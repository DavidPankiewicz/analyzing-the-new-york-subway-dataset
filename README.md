# Analyzing and Drawing Conclusions from NYC Subway Ridership Data

# Executive Summary 
I analyzed data from the MTA on NYC subway ridership to test if more people ride the subway system on rainy days than dry days. Using statistical tests and graphic summaries, I conclude that while the distributions of ridership are different at statistically significant level (critical value of 0.05), the differences are very slight and do not make an appreciable difference on the subway system as a whole. It is worth noting that almost every other non-weather factor has a much stronger effect on ridership (e.g. location, time of day, etc.). Further segmenting of the data may be useful to test if specific stations are more affected by rain than others. 

## Objective
Note: This project was completed for a Udacity course. The PDF of the writeup for Udacity is contained in the folder above. The information contained in this README contains the context needed for those unfamiliar with the supporting Udacity course.   

As part of the Udacity course, I was asked to use this dataset to perform an analysis and writeup on the following question:

* *Does rain increase subway ridership?* 

While not examined in this , there are a significant number of other questions one could explore with this dataset. Some examples:
* What times of day are the busiest?
* Is there a difference between weekday and weekend ridership?
* What are the most and least used subway stops?
* Do other factors have an effect on ridership?

## Data
The dataset comes from the NYC MTA. The raw data can be found on the MTA website here. (See these python files). The final clean csv file used for analaysis can be found at [this Dropbox link](https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv). 

The dataset is limited to data from May 2011. Variables include day, time, subway data (subway station, number of riders entering a given station), and weather data from Weather Underground (rain, temperature, wind, and other weather factors

### Hypothesis Testing
First, I wanted to see if ridership on rainy days follows a different distiribution than ridership on dry days. I split the data based on the "rain" binary variable, and plotted a historgram of ridership for each sample.  I examined the dsitused a must use a non-parametric test to examine whether these two samples come from the same distribution. To do this, I used the [Mann-Whitney U test](https://en.wikipedia.org/wiki/Mann–Whitney_U_test) using the SciPy library.

/// Makes n assumptions about underlying distribution of data

The resutls are as follows

Using a critical value of 0.05, we reject the null hypothesis that these two samples come from the same distribution. 

Other summary data seems to align 



### Estimated Effects of Rain

Given rain does appear to change ridership on a stati

Given that we have established that the distributions are statistically different, we now must look to find what effect rain may be having on ridership. To examine the effects of rain, I built a regression model using gradient descent and a model using the `statsmodel` module API for ordinary least square (OLS). 

As expected, these models produced similar results. 


Given that are we seeing a statistically significant difference in the distributions of the two samples, I looked to estimate how much of a difference the presence of rain actually makes on ridership. To do this, I tested various linear regression models to estimate ridership. The best model achieved an R^2 of 0.4783. 

To check for multicollinearity, I removed variables I suspected to be correlated (e.g., "rain" and "precipi", the amount of precipitation). Also, to test for significance of the variable in the model, I 

## Conclusions
Understanding data goes hand in hand with storytelling. Our initial hypothesis on the situation was that when there is rain, people prefer to take the subway (who likes getting caught in the rain?). However, based on the results of our regression, we see that the coefficient for rain is very small in comparison to other factors, meaning that the presence or lack of rain has small effects on ridership relative to other factors. 

Questions about data must fit within a story. 

## Limitations and Caveats
* Assumption on the Effects of Rain: For this analysis, we assume that rain causes more people to ride the subway instead of walking. However, it does not consider that there may be people who totally cancel their plans altogether and don't use any form of transporation, thus decreasing subway ridership. 
* Limited scope of time: the dataset contained is only for May 2011. Given that (1) the weather in NYC changes greatly over the course of the entire year and (2) we are trying answer a general question about rain and subway riderhsip during all times (and not constricted to only May 2011), our data may not be perfectly suited for the question we are trying to answer. 
* Structure of Analysis: The challenge with performing the analysis as given is that we are looking to predict subway ridership across the 
*



