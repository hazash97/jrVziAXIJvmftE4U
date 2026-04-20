#Correlation Matrix

raw_data = getData('Raw Data')

correls = raw_data.corr().round(2)

import seaborn as sb
heatmap = sb.heatmap(correls,annot=True)
