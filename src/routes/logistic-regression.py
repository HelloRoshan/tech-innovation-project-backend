import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import os

#read the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
node_data = pd.read_csv(os.path.join(script_dir, "nodes.csv"))
edge_data = pd.read_csv(os.path.join(script_dir, "edges.csv"))


# Merge based on source and target columns
merged_data = edge_data.merge(node_data, left_on='source', right_on='ID', how='inner')
merged_data = merged_data.merge(node_data, left_on='target', right_on='ID', suffixes=('_source', '_target'), how='inner')

# Create a 'Tie Strength' column to quantify the strength or frequency of ties
tie_strength = merged_data.groupby(['sender', 'receiver']).size().reset_index(name='Tie_Strength')
merged_data = merged_data.merge(tie_strength, on=['sender', 'receiver'], how='inner')

# Create a 'Tie' column with 1 indicating a tie (connection)
merged_data['Tie'] = 1

# print(merged_data)

# Drop unnecessary columns, keeping the relevant attributes
merged_data = merged_data[['Gender_source', 'Agree_source', 'Performance_source', 'Age_source',
                           'Gender_target', 'Agree_target', 'Performance_target', 'Age_target',
                           'Tie']]

X = merged_data.drop('Tie', axis=1)
y = merged_data['Tie']

# Split the data into training and testing sets:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make prediction
y_pred = model.predict(X_test)


# Evaluate the model's performance:
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Confusion Matrix:\n", confusion)
print("Classification Report:\n", classification_rep)
