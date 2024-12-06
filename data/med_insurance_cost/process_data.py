


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

def main():
    # Load the dataset
    data = pd.read_csv("data/med_insurance_cost/medical_insurance.csv", header=0, delimiter=",")
    
    # Encode categorical variables
    label_encoders = {}
    for col in ['sex', 'smoker', 'region']:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le
    
    # Separate features and target
    target_col = 'charges'
    features = data.drop(columns=[target_col])
    target = data[target_col]
    
    # Scale numerical features
    numerical_cols = ['age', 'bmi', 'children']
    scaler = StandardScaler()
    features[numerical_cols] = scaler.fit_transform(features[numerical_cols])
    
    # Scale the target using MinMaxScaler (instead of StandardScaler)
    target_scaler = MinMaxScaler()
    target = target_scaler.fit_transform(target.values.reshape(-1, 1)).squeeze()  # Reshaping for scaler
    
    # Combine scaled features and target back
    data = pd.concat([features, pd.Series(target, name=target_col)], axis=1)
    
    # Split into train and test sets
    raw_train, raw_test = train_test_split(data, test_size=0.3, shuffle=True, random_state=2023)
    
    # Save train and test sets to files
    raw_train.to_csv("data/med_insurance_cost/train.txt", index=False, header=False, sep=' ')
    raw_test.to_csv("data/med_insurance_cost/test.txt", index=False, header=False, sep=' ')

main()
