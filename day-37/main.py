import datetime, json, requests

with open("user_params.json","r") as f:
    login_info = json.load(f)

USERNAME = login_info["username"]
TOKEN = login_info["token"]

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/"
GRAPH_ID = "writing"
pixel_endpoint = f"{graph_endpoint}{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}

# ## THIS CODE CREATES A GRAPH
# graph_parameters = {
#     'id': 'writing',
#     'name': 'writing_graph',
#     'unit': 'words',
#     'color': 'momiji',
#     'type': 'int'
# }
#
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

## THIS CODE ADDS DATA FOR TODAY
# today = datetime.datetime.now().strftime("%Y%m%d")
# pixel_parameters = {
#     "date": today,
#     "quantity": "100"
# }
# response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
# print(response.text)

## THIS CODE UPDATES EXISTING DATA
# today = datetime.datetime.now().strftime("%Y%m%d")
# pixel_update_endpoint = f"{pixel_endpoint}/{today}"
# pixel_update_parameters = {
#     "quantity": "1000"
# }
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_parameters, headers=headers)
# print(response.text)

## THIS CODE DELETES DATA
today = datetime.datetime.now().strftime("%Y%m%d")
pixel_update_endpoint = f"{pixel_endpoint}/{today}"
response = requests.delete(url=pixel_update_endpoint, headers=headers)
print(response.text)