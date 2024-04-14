h = int(input("Nhap do cao h: "))
triangle_out = h - 1  # Initial number of spaces
triangle_in = 1       # Initial number of spaces inside the triangle

for i in range(h):
    if i == 0:
        print(" " * triangle_out + "*")
    elif i < h - 1:
        print(" " * triangle_out + "*" + " " * triangle_in + "*")
        triangle_in += 2  # Increase the number of inside spaces by 2
    else:
        print("*" * (h * 2 - 1))  # Print the bottom line
    triangle_out -= 1  # Decrease the number of outside spaces
