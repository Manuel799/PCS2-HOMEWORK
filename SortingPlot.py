#My Plot for Sorting
import matplotlib.pyplot as plt
plt.plot([0.0001486869999999807, 0.002111033999999984,0.026823032999999996,0.549024416],label='QuickSort')
plt.plot([0.0002937759999999956, 0.0002937759999999956, 0.08703789, 1.1702217490000002], label ='MergeSort')
plt.annotate('QuickSort', xy = (2.6,0.25), xytext =  (2.65,0.015), arrowprops= dict(facecolor = 'red', shrink = 0.05))
plt.annotate('MergeSort', xy = (2.2,0.57), xytext =  (1.5,0.75), arrowprops= dict(facecolor = 'green', shrink = 0.05))
plt.ylabel('Time')

plt.title('My Plot')

plt.show()


