import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split




dataFrame=pd.read_csv("Data.csv")

X=dataFrame[['V_fuelAvg','Passangers','Traffic_rating','Signals_km','Road_rating']]
y=dataFrame['FuelAvg']

X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=0.5)

lm = linear_model.LinearRegression()
lm.fit(X_train, y_train.values)


y_pred=lm.predict(X_test)

y_test=y_test.values

# Calculating accuracy
acceptableDiff=3
Acceptable=0



for index,value in enumerate(y_pred):
    if abs(value-y_test[index])<=acceptableDiff:
        Acceptable+=1
        
percent=100*(Acceptable/len(y_pred))

print("Trained model Accuracy: ",round(percent))
