import csv
from random import randint,uniform

def getRandomDetails():
    # Random Details
    V_fuelAvg = uniform(4, 60)
    passangers = randint(1,30)
    distance = uniform(4,1400)
    traffic_rating = randint(0,5)
    trafficSignals = randint(0, distance//3)
    road_rating = randint(1,5)

    # Calculated data 55.01,8,133.49,3,42,5,32.49,4.11,2.43
    idealFuelConsump = distance/V_fuelAvg
    Signals_km = trafficSignals/distance

    # Adding a bit random effect of factors

    fuelAvg= V_fuelAvg
    fuelAvg *= (100-(passangers*uniform(0.1,0.2)))/100
    fuelAvg *= (100-((traffic_rating-2)*uniform(1,5)))/100
    fuelAvg *= (100-((3-road_rating)*uniform(1,10)))/100

    fuelConsump = distance/fuelAvg
    fuelConsump += trafficSignals*uniform(0.01, 0.1)
    fuelAvg = distance / fuelConsump

    record = [V_fuelAvg,passangers,distance,traffic_rating,Signals_km,road_rating,fuelAvg,fuelConsump,idealFuelConsump]
    for index in range(len(record)):
        record[index]=round(record[index],2)
    return record

print("Ready!")
detail=[]

for counter in range(1000):
    detail.append(getRandomDetails())


with open("Data.csv","a",newline='') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',',dialect='excel')
    csvWriter.writerows(detail)

print("Done")