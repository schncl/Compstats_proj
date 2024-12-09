import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def main():
    # Load the dataset
    data = pd.read_csv(r"C:\Users\Pınar\Desktop\CS_project_test\data\Breast_cancer_data\Breast_cancer_data.csv", header=0, delimiter=",")
    
    # Separate features and target
    target_col = 'diagnosis'
    features = data.drop(columns=[target_col])
    target = data[target_col]
    
    # Scale numerical features
    scaler = StandardScaler()
    features = scaler.fit_transform(features)
    
    # Scale the target using MinMaxScaler (instead of StandardScaler)
    target_scaler = MinMaxScaler()
    target = target_scaler.fit_transform(target.values.reshape(-1, 1)).squeeze()  # Reshaping for scaler
    
    # Combine scaled features and target back
    data = pd.DataFrame(features, columns=data.columns[:-1])
    data[target_col] = target
    
    # Split into train and test sets
    raw_train, raw_test = train_test_split(data, test_size=0.3, shuffle=True, random_state=2023)
    raw_train.to_csv(r"C:\Users\Pınar\Desktop\CS_project_test\data\Breast_cancer_data\train.txt", index=False, header=False, sep=' ')
    raw_test.to_csv(r"C:\Users\Pınar\Desktop\CS_project_test\data\Breast_cancer_data\test.txt", index=False, header=False, sep=' ')
  

  


main()
