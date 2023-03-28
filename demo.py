def rotate_image_90_cw(image):
    # transpose the matrix
    transposed_image = list(zip(*image))

    # reverse each row
    rotated_image = [list(reversed(row)) for row in transposed_image]

    return rotated_image
import math

def rotate_image(image, angle):
    # convert the angle to radians
    angle = math.radians(angle)

    # calculate the rotation matrix
    rotation_matrix = [
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle), math.cos(angle)]
    ]

    # apply matrix multiplication to the image and rotation matrix
    rotated_image = []
    for row in image:
        new_row = []
        for i in range(len(rotation_matrix[0])):
            new_pixel = 0
            for j in range(len(row)):
                new_pixel += row[j] * rotation_matrix[j][i]
            new_row.append(new_pixel)
        rotated_image.append(new_row)

    # round the values to the nearest integer and convert to PBM format
    rotated_image = [[str(round(pixel)) for pixel in row] for row in rotated_image]

    return rotated_image
def read_pbm_file(filename):
    with open(filename, 'r') as file:
        # skip the magic number
        file.readline()

        # read the dimensions
        dimensions = [int(dimension) for dimension in file.readline().split()]

        # read the image data
        image_data = [[int(pixel) for pixel in line.split()] for line in file]

        return dimensions, image_data

def write_pbm_file(filename, dimensions, image_data):
    with open(filename, 'w') as file:
        # write the magic number and dimensions
        file.write('P1\n')
        file.write('{} {}\n'.format(dimensions[0], dimensions[1]))

        # write the image data
        for row in image_data:
            file.write(' '.join(str(pixel) for pixel in row))
            file.write('\n')

filename = input("enter file name:")
dimensions, image_data = read_pbm_file(filename)

# rotate the image by 45 degrees
rotated_image_data = rotate_image(image_data, 45)

# write the rotated image to disk
write_pbm_file('rotated_image.pbm', dimensions, rotated_image_data)
