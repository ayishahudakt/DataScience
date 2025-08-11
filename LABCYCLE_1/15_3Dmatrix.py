import math

# Translation Matrix (3D)
def translation_matrix(tx, ty, tz):
    return [[1, 0, 0, tx],
            [0, 1, 0, ty],
            [0, 0, 1, tz],
            [0, 0, 0, 1]]

# Rotation Matrices (3D)
def rotation_matrix_x(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    cos_a = math.cos(angle_radians)
    sin_a = math.sin(angle_radians)
    return [[1, 0, 0, 0],
            [0, cos_a, -sin_a, 0],
            [0, sin_a,  cos_a, 0],
            [0, 0, 0, 1]]

def rotation_matrix_y(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    cos_a = math.cos(angle_radians)
    sin_a = math.sin(angle_radians)
    return [[cos_a, 0, sin_a, 0],
            [0, 1, 0, 0],
            [-sin_a, 0, cos_a, 0],
            [0, 0, 0, 1]]

def rotation_matrix_z(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    cos_a = math.cos(angle_radians)
    sin_a = math.sin(angle_radians)
    return [[cos_a, -sin_a, 0, 0],
            [sin_a,  cos_a, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]

# Scaling Matrix (3D)
def scaling_matrix(sx, sy, sz):
    return [[sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]]

# User Input
tx = float(input("Enter translation in x: "))
ty = float(input("Enter translation in y: "))
tz = float(input("Enter translation in z: "))

angle_x = float(input("Enter rotation about X axis (degrees): "))
angle_y = float(input("Enter rotation about Y axis (degrees): "))
angle_z = float(input("Enter rotation about Z axis (degrees): "))

sx = float(input("Enter scaling in x: "))
sy = float(input("Enter scaling in y: "))
sz = float(input("Enter scaling in z: "))

# Output Matrices
print("\nTranslation Matrix:")
for row in translation_matrix(tx, ty, tz):
    print(row)

print("\nRotation Matrix about X-axis:")
for row in rotation_matrix_x(angle_x):
    print(row)

print("\nRotation Matrix about Y-axis:")
for row in rotation_matrix_y(angle_y):
    print(row)

print("\nRotation Matrix about Z-axis:")
for row in rotation_matrix_z(angle_z):
    print(row)

print("\nScaling Matrix:")
for row in scaling_matrix(sx, sy, sz):
    print(row)

