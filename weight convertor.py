weight =  float(input("enter the weight:"))
unit = input("enter the weight unit (kg or lbs):")

if unit == "kg":
    convert_weight = weight *2.205
elif unit == "lbs":
    convert_weight = weight / 2.205

print("the converted weight is :", convert_weight)
