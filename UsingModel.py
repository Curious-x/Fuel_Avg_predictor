import pandas as pd
from sklearn import linear_model
import pickle


model = pickle.load(file=open('mymodel.pkl','rb'))

VehiclefuelAvg = 30 # Km/liter
passangers = 2

traffic_rating = 2
# 0:No 1:little 2:Normal 3:Busy 4:Very Busy 5:Trafic Jam

Signals_per_Km = 0.01
road_rating = 3
# 1:small roads 2:main roads 3:Main highway 4:Highway 5:MotorWay

predicted_fuel_avg_trip=model.predict([[VehiclefuelAvg,passangers,traffic_rating,Signals_per_Km,road_rating]])[0]
print(round(predicted_fuel_avg_trip,2))