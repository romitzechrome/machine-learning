import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print("_________________________________________seaborn")

# ----------------------------------------------------------------

# days = [1,2,3,4,5,6,7,8,9,10,11,12]
# temp= [32,36,36,23,26,25,36,35,34,36,40,42]

# temp_df = pd.DataFrame({"days":days,"temp":temp})

#      total_bill   tip     sex smoker   day    time  size
# 0         16.99  1.01  Female     No   Sun  Dinner     2
# 1         10.34  1.66    Male     No   Sun  Dinner     3
# 2         21.01  3.50    Male     No   Sun  Dinner     3
# 3         23.68  3.31    Male     No   Sun  Dinner     2
# 4         24.59  3.61  Female     No   Sun  Dinner     4
# ..          ...   ...     ...    ...   ...     ...   ...
# 239       29.03  5.92    Male     No   Sat  Dinner     3
# 240       27.18  2.00  Female    Yes   Sat  Dinner     2
# 241       22.67  2.00    Male    Yes   Sat  Dinner     2
# 242       17.82  1.75    Male     No   Sat  Dinner     2
# 243       18.78  3.00  Female     No  Thur  Dinner     2

# sns.lineplot(x = 'days',y = 'temp',data=temp_df)
# plt.show()

# ------------------------------------------------------------

# tips_df = sns.load_dataset('tips')
# print(tips_df)

# sns.lineplot(y ='total_bill',x = 'size',data=tips_df)
# plt.show()

# -------------------------------------------------------------------
# tips_df = sns.load_dataset('tips')
# print(tips_df)

# sns.lineplot(y ='total_bill',x = 'size',data=tips_df,hue='sex',style='sex',)
# plt.show()

#histogram   ----------------------------------------------------------------------

print("_____________________________histogram")


# tips_df = sns.load_dataset('tips')

# sns.distplot(tips_df['total_bill'])
# plt.show()

# heatmap-----------------------------------------------------------------------

arr2d = np.linspace(1,5,12).reshape(4,3)

print(arr2d)
# [[1.         1.36363636 1.72727273]
#  [2.09090909 2.45454545 2.81818182]
#  [3.18181818 3.54545455 3.90909091]
#  [4.27272727 4.63636364 5.        ]]

sns.heatmap(arr2d)
plt.show()






























