from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load data
covid_df = pd.read_csv("Covid Dataset.csv")

# encode data into 1s and 0s (1=yes 0=no)
label_encoder = LabelEncoder()
for x in range(21):
  	covid_df.iloc[:,x] = label_encoder.fit_transform(covid_df.iloc[:,x].values)

#split data into training and testing
X = covid_df.drop(["COVID-19"], axis=1).values
y = covid_df["COVID-19"].values                 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42, stratify = y)

#init model and find best parameters using gridsearchCV
knn = KNeighborsClassifier()
param_grid = {"n_neighbors": np.arange(1,50)}
knn_cv = GridSearchCV(knn, param_grid, cv=5)
knn_cv.fit(X_train, y_train)
n_param = knn_cv.best_params_["n_neighbors"]


def get_predict(features_list):
	arr = np.array(features_list)
	arr = arr.reshape(1, -1)
	r = knn_cv.predict(arr)
	result = int(r[0])

	# yes=1 and no=0
	return result