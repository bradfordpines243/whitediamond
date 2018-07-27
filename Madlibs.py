def game():
    print("""Welcome to Madlibs,
    a game that allows you to build your own 
    funny jokes using different nouns
    and verbs""")


    noun1 = raw_input("Please provide a noun:")
    friend = raw_input("Please provide the name of a friend:")
    noun2 = raw_input("Please provide a noun:")
    movie_theatre = raw_input("Please provide the name of a movie theatre:")
    movie = raw_input("Please provide the name of your favorite movie:")
    activity = raw_input("Please provide a activity:")
    noun3 = raw_input("Please provide a noun:")

    madlibs = ("""You walk down the %s, contemplating the day ahead of you. 
    First, you have a meeting with %s, where you will discuss %s. Then you 
    will be going to the %s to see %s. After that you will be %s. 
    But as you think about the day ahead of you walk into a %s.""")

    print(madlibs %(noun1,friend,noun2,movie_theatre,movie,activity,noun3))
while True:
    start = raw_input("press x to start, press y to exit")
    if start == "x":
        game()
    if start == "y":
        break