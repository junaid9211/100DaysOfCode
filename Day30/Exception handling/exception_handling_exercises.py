# Exercise 1 IndexError
fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    try:
        pie = fruits[index] + ' pie'
    except IndexError:
        pie = 'fruit pie'

    return pie

print(make_pie(5))

# Exercise 2 KeyError
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        pass

print(f'Total likes: {total_likes}')
