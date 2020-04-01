from utils import *
from candidate import Candidate

endorsements = loadAndCleanData("endorsements-2020.csv")
#print(endorsements)

#Create a set of candidate in endorsement

candidates = {}
candidateNames = pd.unique(endorsements["endorsee"])

for candidate in candidateNames:
	if type(candidate) != str:
		continue
	c = (candidate, endorsements)	
	if (c.countEndorsements) > 10:
		candidates[candidate] = c
		print(candidate +"has" + str(c.countEndorsements()) +"endorsements")
