from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn import metrics

iris = datasets.load_iris()
print(iris.target_names)

print(iris.feature_names)

X,y = datasets.load_iris(return_X_y= True)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

data = pd.DataFrame({'sepallength':iris.data[:,0],'sepalwidth':iris.data[:,1],
                     'petallength':iris.data[:,2],'petalwidth':iris.data[:,3],
                     'species':iris.target
                     })

print(data.head())

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)

y_pred =clf.predict(X_test)

print(f"Dokładność modelu: {metrics.accuracy_score(y_test,y_pred)}")

print(clf.predict([[3,3,2,2]]))




