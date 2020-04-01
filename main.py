from utils import *
from poll import Poll
#work with Ziyang Zhang, Kat Anderson

# Use your utils function to load in the data
df = loadAndCleanData("2020_democratic_presidential_nomination-6730.csv")

# Create a list of poll objects from my dataframe
pollNames = pd.unique(df["Poll"])
print(pollNames)

# Create a new object for each poll and print its properties
polls = []
for name in pollNames:
    poll = Poll(name, df)
    polls.append(poll)
    print(poll.outlet)
    #print(poll.getMostRecentPoll())
    pollCount = poll.countPoll()
    print("Number of polls: " + str(pollCount))
    print("Change in poll for Sanders " + str(poll.changeInPoll("Sanders")))
    print("Average in poll for Sanders " + str(poll.avgInPoll("Sanders")))
    print("Median in poll for Sanders " + str(poll.medianInPoll("Sanders")))
    print("Correlation between Sanders and Buttigieg " + str(poll.correlatedPolls("Sanders", "Buttigieg")))
    print("Correlation between Sanders and Buttigieg " + str(poll.correlatedPolls("Sanders", "Buttigieg")))
    print(poll.plotCandidate("Sanders"))
    print(poll.plotCandidate("Biden","Bloomberg","Warren","Buttigieg","Klobucahr","Steyer","Gabbard"))

print(statsPerCandidate(df,"Sanders"))

    if (pollCount > 1):
        print("Biden's Polling Numbers: " + str(poll.avgInPoll("Biden")) + " +/- " + str(poll.pollUncertainty("Biden")))

        print("Sanders' Polling Numbers: " + str(poll.avgInPoll("Sanders")) + " +/- " + str(poll.pollUncertainty("Sanders")))

#print(polls)
#6:
normalizeData(df)
#7:
for candidate in df.columns:
	if candidate not in ["Poll","Date","Sample","Spread"]:
		plotCandidate(candidate,df)


#9:
myPeople = []
for candidate in df.columns:
	if candidate not in ["Poll","Date","Sample","Spread"]:
		myPeople.append(candidate)
		print(candidate,statsPerCandidate(candidate,df))

#11:			
df = cleanSample(df)
print(cleanSample)

print(computePollWeight(df,"poll"))

#14:
for candidate in myPeople:
	print(candidate,":",weightedStatsPerCandidate(candidate,df))

#16:
myList = []

for candidate1 in myPeople:
	for candidate2 in myPeople:
		if candidate1 != candidate2:
			if [candidate1,candidate2] not in myList and [candidate2,candidate1] not in myList:
				print(candidate1,"vs",candidate2,":",computeCorrelation(candidate1,candidate2,df))
				myList.append([candidate1,candidate2])

print(str(candidate1) +" and "+str(candidate2)+"are the most correlated.")
print(str(candidate1) +" and "+str(candidate2)+"are the least correlated.")

#18:
superTuesdat(df,myPeople)
print("Biden's mean",df["BidenST"].mean())
print("Sanders' mean",df["SndersST"].mean())
print("Biden's weighted mean",weightedStatsPerCandidate("BidenST",df))
print("Sanders' weighted mean",weightedStatsPerCandidate("SandersST",df))
#Biden will win

#19:
print("Biden:",getConfidenceIntervals(df["BidenST"]))
print("Sanders:",getConfidenceIntervals(df["SandersST"]))
print("Difference:",(getConfidenceIntervals(df["BidenST"])-getConfidenceIntervals(df["SandersST"])))

#20:
print("First",runTTest(df["Biden"],df["Sanders"]))
print("Second",runTTest(df["BidenST"],df["SandersST"]))



