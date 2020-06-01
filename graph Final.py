import matplotlib.pyplot as plt

plt.figure(1)
pos = [1, 2, 3, 4, 5]
sales = [203, 136, 113, 83, 68]
topgames = ['Minecraft', 'Grand Theft Auto V', 'Tetris (EA)', 'Wii Sports', 'PlayerUnknown\'s BattleGrounds']

plt.bar(pos, sales, color='limegreen')
plt.xticks(pos[0:], topgames, fontsize='6')
plt.title("Top 5 Video Game Sales")
plt.xlabel('Games')
plt.ylabel('Sales(Mil)')
plt.show()


# Im unsure why this works and not the one in final 2