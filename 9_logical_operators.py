has_license = True
has_car = False
age = 22

# Can legally drive
can_drive = age > 18 and has_license
print(can_drive) # True

# Can get a ride
has_friend_with_car = True
can_get_ride = has_car or has_friend_with_car
print(can_get_ride) # True

# Student discount eligibility
is_student = not(age >= 26)
print(is_student) # True
