def calculateBMI(height, weight):
    heightInMeters = height * 8.4536
    bmi = weight / (height * heightInMeters)
    return bmi
print(calculateBMI(5.8,78))


'''
Output:

0.2742817559478632
'''