# Python script to determine Euclidean Distance between the options
from math import *

import numpy


def euclidean_distance(x,y):
  return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

from pandas import *

alternatives = ['AppEEARS','Field Campaign Explorer (FCX)','OpenAltimetry','Data Access Tool','Operation IceBridge Portal','Vertex','Earthdata Search','SOOT','Airborne Data Visualizer','Giovanni','Worldview']

data = read_csv('acw-scores-fitness_only.csv')
vectors = {}
for x in alternatives:
  vectors[x] =  data[x].tolist()

results =  numpy.zeros((11, 11))



# Iterate over the whole things
for i,k in enumerate(vectors.keys()):
  for j, alternative in enumerate(alternatives):
    if k == alternative:
      score = 0
    else:
      # ok, normally euclidean distance is the same regardless of rodering, but in the case
      # where a tool has more functionality than another tool, then we want the scores to be
      # different. So we take the tool we're examining and remove all '0's, or capabilities
      # it doesn't have, remove those from the comparison tool, and then calculate 'distance'.
      # In the case of higher overlaps, we get a smaller number. When we compute the inverse
      # relationship- the tool with many capabilities and the comparison tool without them,
      # there will be A) more comparisons and B) a larger resulting number, signifying that 
      # it's harder to converge one way vs the other.

      idxlist = numpy.nonzero(vectors[k])[0]
      temp_vector = [vectors[k][idx] for idx in idxlist]
      temp_alternative = [vectors[alternative][idx] for idx in idxlist]

      score = euclidean_distance(temp_vector,temp_alternative)
    results[i][j] = score


# print(results)
df = DataFrame(results, alternatives, alternatives)
#df = DataFrame(results, columns =alternatives, rows=alternatives) 
print("\nPandas DataFrame: ") 
print("Find a tool by the column, and the numbers indicate how far away the column-based tool is from meeting the row-based tools functionalities. Lower means closer to meeting its needs")
print(df) 


