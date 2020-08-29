basecost = 2.40
roundtrip = basecost*2

"""multiplied by week, month, semester cost"""
roundtriphalf = 6*3*3*(basecost*1.5)
roundtripqhalf = 6*3*3*(basecost*1.75)


weekcost = 6*roundtrip
monthcost =weekcost*3
semestercost =monthcost*3


print ("The estimated roundtrip half cost is: " + str(roundtriphalf))
print ("The estimated roundtrip quarter and a half cost is: " + str(roundtripqhalf))
print("The estimated semester cost is: " + str(semestercost))
print()
print()
print()

print("The estimated month cost is: " + str(monthcost))

print()
print("MBTA card deal is: $240 for the semester")

print(":^)")