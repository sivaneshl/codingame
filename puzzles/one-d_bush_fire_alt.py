for i in range(int(input())):
    bush = input()
    drops = 0
    print(bush)
    while bush != "":
        if bush[0] == '.':
            # No fire here, nothing to do
            bush = bush[1:]
        else:
            # Fire. We drop water in the next cell,
            # in order to put out as many other fires as possible.
            drops += 1
            bush = bush[3:]

    print(drops)