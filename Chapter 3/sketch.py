import os


os.chdir("C:\\Users\\akifk\\Desktop\\HeadFirstPython\\Chapter 3\data")


try:
    #if os.path.exists('sketch.txt'):
        data = open("sketch.txt")



        for each_line in data:
            if not each_line.find(":") == -1:
                try:
                        (role, line_spoken) = each_line.split(":", 1)
                        print(role, end='')
                        print(' said:', end='')
                        print(line_spoken, end='')
                except ValueError:
                    pass
    #else:
    #    print("The data file is missing!! nooooooooo")
except IOError:
     print("The data file is missing!! nooooooooo")
