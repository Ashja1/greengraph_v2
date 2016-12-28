#December 27, 2016, London
#Ashja

from matplotlib import pyplot as plt
from greengraph_code import Greengraph


mygraph = Greengraph('New York','Chicago')
data = mygraph.green_between(20)
plt.plot(data)
print(data)
#blah
