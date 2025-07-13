import numpy as np
import pandas as pd

# Assuming votingproximity and investingproximity are numpy arrays
n = votingproximity.shape[0]
print('n')
politicians = range(n)

# Create DataFrame
df = pd.DataFrame([(i, j, votingproximity[i, j], investingproximity[i, j])
                   for i in politicians for j in politicians if i != j],
                  columns=['Politician1', 'Politician2', 'VotingProximity', 'InvestingProximity'])

# Export to CSV
df.to_csv('proximity_data.csv', index=False)