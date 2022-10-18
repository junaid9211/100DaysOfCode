import requests

# this file contains practice code of using pixela api which is used to create GitHub like heatmaps for habit tracking

# 1. creating a user

username = 'ausername123'
token = 'kjldfsakjadfmn5342sgf'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


# 2. creating a graph

graph_endpoint = f'{pixela_endpoint}/{username}/graphs'
graph_id = 'test1'
graph_config = {
    'id': graph_id,
    'name': 'Reading Habit',
    'unit': 'pages',
    'type': 'int',
    'color': 'ajisai'
}
#
headers = {
    'X-USER-token': token
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# 3. create a pixel
post_pixel_endpoint = f'{pixela_endpoint}/{username}/graphs/{graph_id}'

pixel_config = {
    'date': '20221010',
    'quantity': '4',

}

response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# 4. update a pixel
date_to_update = '20221010'
put_pixel_endpoint = f'{pixela_endpoint}/{username}/graphs/{graph_id}/{date_to_update}'
put_pixel_config = {
    'quantity': '100'
}

response = requests.put(url=put_pixel_endpoint, json=put_pixel_config, headers=headers)
print(response.json())