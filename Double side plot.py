# importing pandas module 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

print ("Give me the left side filename (In CSV format)")
file_name_left=input()
    
print ("Give me the right side filename (In CSV format)")
file_name_right=input()

#print ('Negative (-) or positive (+) power supply?')
#ps=input()
#column_tag=''
#if (ps=='-'):
#    ps='Negative'
#    column_tag='Neg'
#else:
#    ps='Positive' 
#    column_tag='Pos'

    
def reader(file_name, column_tag):
    global data
    global means
    global column_max
          
    # making data frame from csv file 
    data = pd.read_csv(file_name + '.csv') 

    # dropping passed columns 
    data.drop(["time", "Unix time"], axis = 1, inplace = True) 

    # dropping the row when HWienNeg:readVolt=0
    data.drop(data[data['HWien' + column_tag + ':readVolt'] == 0].index, inplace = True) # Colum_tag passes the value Neg or Pos to remove the readVolt=0 rows from the proper column

    # mean calculation and file appending
    means = data.groupby('HWien' + column_tag +':setVolt').mean()
    
    column_max = data['VIPK202cur'].max() # Gets the max of the VIPK202cur column
    
    return (data, means,column_max)

reader (file_name_left, 'Neg')
#print(data, means)
data_left = data
means_left = means
max_left = column_max
print(max_left)
#print(data_left, means_left)

reader (file_name_right, "Pos")
#print(data, means)
data_right = data
means_right = means
max_right = column_max
print(max_right)
#print(data_left, means_left)

#Plot the fixed file

#Define the size of the plot
plt.rcParams["figure.figsize"] = [20.5, 17]
plt.rcParams.update({'font.size': 40})

#plt.title(plate + " plate, " + ps + " power supply") 
plt.xlabel("Voltage [kV]") 
plt.ylabel("IP current [Normalized to 1]") 
#plt.ylim(0, 1) # plot y-axis limit
plt.plot(data_left['HWienNeg:readVolt']*(-1)/1000 , (data_left['VIPK202cur']/max_left) , "ob")
plt.plot(means_left['HWienNeg:readVolt']*(-1)/1000 , (means_left['VIPK202cur']/max_left) , color='red')
plt.plot(data_right['HWienPos:readVolt']/1000 , (data_right['VIPK202cur']/max_right) , "ob")
plt.plot(means_right['HWienPos:readVolt']/1000 , (means_right['VIPK202cur']/max_right) , color='red')
plt.grid(True) #Grid
plt.savefig(file_name_left + file_name_right + 'Normalized.png') #save plot to png file
plt.show() 


