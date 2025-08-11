import math

def translation_matrix(tx, ty):
    return [[1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]]

def rotation_matrix(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    cos_a = math.cos(angle_radians)
    sin_a = math.sin(angle_radians)
    return [[cos_a, -sin_a, 0],
            [sin_a,  cos_a, 0],
            [0,      0,     1]]

def scaling_matrix(sx, sy):
    return [[sx, 0,  0],
            [0,  sy, 0],
            [0,  0,  1]]

tx = float(input("Enter translation in x: "))
ty = float(input("Enter translation in y: "))
angle = float(input("Enter rotation angle in degrees: "))
sx = float(input("Enter scaling in x: "))
sy = float(input("Enter scaling in y: "))

print("\nTranslation Matrix:")
for row in translation_matrix(tx, ty):
    print(row)

print("\nRotation Matrix:")
for row in rotation_matrix(angle):
    print(row)

print("\nScaling Matrix:")
for row in scaling_matrix(sx, sy):
    print(row)

