import pandas as pd

import math
import numpy as np
import scipy.stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

def helloWorld():
  print("Hello, World!")

def loadAndCleanData(filename):
    data = pd.read_csv(filename)
    data.fillna(0)
    #print(data)
    return data

def counputePDF(feature, data):
	data[feature].plot.kde()
	plt.show()

def viewDistribution(feature,data):
	data[feature].hist()
	plt.show()

def viewLogDistribution(viewDistribution, data):
    data[viewDistribution].hist()
    plt.show()
    
def computeProbability(feature, bin, data):
    # Count the number of datapoints in the bin
    count = 0.0

    for i,datapoint in data.iterrows():
        # See if the data is in the right bin
        if datapoint[feature] >= bin[0] and datapoint[feature] < bin[1]:
            count += 1

    # Count the total number of datapoints
    totalData = len(data)

    # Divide the number of people in the bin by the total number of people
    probability = count / totalData

    # Return the result
    return probability

def computeConfidenceInterval(data):
      # Confidence intervals
      npArray = 1.0 * np.array(data)
      stdErr = scipy.stats.sem(npArray)
      n = len(data)
      return stdErr * scipy.stats.t.ppf((1+.95)/2.0, n - 1)

def getEffectSize(d1,d2):
    m1 = d1.mean()
    m2 = d2.mean()
    s1 = d1.std()
    s2 = d2.std()

    return (m1 - m2) / math.sqrt((math.pow(s1, 3) + math.pow(s2, 3)) / 2.0)

def runTTest(d1,d2):
    return scipy.stats.ttest_ind(d1,d2)

# pip install statsmodels
# vars is a string with our independent and dependent variables
# " dvs ~ ivs"
def runANOVA(dataframe, vars):
    model = ols(vars, data=dataframe).fit()
    aov_table = sm.stats.anova_lm(model, typ=2)
    return aov_table 

    
def getConfidenceIntervals(datacolumn):
	npArray = 1.0 * np.array(datacolumn)
	stdErr = scipy.stats.sem(npArray)
	n = len(datacolumn)
	return stdErr * scipy.stats.t.ppf((1+.95)/2.0,n-1)   
