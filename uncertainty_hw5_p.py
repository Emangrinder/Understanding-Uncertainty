# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

# %%

with open('taxicab.pkl', 'rb') as f:
    data = pickle.load(f)

print(len(data))
data[0]

# %%

## Extract state space
states = set(data[0])
for i in range(1,len(data)):
    trip_i = set(data[i])
    states = states.union(trip_i)
states = list(states)

# %%

## Compute transition counts

S = len(states)
tr_counts = np.zeros( (S, S))
        
## Compute transition counts:

for trip in data:
    trip = np.array(trip)
    for t in range(1, len(trip)):
        x_tm1 = trip[t-1]
        x_t = trip[t]
        
        index_from = states.index(x_tm1)
        index_to = states.index(x_t)
        
        tr_counts[index_from, index_to] += 1

print("Transition Counts:\n", tr_counts)

# %%
sums = tr_counts.sum(axis=0, keepdims=True)
print('State proportions: \n')
print(sums)

# %%

## Normalize the transition count matrix to get proportions
tr_pr = np.divide(tr_counts, sums, 
            out=np.zeros_like(tr_counts), 
            where=sums!=0)

print("Transition Proportions:\n")
tr_df = pd.DataFrame(np.round(tr_pr, 2), index=states, columns=states)
print(tr_df)

plt.figure(figsize=(12, 10))
sns.heatmap(tr_df, 
            cmap='Blues',
            square=True,
            xticklabels=states,
            yticklabels=states,
            annot=True)
plt.show()