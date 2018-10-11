def main():
    draw7()
    starsAndStripes()

def draw7():
    for i in range(0, 7):
        string = ""
        for i in range(0, 7):
            string += "*"
        print (string)

def starsAndStripes():
    for i in range(0, 3):
        starString = ""
        dashString = ""
        for i in range (0, 7):
            starString += "*"
            dashString += "-"
        print(starString)
        print(dashString)


main()
