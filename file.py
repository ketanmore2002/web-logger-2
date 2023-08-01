#***K-Means***

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/content/Mall_Customers.csv')
df.head(6)

#Select the annual income and the spending score columns
X = df.iloc[:, [3,4]].values


# KMeans class from the sklearn library.
from sklearn.cluster import KMeans

wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters=i)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

# print(wcss)
plt.plot(range(1,11),wcss)
plt.show()

kmeans = KMeans(n_clusters=5)

y_kmeans = kmeans.fit_predict(X)
y_kmeans

df['cluster'] = y_kmeans
df.head(5)

#6 Visualising the clusters
plt.scatter(X[y_kmeans==0, 0], X[y_kmeans==0, 1], s=100, c='red', label ='Cluster 1')
plt.scatter(X[y_kmeans==1, 0], X[y_kmeans==1, 1], s=100, c='blue', label ='Cluster 2')
plt.scatter(X[y_kmeans==2, 0], X[y_kmeans==2, 1], s=100, c='green', label ='Cluster 3')
plt.scatter(X[y_kmeans==3, 0], X[y_kmeans==3, 1], s=100, c='cyan', label ='Cluster 4')
plt.scatter(X[y_kmeans==4, 0], X[y_kmeans==4, 1], s=100, c='magenta', label ='Cluster 5')

#Plot the centroid. This time we're going to use the cluster centres
#attribute that returns here the coordinates of the centroid.
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label = 'Centroids')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income(k$)')
plt.ylabel('Spending Score(1-100)')
plt.show()

# **Hirarchical clustering**

import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogam', fontsize = 20)
plt.xlabel('Customers')
plt.ylabel('Ecuclidean Distance')
plt.show()

from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)


plt.scatter(X[y_kmeans==0, 0], X[y_kmeans==0, 1], s=100, c='red', label ='Cluster 1')
plt.scatter(X[y_kmeans==1, 0], X[y_kmeans==1, 1], s=100, c='blue', label ='Cluster 2')
plt.scatter(X[y_kmeans==2, 0], X[y_kmeans==2, 1], s=100, c='green', label ='Cluster 3')
plt.scatter(X[y_kmeans==3, 0], X[y_kmeans==3, 1], s=100, c='cyan', label ='Cluster 4')
plt.scatter(X[y_kmeans==4, 0], X[y_kmeans==4, 1], s=100, c='magenta', label ='Cluster 5')

#Plot the centroid. This time we're going to use the cluster centres
#attribute that returns here the coordinates of the centroid.
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label = 'Centroids')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income(k$)')
plt.ylabel('Spending Score(1-100)')
plt.show()

# **Apriori Algo**

!pip install apyori

import pandas as pd
import numpy as np
from apyori import apriori

df = pd.read_csv('/content/Market_Basket_Optimisation.csv')
df.head(5)

df.fillna(0,inplace=True)
columns_except_last = df.columns[:-1]
df = df[columns_except_last]
df

transactions = []

for i in range(0,len(df)):
    transactions.append([str(df.values[i,j]) for j in range(0,19) if str(df.values[i,j])!='0'])

rules = apriori(transactions, min_support=0.003, min_confidance=0.2, min_lift=3, min_length=2)
Results = list(rules)
Results

for item in Results:
  pair=item[0]
  items = [x for x in pair]

  print('Rule:' + items[0]+ ' -> ' + items[1])

  print('Support: '+ str(item[1]))
  print('Confidence: '+ str(item[2][0][2]))
  print('Lift: '+ str(item[2][0][3]))
  print('========================================')

# **Rainforcemrnt Learning**

import numpy as np

state_to_index = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4}
indes_to_state = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}

reward_matrix = np.array([
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0]
    ])

reward_matrix


gamma = 0.95 # Discount factor
alpha = 0.1  # Learning rate

state_size = len(state_to_index)
action_size = len(indes_to_state)
Q_matrix = np.zeros([state_size, action_size])
Q_matrix

def q_learning_updates(s, a, reward, s2, Q_matrix):
  Q_matrix[s, a] = (1 - alpha) * Q_matrix[s, a] + alpha*(reward + gamma * np.max(Q_matrix[s2, :]))
  s=s2
  return s, Q_matrix


def get_action(state, Q_matrix, epsilon=0.1):
  if np.random.random() < epsilon:
    return np.random.choice(action_size)
  else:
    return np.argmax(Q_matrix[state, :])



def find_optimal_route(initial_state, goal_state, Q_matrix, episodes=1000):
    for _ in range(episodes):
        state = initial_state
        while state != goal_state:
            action = get_action(state, Q_matrix)
            next_state = action
            reward = reward_matrix[state, action]
            state, Q_matrix = q_learning_updates(state, action, reward, next_state, Q_matrix)

    return Q_matrix


initial_state = state_to_index['A']
goal_state = state_to_index['E']

Q_matrix = find_optimal_route(initial_state, goal_state, Q_matrix)
print(Q_matrix)

optimal_actions = [np.argmax (Q_matrix[state, ]) for state in range(state_size)]
optimal_actions = [indes_to_state[action] for action in optimal_actions]
print("Optimal Actions for each state:", optimal_actions)

for state in state_to_index:
  for action in state_to_index:
    state_idx= state_to_index[state]
    action_idx= state_to_index [action]
    immediate_reward = reward_matrix[state_idx, action_idx]
    print (f"Immediate Reward for moving from state {state} to state {action}: {immediate_reward}")

action_sequence = ['A', 'B', 'C', 'D', 'E']
discounted_reward = 0
current_gamma = 1
for i in range(len(action_sequence) - 1):
  state = state_to_index[action_sequence[i]]
  next_state = state_to_index [action_sequence[i+1]]
  reward = reward_matrix[state, next_state]
  discounted_reward += current_gamma * reward
  current_gamma *= gamma
print("Discounted Reward for the action sequence:", discounted_reward)

# **Time serese Analyis**

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
#Load the Air Passengers dataset
series = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv', header=0, index_col=0)

series

def check_stationary (series):
  result = adfuller (series)
  print('ADF Statistic: %f' % result[0])
  print('p-value: %f' % result[1])
  print('Critical Values:')
  for key, value in result[4].items():
    print('\t%s: %.3f' % (key, value))


check_stationary (series)

def make_stationary (series):
  stationary_series = series.diff().dropna()
  return stationary_series

stationary_series = make_stationary (series)

check_stationary (stationary_series)

plot_acf(stationary_series)
plot_pacf(stationary_series)
plt.show()

#Plot the original time series:
plt.figure(figsize=(10, 6))
plt.plot(series.index, series["Passengers"])
plt.title("Airline Passengers")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.show()

# !pip install pmdarima
import pmdarima as pm
auto_model = pm.auto_arima (series, seasonal=False, stepwise=True, suppress_warnings=True, trace=True, error_action='ignore', information_criterion='aic')
print("Optimal (p, d, q) values:", auto_model.order)

from statsmodels.tsa.arima.model import ARIMA
model = ARIMA (series, order=(4, 1, 3))
model_fit = model.fit()
# Plot the stationary series and fitted values
plt.figure(figsize=(10, 6))
plt.plot(stationary_series, label="Actual")
plt.plot(model_fit.fittedvalues, color='red', label="ARIMA")
plt.title("ARIMA Airline Passengers")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.legend()
plt.show()

forecast = model_fit.forecast(steps=10)
print("Forecasted values: \n", forecast)

# **Boosting**

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

iris = load_iris()

X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = AdaBoostClassifier(n_estimators=50, learning_rate=1, random_state=42)
cv_scores = cross_val_score (clf, X_train, y_train, cv=5)
print("Cross-validation scores: ", cv_scores)
print("Mean cross-validation score:", cv_scores.mean())



clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score (y_test, y_pred)
print("Test set accuracy:", accuracy)


n_estimators_values = [10, 50, 100, 500, 1000, 5000]
CV_scores_mean = []

for n_estimators in n_estimators_values:
    clf = AdaBoostClassifier(n_estimators=n_estimators, learning_rate=1, random_state=42)
    CV_scores = cross_val_score(clf, X_train, y_train, cv=5)
    CV_scores_mean.append(CV_scores.mean())

plt.plot(n_estimators_values, CV_scores_mean, marker='o')
plt.xlabel('Number of Trees')
plt.ylabel('Mean Cross-Validation Score')
plt.title('AdaBoost Performance with Different Numbers of Trees')
plt.show()

learning_rates = np.linspace(0.1, 2, 20)
CV_scores_mean = []

for learning_rate in learning_rates:
    clf = AdaBoostClassifier(n_estimators=50, learning_rate=learning_rate, random_state=42)
    CV_scores = cross_val_score(clf, X_train, y_train, cv=5)
    CV_scores_mean.append(CV_scores.mean())

plt.plot(learning_rates, CV_scores_mean, marker='o')
plt.xlabel('Learning Rate')
plt.ylabel('Mean Cross-Validation Score')
plt.title('AdaBoost Performance with Different Learning Rates')
plt.show()

# **Deep Learning**

# Loading dataset into keras pttoarch and train test split

import pandas as pd

df = pd.read_csv('/content/tts.csv')

df

X = df.iloc[:,[0]]
y = df.iloc[:,[1]]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=24)

print('X_train: \n',X_train)
print('X_test: \n',X_test)
print('y_train: \n',y_train)
print('y_test: \n',y_test)

# Creating function to compute verious losses

