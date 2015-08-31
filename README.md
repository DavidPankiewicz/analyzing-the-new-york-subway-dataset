# Analyzing and Drawing Conclusions from NYC Subway Ridership Data

Note: This project was completed for a Udacity course. The PDF of the writeup for Udacity is contained in the folder above. The information contained in this README contains the context needed for those unfamiliar with the supporting Udacity course.

## Introduction and Data
I explored a NYC subway ridership dataset as a means of answering the following question: 

*Does rain increase subway ridership?* 

The dataset was collect over the month of May 2011. Variables include day, time, subway data (subway station, number of riders entering a given station), and weather data from Weather Underground (rain, temperature, wind, and other weather factors). 
See [this Dropbox link](https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv) to download the data set.

## Methods
The first question I asked is whether the distribution of ridership under rainy conditions is any different than the distribution of ridership undery dry conditions. I first segmented my data on the binary variable "rain". After plotting the histograms of ridership under both conditions, it is clear that the data does not follow a Normal distribution, and thus we cannot use parametric tests to

We first set up  

In doing this, we look to set up a Null Hypotheses that these two sample come from the same distribution. 

Using the Mann-Whitney U test 


Given that we have established that the distributions are statistically different, we now must look to find what effect rain may be having on ridership. To examine the effects of rain, I built a regression model using gradient descent and a model using the `statsmodel` module API for ordinary least square (OLS). 

As expected, these models produced similar results. 

## Conclusions
Understanding data goes hand in hand with storytelling. Our initial hypothesis was that when there is rain, people prefer to take the subway (who likes getting caught in the rain?). However, based on the results of our regression, we see that the coefficient for rain is very small in comparison to other factors, meaning that the presence or lack of rain has small effects on ridership relative to other factors. 

Questions about data must fit within a story. 

## Limitations and Caveats
* Assumption on the Effects of Rain: For this analysis, we assume that rain causes more people to ride the subway instead of walking. However, it does not consider that there may be people who totally cancel their plans altogether and don't use any form of transporation, thus decreasing subway ridership. 
* Limited scope of time: the dataset contained is only for May 2011. Given that (1) the weather in NYC changes greatly over the course of the entire year and (2) we are trying answer a general question about rain and subway riderhsip during all times (and not constricted to only May 2011), our data may not be perfectly suited for the question we are trying to answer. 
* Structure of Analysis: The challenge with performing the analysis as given is that we are looking to predict subway ridership across the 
*

In our data set, 

