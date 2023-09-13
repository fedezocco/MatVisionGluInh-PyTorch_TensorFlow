""" 
Implemented by Federico Zocco
Last update: 13 September 2023

This script converts the coordinate labels into an .npy 
data file, which will be the target in regression.
Each pair (xi, yi) refers to the point Pi. Here, I am
considering two points P1 and P2.

The coordinate zi is constant and the same for P1 and P2, 
hence it is not included in the training.

This script has been used to generate "InhPoints_50labels.npy" for
the training notebook "InhPoints_training.ipynb".  

Refer to "InhPoints_training.ipynb" for more info.      
"""

import numpy as np
labels = np.array([[4.9,6.9,2.5,7.9], # [x1, y1, x2, y2]
                   [7.6,5.4,5.9,7.0], 
                   [5.0,7.0,3.0,5.9], 
                   [10.0,5.0,12.5,6.0],
                   [16.5,4.2,15.4,6.8],
                   [23.5,5.9,21.8,4.4],
                   [25.8,5.0,27.9,3.5],
                   [32.9,5.7,30.8,4.0],
                   [36.9,5.0,36.9,7.5],
                   [36.2,5.2,38.4,3.5],
                   [3.0,9.8,5.1,8.8],
                   [8.0,11.4,8.5,9.0],
                   [15.1,11.0,12.9,12.0],
                   [21.3,10.9,23.9,11.8],
                   [23.8,12.0,23.8,9.3],
                   [30.0,12.4,27.3,12.2],
                   [34.2,13.2,32.8,11.1],
                   [36.5,10.1,38.0,12.1],
                   [22.4,13.0,25.0,13.0],
                   [8.0,12.0,5.5,12.1],
                   [4.5,17.6,6.8,12.0],
                   [7.1,19.0,9.1,17.1],
                   [13.0,15.6,11.1,17.2],
                   [16.9,15.6,14.5,15.0],
                   [20.0,18.0,19.0,15.5],
                   [23.0,17.6,20.8,19.0],
                   [24.0,16.2,24.0,19.0],
                   [25.9,17.9,27.9,19.3],
                   [33.2,19.1,31.0,18.0],
                   [34.9,21.0,34.0,18.5],
                   [38.0,23.5,40.2,24.5],
                   [4.5,27.0,6.9,27.9],
                   [7.2,27.2,8.5,29.4],
                   [12.0,29.1,13.8,27.4],
                   [13.9,27.3,13.0,24.8],
                   [13.8,27.3,13.0,24.8],
                   [22.5,25.5,20.6,27.5],
                   [29.0,27.6,29.0,24.9],
                   [32.0,25.0,29.7,27.0],
                   [35.8,26.5,38.0,25.0],
                   [23.4,21.0,25.2,19.2],
                   [13.5,30.0,11.2,31.0],
                   [23.9,35.9,26.2,35.4],
                   [35.1,27.5,29.0,33.0],
                   [32.2,34.0,34.0,36.0],
                   [14.7,34.9,12.4,33.9],
                   [9.0,34.7,8.1,32.1],
                   [19.5,34.9,22.0,35.3],
                   [15.0,20.0,21.6,17.0],
                   [20.1,21.8,22.5,23.0]])