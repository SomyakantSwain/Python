
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))


if x == 0 and y == 0:
    message = "The point is at the origin."
elif x == 0:
    message = "The point lies on the Y-axis."
elif y == 0:
    message = "The point lies on the X-axis."
elif x > 0 and y > 0:
    message = "The point is in Quadrant I."
elif x < 0 and y > 0:
    message = "The point is in Quadrant II."
elif x < 0 and y < 0:
    message = "The point is in Quadrant III."
else:  # x > 0 and y < 0
    message = "The point is in Quadrant IV."

# Print the result
print(message)
