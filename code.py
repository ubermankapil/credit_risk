import numpy as np
import pandas
import datetime
from datetime import strftime
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
import pydot
from IPython.display import Image

data = pandas.read_csv('/Users/ankit/data.csv', delimiter=',')
age = []
ref = datetime.datetime.strptime("30-Apr-14", "%d-%b-%y")
for d in dob:
        if type(d) == float:
            age.append(d)
        else:
        	dt = datetime.datetime.strptime(d, "%d-%b-%y")
            if dt.year > 2014 :
                dt = dt - datetime.timedelta(weeks=52*100)
                age_in_days = (ref - dt).days / 365
                age.append(age_in_days)

data['AGE'] = pandas.Series(age)
data.OD == None
data.OD.fillna(data.OD.mean())
new_data = data.dropna()
new_data[["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALUE RATIO)", "SECU_AMT", "AGE"]].values
train_X = new_data[["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALUE RATIO)", "SECU_AMT", "AGE"]].values
train_Y = new_date["FIELD VALUE"].values

clf = DecisionTreeClassifier()
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
graph = pydot.graph_from_dot_data(dot_data.getvalue())
raph[0].write_pdf("dtree.pdf")
clf = DecisionTreeClassifier(min_samples_leaf=20)
clf = clf.fit(train_X, train_Y)
tree.export_graphviz(clf, out_file=dot_data)
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALRATIO)", "SECU_AMT", "AGE"], filled=True, rounded=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree3.pdf")
clf = DecisionTreeClassifier(max_depth=3)
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALRATIO)", "SECU_AMT", "AGE"], filled=True, rounded=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree3.pdf")
clf = DecisionTreeClassifier(max_depth=4)























