import pandas as pd
import numpy as np
from prince import CA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data (replace this with your own dataset)
data = pd.DataFrame({
    'Category1': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Category2': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Count': [10, 20, 30, 15, 25, 35]
})

# One-hot encode categorical variables
data_encoded = pd.get_dummies(data[['Category1', 'Category2']])

# Perform correspondence analysis
ca = CA(n_components=3)
ca.fit(data_encoded)

# Get the row coordinates using the SVD results
row_coordinates = pd.DataFrame(ca.row_coordinates(data_encoded), index=data_encoded.index)

# Plot 3D correspondence analysis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot points (row coordinates)
ax.scatter(row_coordinates.iloc[:,0], 
           row_coordinates.iloc[:,1], 
           row_coordinates.iloc[:,2])

# Annotate points
for i, txt in enumerate(data_encoded.index):
    ax.text(row_coordinates.iloc[i,0], 
            row_coordinates.iloc[i,1], 
            row_coordinates.iloc[i,2], 
            txt, color='red')

# Set labels
ax.set_xlabel('Component 1')
ax.set_ylabel('Component 2')
ax.set_zlabel('Component 3')

# Save an image
plt.savefig('correspondence_map.png', dpi=300, bbox_inches='tight')

# Show plot
plt.show()
