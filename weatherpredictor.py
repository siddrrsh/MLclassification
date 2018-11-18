from sklearn import tree
features = [[35, 80, 0],[45, 85, 5],[75, 20, 60],[70, 25, 90]]
labels = [1,1,0,0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print(clf.predict([[40,65,4]]))
