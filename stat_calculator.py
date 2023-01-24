import numpy as np


#Create a function that can will calculate statistic data for a given list of nrs and output in a dictionary format
def calculate(list):

#raise an error if the size of the list is less than 9 numbers
    if len(list) < 9:
        raise ValueError("The list must contain nine numbers.")

    #Convert the list to a 3x3 matrix
    matrix = np.array(list).reshape(3, 3)


    #Mean, variance, standard deviation, min and max calculations and convert from array to a list format
   
    mean_ax0 = np.mean(matrix, axis=0).tolist()
    mean_ax1 = np.mean(matrix, axis=1).tolist()
    flattened_mean = np.mean(matrix.flatten())
    
    variance_ax0 = np.var(matrix, axis=0).tolist()
    variance_ax1 = np.var(matrix, axis=1).tolist()
    flattened_var = np.var(matrix.flatten())
  
    stdDev_ax0 = np.std(matrix, axis=0).tolist()
    stdDev_ax1 = np.std(matrix, axis=1).tolist()
    flattened_std = np.std(matrix.flatten())
   
    maxValue_ax0 = np.max(matrix, axis=0).tolist()
    maxValue_ax1 = np.max(matrix, axis=1).tolist()
    flattened_max = np.max(matrix.flatten())
   
    minValue_ax0 = np.min(matrix, axis=0).tolist()
    minValue_ax1 = np.min(matrix, axis=1).tolist()
    flattened_min = np.min(matrix.flatten())
    sumRows = np.sum(matrix, axis=1).tolist()
    sumCol = np.sum(matrix, axis=0).tolist()
    flattened_sum = np.sum(matrix.flatten())

    output = {'mean': [[mean_ax0[0], mean_ax0[1], mean_ax0[2]], [mean_ax1[0], mean_ax1[1], mean_ax1[2]], flattened_mean],
              'variance': [[variance_ax0[0], variance_ax0[1], variance_ax0[2]], [variance_ax1[0], variance_ax1[1], variance_ax1[2]], flattened_var],
              'standard deviation': [[stdDev_ax0[0], stdDev_ax0[1], stdDev_ax0[2]], [stdDev_ax1[0], stdDev_ax1[1], stdDev_ax1[2]], flattened_std],
              'max': [[maxValue_ax0[0], maxValue_ax0[1], maxValue_ax0[2]], [maxValue_ax1[0], maxValue_ax1[1], maxValue_ax1[2]], flattened_max],
              'min': [[minValue_ax0[0], minValue_ax0[1], minValue_ax0[2]], [minValue_ax1[0], minValue_ax1[1], minValue_ax1[2]], flattened_min],
              'sum': [[sumCol[0], sumCol[1], sumCol[2]], [sumRows[0], sumRows[1], sumRows[2]], flattened_sum]}
    return output

result = calculate([2,6,2,8,4,0,1,5,7])

print(result)
