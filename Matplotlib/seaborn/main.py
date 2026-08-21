import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# sns.get_dataset_names() # list of built-in datasets
# iris = sns.load_dataset("iris") # default built-ins
tips = sns.load_dataset("tips")
sns.set_theme(style='darkgrid') # makes grid with grey background

# Figure level functions and axis level functions;

# scatterplot, is an axis level function, one axis, one visualization
#sns.scatterplot(x="total_bill", y="tip", data=tips, hue="sex", size="size", style="smoker") # hue is differentiation by color and type, and size is differentiation by size, (hue, size, and smoker are all in legend)

# lineplot
dow_data = sns.load_dataset("dowjones")
#sns.lineplot(x="Date", y="Price", data=dow_data)

# relplot, does the same as scatterplot but we can use it with different kind, and we can have multiple plots in one figure. It can be multipleplot, scatter, as well as line [hence, can be used as different kinds]
#sns.relplot(x="total_bill", y="tip", data=tips, hue="day", size="size", style="smoker",col="sex",  col_wrap=2, kind="scatter") 
# col="day" different graphs for each sex, col_wrap=2 show graphs as 2 by 2 insetad of the default


# DIStribution plots
# sns.distplot(crash_df("not_distracted")) distplot is deprecated, and replaced with displot and histplot
#sns.displot(tips, x='tip', col='sex', kind='hist') # can do directly sns.histplot() without the kind. But we can split plots in displot based on a feature, which can't be possible in histplot. However, we can do sns.histplot(tips, x='tip', heu="sex") to highlight different genders with different colors in one histplot. 

# kdeplot
#sns.kdeplot(tips, x='tips', y='total_bill', fill=True, hue='day') # fill to fill the contour with color

# ecdfplot
#sns.ecdfplot(tips, x='tip')

# rugplot, can't be used alone, is used in a histogram
#sns.displot(tips, x='tip', kind='hist')
#sns.rugplot(tips, x='tip', color='red') # plots individual data points onto the histogram. Not just the density, it also shows the actual values.

# catplot, figure level function
#sns.catplot(tips, x='tip', y='day', kind='strip', hue='sex') # some alternative, stripplot, swarmplot(same but values vertically lined up)

# boxplot, shows the median, different quantiles and some outliers, min and max
#sns.boxplot(tips, x='tip', y='day') # alternative, violinplot shows the distribution in curvature, boxenplot

# barplot
#sns.barplot(tips, x='day', y='tip', hue='sex') # alternative, countplot

# pointplot
#sns.pointplot(tips, x='tip', y='day', hue='sex')

# jointplot, scatterplot with histogram
#sns.jointplot(tips, x='total_bill', y='tip' )

# pairplot, plots all the numerical data against one another. If they're not processed they're not going to be used. 
#sns.pairplot(tips)

# heatmap
'''titanic = sns.load_dataset('titanic')
# pandas cleaning for non numericals
titanic.sex = titanic.sex.apply(lambda x: 1 if x == 'male' else 0)
titanic.alive = titanic.alive.apply(lambda x: 1 if x == 'yes' else 0)
titanic.alone = titanic.alone.apply(lambda x: 1 if x else 0)
titanic['class'] = titanic['class'].astype(pd.CategoricalDtype(categories=['First', 'Second', 'Third'], ordered=True)).cat.codes
titanic = titanic.drop(['embarked', 'who', 'adult_male', 'deck', 'embark_town'], axis=1)
plt.figure(figsize=(12,8))
sns.heatmap(titanic.corr(), annot=True, cmap='coolwarm')'''

# clustermap
iris = sns.load_dataset('iris')
#sns.clustermap(iris.drop('species', axis=1)) # y axis everyline is a row and every coloumn is a feature

# Regression plots
# lmplot, performs linear regression. Figure level function
#sns.lmplot(tips, x='total_bill', y='tip', hue='sex', col='day')

# regplot. Axes level function
#sns.regplot(tips, x='total_bill', y='tip')

plt.show()