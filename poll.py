# A Poll object represents all polling data from a given outlet
import math
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

class Poll:
  # Start with a poll name and data
  def __init__(self, name, df):
    self.outlet = name
    self.data = df.loc[df['Poll']==name]

  # Return the most recent poll
  # Note that this assumes the data is already sorted by date from newest to oldest
  def getMostRecentPoll(self):
      return self.data.iloc[0]

  # Return the number of polls for this object
  def countPoll(self):
      return len(self.data)

  # Determine by what percent of the vote a candidate's position has changed
  def changeInPoll(self, candidate):
      candidateData = self.data[candidate]
      return candidateData.iloc[0] - candidateData.iloc[len(candidateData) - 1]

  # Compute the average number of votes a poll expects a candidate to get over time
  def avgInPoll(self, candidate):
      return self.data[candidate].mean()

  def medianInPoll(self, candidate):
      return self.data[candidate].median()

  def correlatedPolls(self, candidate1, candidate2):
      if (self.countPoll() == 1):
          print("Not enough data")
          return 0
      else:
          return self.data[candidate1].corr(self.data[candidate2])
#1：I think Joe Biden is going to win this. His winning probability goes higher and higher.          
#5:
  def normalizedData(df):
      x = df.copy()
      sumlist = []

      for i, row in x.iterrows():
        row.drop(items = ["Poll","Date","Sample","Spread"],inplace = True)
        print(row)
        sumlist.append(100-sum(row))
      x["Undecided"]=sumList
      print(x)
#6：
  normalizeData(df)
# print(plotCandidate)      
#7:
  def plotCandidate(slef,name):
      plot_df = plt.scatter(x=self.data.Poll, y=self.data[name])
      plt.show(plot.df)

#8:
  def statsPerCandidate(df,name):
      stats = df[name].mean()
      #print (statsPerCandidate)
      return stats      

  def pollUncertainty(self, candidate):
      # Standard Deviation
      #return self.data[candidate].std()

      # IQR
      #upperQuantile = self.data[candidate].quantile(.75)
      #lowerQuantile = self.data[candidate].quantile(.25)
      #return upperQuantile - lowerQuantile

      # Margin of error
      #n = self.countPoll()
      #sigma = self.data[candidate].std()
      #z = 1.96
      #return z * sigma / math.sqrt(n)

      # Confidence intervals
      npArray = 1.0 * np.array(self.data[candidate])
      stdErr = scipy.stats.sem(npArray)
      n = self.countPoll()
     return stdErr * scipy.stats.t.ppf((1+.95)/2.0, n - 1)


#9:
	def statsPerCandidate(df,candidate):
		return df[candidate].mean()     
#10:
    def cleanDate(df):
      sampleType = []
      sampleSize = []
      for i in df:
      	if "RV" in row["Sample"]:
        	sampleType.append("RV")
        elif "LV" in row["Sample"]:
        	sampleType.append("LV")
		df["Sample Type"] = sampleType
    	df["Sample Size"] = sampleSize
    	return df

#12:
def computePollWeight(df, poll):
    x = df["Poll"]
    SumOfX = sum(x["Sample Size"])
    y = sum(df["Sample Size"])
    return SumOfX/y

#13:
def weightedPerCandidate(candidate, df):
    weightedAverages = []
    for poll in df["Poll"].unique():
        x = sum([df["Poll"] == poll][candidate])
        y = computePollWeight(df, poll)
        weightedAverages.append(x*y)
    return sum(weightedAverages)/len(weightedAverages)

#15:
def computerCorrelation(candidate1, candidate2, df):
    return df[candidate1].corr(df[candidate2])

#17:
def superTuesday(df, candidates):
    BidenST = []
    SandersST = []

    for i, row in df.iterrows():
        BidenCount = row["Biden"]
        SandersCount = row["Sanders"]
        for candidate in candidates:
            if candidate != "Biden" and candidate != "Sanders":
                BidenCorr = computerCorrelation("Biden", candidate, df)
                SandersCorr = computerCorrelation("Sanders", candidate, df)
                if abs(BidenCorr) > abs(SandersCorr):
                    BidenCount += row[candidate]
                else:
                    SandersCount += row[candidate]
        BidenST.append(BidenCount)
        SandersST.append(SandersCount)

    df["BidenST"] = BidenST
    df["SandersST"] = SandersST

#19:
def pollUncertainty(self, candidate):
      # Standard Deviation
      #return self.data[candidate].std()

      # IQR
      #upperQuantile = self.data[candidate].quantile(.75)
      #lowerQuantile = self.data[candidate].quantile(.25)
      #return upperQuantile - lowerQuantile

      # Margin of error
      #n = self.countPoll()
      #sigma = self.data[candidate].std()
      #z = 1.96
      #return z * sigma / math.sqrt(n)

      # Confidence intervals
      npArray = 1.0 * np.array(self.data[candidate])
      stdErr = scipy.stats.sem(npArray)
      n = self.countPoll()
     return stdErr * scipy.stats.t.ppf((1+.95)/2.0, n - 1)


