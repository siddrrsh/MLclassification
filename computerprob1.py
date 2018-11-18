from sklearn import tree
features = [[4.5,0],[1.75,1],[4,0],[2,1]]
labels = [1,0,1,0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print(clf.predict([[3.75,0]]))

