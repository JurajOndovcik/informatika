import random
import matplotlib.pyplot as plt

dva = 0
tri = 0
styri = 0
pat = 0
sest = 0
sedem = 0
osem = 0
devat = 0
desat = 0
jedenast = 0
dvanast = 0

for i in range(1000):
    kocka1 = random.randint(1, 6)
    kocka2 = random.randint(1, 6)
    body = kocka1 + kocka2

    if body == 2:
        dva += 1
    elif body == 3:
        tri += 1
    elif body == 4:
        styri += 1
    elif body == 5:
        pat += 1
    elif body == 6:
        sest += 1
    elif body == 7:
        sedem += 1
    elif body == 8:
        osem += 1
    elif body == 9:
        devat += 1
    elif body == 10:
        desat += 1
    elif body == 11:
        jedenast += 1
    elif body == 12:
        dvanast += 1


# x-coordinates of left sides of bars 
left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# heights of bars
height = [dva, tri, styri, pat, sest, sedem, osem, devat, desat, jedenast, dvanast]

# labels for bars
tick_label = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('SIMULACIA KOCIEK')
print("2:   ", dva)
print("3:   ", tri)
print("4:   ", styri)
print("5:   ", pat)
print("6:   ", sest)
print("7:   ", sedem)
print("8:   ", osem)
print("9:   ", devat)
print("10:  ", desat)
print("11:  ", jedenast)
print("12:  ", dvanast)
# function to show the plot
plt.show()