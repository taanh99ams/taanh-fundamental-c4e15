def is_inside(coord_point, coord_rec):
    x_point = coord_point[0]
    y_point = coord_point[1]
    x_rec = coord_rec[0]
    y_rec = coord_rec[1]
    width = coord_rec[2]
    height = coord_rec[3]
    result = 0
    if x_rec <= x_point <= x_rec + width and y_rec <= y_point <= y_rec + height:
        result = "True"
    else:
        result = "False"
    return result

in_or_out = is_inside([100, 120], [140, 60, 100, 200])
if in_or_out == "False":
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
