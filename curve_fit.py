import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

values = [
{
    "x":[0.25,0.5,0.75,1,1.25,1.50],
    "y":[-58.249445676274945, -60.28265765765766, -68.46178343949045, -65.78125, -76.175, -66.79710144927536]
},
{
    "x":[0.25,0.5,0.75,1,1.25,1.50],
    "y":[-55.11542730299667, -54.469255663430424, -64.77790055248619, -68.78538812785388, -66.61391694725027, -66.33178114086147]
},
{
    "x":[0.25,0.5,0.75,1,1.25,1.50],
    "y":[-59.4122621564482, -64.08768267223383, -67.74273858921161,-70.51059322033899, -72.49356223175965, -70.17124735729386]
}
]

def f(x, n ,c0):
    return (-10 *n * np.log10(x)) + c0

curves = []
for value in values:
    curves.append(curve_fit(f ,value["x"], value["y"], p0=[1,-75]))

i=0
for curve in curves:
    print(curve)
    print("Error:", np.sqrt(np.diag(curve[1])))
    plt.figure()
    plt.plot(values[i]["x"], values[i]["y"], 'ko', label="Original Noised Data")
    plt.plot(values[i]["x"], f(values[i]["x"], *curve[0]), 'r-', label="Fitted Curve")
    plt.legend()
    plt.show()
    i+=1


# Results of the curves
# (array([  1.73256315, -68.1380942 ]), array([[ 0.47526146, -0.59805906],
#        [-0.59805906,  4.03263027]]))
# Error: [0.6893921 2.008141 ]
# (array([  1.88119329, -65.04953258]), array([[ 0.29331606, -0.36910278],
#        [-0.36910278,  2.48880958]]))
# Error: [0.54158662 1.57759614]
# (array([  1.62940665, -69.45342562]), array([[ 0.04982179, -0.0626947 ],
#        [-0.0626947 ,  0.42274177]]))
# Error: [0.22320795 0.65018595]
