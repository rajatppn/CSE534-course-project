import numpy as np
import math

def is_ibeacon(uuid):
    return uuid == "526c7565-4368-6172-6d42-6561636f6e73"

def is_ibeacon2(uuid):
    return uuid == "426c7565-4368-6172-6d42-6561636f6e73"

def is_ibeacon3(uuid):
    return (uuid == "d546df97-4757-47ef-be09-3e2dcbdd0c77" or uuid == "fda50693-a4e2-4fb1-afcf-c6eb07647825")

IBEACON_PARAMS = (1.71175143, -68.08380798)

IBEACON2_PARAMS = (1.88119329, -65.04953258)

IBEACON3_PARAMS = (1.62940665, -69.45342562)

ibeacon_sum = 0
ibeacon_count = 0
ibeacon2_sum = 0
ibeacon2_count = 0
ibeacon3_sum = 0
ibeacon3_count = 0

setups = ["1.txt", "2.txt", "3.txt", "4.txt"]

results = {
    "1": None,
    "2": None,
    "3": None,
    "4": None
}
def f(x, n ,c0):
    return math.pow(10, (c0 -x)/(10*n))

for setup in setups:
    print(setup)
    with open(setup) as fp:
        for line in fp.readlines():
            line = line.strip()
            if(line=="Starting scan"):
                ibeacon_sum = 0
                ibeacon_count = 0
                ibeacon2_sum = 0
                ibeacon2_count = 0
                ibeacon3_sum = 0
                ibeacon3_count = 0
            else:
                uuid, rssi = line.split(',')
                uuid = uuid.strip()
                rssi = int(rssi.strip())
                print(uuid,rssi)
                if(is_ibeacon(uuid)):
                    ibeacon_sum += rssi
                    ibeacon_count += 1
                elif(is_ibeacon2(uuid)):
                    ibeacon2_sum += rssi
                    ibeacon2_count += 1
                if(is_ibeacon3(uuid)):
                    ibeacon3_sum += rssi
                    ibeacon3_count += 1
        ibeacon_avg_rssi = ibeacon_sum/ibeacon_count
        ibeacon2_avg_rssi = ibeacon2_sum/ibeacon2_count
        ibeacon3_avg_rssi = ibeacon3_sum/ibeacon3_count
        results[setup.split(".")[0]] = {
            "ibeacon_avg_rssi": ibeacon_avg_rssi,
            "ibeacon_distance_estimate": f(ibeacon_avg_rssi, *IBEACON_PARAMS),
            "ibeacon2_avg_rssi": ibeacon2_avg_rssi,
            "ibeacon2_distance_estimate": f(ibeacon2_avg_rssi, *IBEACON2_PARAMS),
            "ibeacon3_avg_rssi": ibeacon3_avg_rssi,
            "ibeacon3_distance_estimate": f(ibeacon3_avg_rssi, *IBEACON3_PARAMS),
        }

print(results)


#results
# {'1': {'ibeacon_avg_rssi': -53.84658454647256, 'ibeacon_distance_estimate': 0.14732136016754635, 'ibeacon2_avg_rssi': -67.90315315315316, 'ibeacon2_distance_estimate': 1.4180516353873736, 'ibeacon3_avg_rssi': -69.55531453362256, 'ibeacon3_distance_estimate': 1.0145025193062556}, '2': {'ibeacon_avg_rssi': -64.61920903954802, 'ibeacon_distance_estimate': 0.6274789764165978, 'ibeacon2_avg_rssi': -62.974387527839646, 'ibeacon2_distance_estimate': 0.7756931583872707, 'ibeacon3_avg_rssi': -65.79828326180258, 'ibeacon3_distance_estimate': 0.5965907008214058}, '3': {'ibeacon_avg_rssi': -64.00114942528735, 'ibeacon_distance_estimate': 0.5774206669100002, 'ibeacon2_avg_rssi': -54.08620689655172, 'ibeacon2_distance_estimate': 0.26134505638070393, 'ibeacon3_avg_rssi': -64.93347639484979, 'ibeacon3_distance_estimate': 0.5279606117064477}, '4': {'ibeacon_avg_rssi': -70.87244283995186, 'ibeacon_distance_estimate': 1.4551615265228253, 'ibeacon2_avg_rssi': -70.05939393939394, 'ibeacon2_distance_estimate': 1.8463454084337774, 'ibeacon3_avg_rssi': -72.9599109131403, 'ibeacon3_distance_estimate': 1.6413459728865263}}
