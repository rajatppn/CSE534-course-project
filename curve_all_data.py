import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

beacons = ["ibeacon", "ibeacon2", "ibeacon3"]
ds = ["25c", "50c", "75c", "1m", "125c", "150c"]
xd = [0.25,0.5,0.75,1,1.25,1.50]

xs = {}
ys = {}

for beacon in beacons:
    i=0
    for d in ds:
        x = xd[i]
        i+=1
        file_name = beacon + "_" + d + ".txt"
        with open(file_name) as fp:
            for line in fp.readlines():
                line = line.strip()
                if(line=="Starting scan"):
                    if(beacon not in xs):
                        xs[beacon] = []
                        ys[beacon] = []
                else:
                    xs[beacon].append(x)
                    ys[beacon].append(int(line))


def f(x, n ,c0):
    return (-10 *n * np.log10(x)) + c0

curves = {}
for beacon in xs:
    curves[beacon] = curve_fit(f ,xs[beacon], ys[beacon], method="dogbox")

i=0
for beacon in curves:
    print(beacon)
    print(curves[beacon])
    print("Error:", np.sqrt(np.diag(curves[beacon][1])))
    plt.figure()
    plt.plot(xs[beacon], ys[beacon], 'ko', label="Original Noised Data")
    plt.plot(xs[beacon], [f(x, *curves[beacon][0]) for x in xs[beacon]], 'r-', label="Fitted Curve")
    plt.legend()
    plt.show()
    i+=1



# Results
# ibeacon
# (array([  1.71175143, -68.08380798]), array([[ 0.00068357, -0.00088277],
#        [-0.00088277,  0.00586835]]))
# Error: [0.02614517 0.07660518]
# ibeacon2
# (array([  1.89106888, -65.03903816]), array([[ 0.0006854 , -0.00089141],
#        [-0.00089141,  0.00587979]]))
# Error: [0.02618022 0.07667977]
# ibeacon3
# (array([  1.62841785, -69.44826202]), array([[ 0.00085305, -0.00108164],
#        [-0.00108164,  0.00723896]]))
# Error: [0.02920708 0.08508207]
