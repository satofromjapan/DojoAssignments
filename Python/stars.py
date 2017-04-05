# def draw_stars(list):
#     for i in list:
#         print i * "*"
#
#
#
# x = [4,6,1,3,5,7,25]
# draw_stars(x)

def draw_stars_b(list):
    for i in list:
        if type(i) is str:
            print i.lower()[0]*len(i)
        elif type(i) is int:
            print i * "*"


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars_b(x)
