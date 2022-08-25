import os

path = 'E:\games'

files = os.listdir(path)

for index, file in enumerate(files):
    
    # Change Dir for each game
    os.chdir('E:\games' + '\\' + file)

    # Print current dir
    cwd = os.getcwd()
    print("Current working directory is:", cwd)

    # Pring game in file
    games = os.listdir(cwd)
    print(games[0])

    # Rename game
    os.rename(games[0], 'game.iso')
    games = os.listdir(cwd)
    print(games[0])

    # Go back to main dir 
    os.chdir(path)

    print('\n')