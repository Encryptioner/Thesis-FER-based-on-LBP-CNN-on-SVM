
# modifying_fer2013_emotion_label.py


import numpy as np
import csv


r = csv.reader(open('dataset/fer2013.csv'))  # Here your csv file
lines = list(r)

# print(lines.__len__())

num_of_instances = lines.__len__()
# num_of_instances = 10
print("number of instances: ", num_of_instances)

for i in range(1, num_of_instances):
    try:
        # emotion, img, usage = lines[i].split(",")

        print('start', lines[i][0])

        if lines[i][0] == '0':
            lines[i][0] = '8'

        if lines[i][0] == '1':
            lines[i][0] = '9'

        if lines[i][0] == '2':
            lines[i][0] = '10'

        if lines[i][0] == '3':
            lines[i][0] = '11'

        if lines[i][0] == '4':
            lines[i][0] = '12'

        if lines[i][0] == '5':
            lines[i][0] = '13'

        if lines[i][0] == '6':
            lines[i][0] = '7'




        if lines[i][0] == '7':
            lines[i][0] = '0'

        if lines[i][0] == '8':
            lines[i][0] = '1'

        if lines[i][0] == '9':
            lines[i][0] = '2'

        if lines[i][0] == '10':
            lines[i][0] = '3'

        if lines[i][0] == '11':
            lines[i][0] = '4'

        if lines[i][0] == '12':
            lines[i][0] = '5'

        if lines[i][0] == '13':
            lines[i][0] = '6'


        print('f ', lines[i][0])

    except:

        print(" error occured\n", end="")

writer = csv.writer(open('dataset/changed_fer2013.csv', 'w'))
writer.writerows(lines)

print('image dataset label changed in a new file')
