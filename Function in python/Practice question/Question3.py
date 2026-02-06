# Write a python function which converts inches to cms.
distance = float(input("Enter distance in inches: "))

def convertIntoCM(d):
    return d*2.54

print(f"{distance} inches = {convertIntoCM(distance)} cms")