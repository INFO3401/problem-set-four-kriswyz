from utils import *
from poll import Poll

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
    #print("Change in poll for Sanders " + str(poll.changeInPoll("Sanders")))
    #print("Average in poll for Sanders " + str(poll.avgInPoll("Sanders")))
    #print("Median in poll for Sanders " + str(poll.medianInPoll("Sanders")))
    #print("Correlation between Sanders and Buttigieg " + str(poll.correlatedPolls("Sanders", "Buttigieg")))
    if pollCount > 1:
        print("Biden Polling Number: " + str(poll.avgInPoll("Biden")) + "+/-" + str(poll.pollUncertainty("Biden")))
        print("Sanders Polling Number: " + str(poll.avgInPoll("Sanders")) + "+/-" + str(poll.pollUncertainty("Sanders")))
    #print("Correlation between Sanders and Buttigieg " + str(poll.correlatedPolls("Sanders", "Buttigieg")))

#print(polls)
