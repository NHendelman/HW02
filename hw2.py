import json
import matplotlib.pyplot as plt
import os
import matplotlib.pyplot as plt
import numpy as np

with open ("/Users/noahendelman/Documents/GitHub/nhendelman/HW/Obama2012.json" , encoding= 'ascii') as f1:
    data_1 = json.loads(f1.read())
with open ("/Users/noahendelman/Documents/GitHub/nhendelman/HW/Obama2013.json" , encoding= "ascii" ) as f2:
    data_2 = json.loads(f2.read())

#January 2012 numbers
Obama_number = 0
for tweet in data_1:
    if 'obama' in tweet['text'].lower():
        Obama_number += 1
print (Obama_number)

michelle_number = 0
for tweet in data_1:
    if 'michelle' in tweet['text'].lower():
        michelle_number += 1
print (michelle_number)

economy_number = 0
for tweet in data_1:
    if 'economy' in tweet['text'].lower():
        economy_number += 1
print (economy_number)

state_number = 0
for tweet in data_1:
    if 'state' in tweet['text'].lower():
        state_number += 1
print (state_number)

the_number = 0
for tweet in data_1:
    if 'the' in tweet['text'].lower():
        the_number += 1
print (the_number)

usa_number = 0
for tweet in data_1:
    if 'usa' in tweet['text'].lower():
        usa_number += 1
print (usa_number)


counts_2012 = {
    'Obama': Obama_number,
    'Michelle': michelle_number,
    'Economy': economy_number,
    'State': state_number,
    'The': the_number,
    'USA': usa_number,
}
print('counts =', counts_2012)

xs = sorted(counts_2012.keys())
ys = [ counts_2012[key] for key in xs ]

print('xs=',xs)
print('ys=',ys)

fig, ax = plt.subplots()
ax.bar(xs, ys)
ax.set_xlabel('Specific Word')
ax.set_ylabel('Usage')
ax.set_title('Word Usage in Obama Tweets of Jan 2012')
plt.show()

#2013------------------------------


Obama_number2 = 0
for tweet in data_2:
    if 'obama' in tweet['text'].lower():
        Obama_number2 += 1
print (Obama_number2)

michelle_number2 = 0
for tweet in data_2:
    if 'michelle' in tweet['text'].lower():
        michelle_number2 += 1
print (michelle_number2)

economy_number2 = 0
for tweet in data_2:
    if 'economy' in tweet['text'].lower():
        economy_number2 += 1
print (economy_number2)

state_number2 = 0
for tweet in data_2:
    if 'state' in tweet['text'].lower():
        state_number2 += 1
print (state_number2)

the_number2 = 0
for tweet in data_2:
    if 'the' in tweet['text'].lower():
        the_number2 += 1
print (the_number2)

usa_number2 = 0
for tweet in data_2:
    if 'usa' in tweet['text'].lower():
        usa_number2 += 1
print (usa_number2)


counts_2013 = {
    'Obama': Obama_number2,
    'Michelle': michelle_number2,
    'Economy': economy_number2,
    'State': state_number2,
    'The': the_number2,
    'USA': usa_number2,
}
print('counts =', counts_2013)

xs2 = sorted(counts_2013.keys())
ys2 = [ counts_2013[key] for key in xs ]

print('ys=',ys)
print('ys2=',ys2)



labels = ['Obama', 'Michelle', 'Economy', 'State', 'The', 'USA']

x = np.arange(len(counts_2012)) 
x2 = np.arange(len(counts_2013)) # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, ys, width, label='Jan2012')
rects2 = ax.bar(x + width/2, ys2, width, label='Jan2013')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Uses')
ax.set_title('Obama Tweet Word Usage')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
