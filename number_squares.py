
# This is a non-efficient way of doing this. Although this works,
# there's a better way to do this.

# def fetch_squares(max_root):
#     squares = []
#     for n in range(max_root):
#         squares.append(n**2)
#     return squares


# MAX = 5
# for square in fetch_squares(MAX):
#     print(square)

# Here we are using the "yield" keyword. The yield statement simultaneously
# defines an exit point and the loop will continue with its next iteration.
def gen_squares(max_num):
    for num in range(max_num):
        yield num**2


MAX = 5
for square in gen_squares(MAX):
    print(square)


