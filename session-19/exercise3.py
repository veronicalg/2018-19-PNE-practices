# Getting information stored in github depending on the user name.

import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = input("Please, enter the github user you want to retrieve information: ")
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
#print(text_json)

# -- Generate the object from the json file
user = json.loads(text_json)

# -- Get the NAME
name = user['name']
print("Name: {}".format(name))




# -- Retrieving the list with the names of all the repos the user has
# -- New connection
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + GITHUB_ID + "/repos", None, headers)
r1 = conn.getresponse()
print()
print("Response received: ", end='')
print(r1.status, r1.reason)
text_json = r1.read().decode("utf-8")
conn.close()
#print(text_json)
list = json.loads(text_json)

#--Create a list with all the repo names
repos_list = []

#-- We retrieve just the repo name from every element of the list that the server has sent to our client.
# and we save it in repos_list.
for i in list:
    repo_name = i['name']
    repos_list.append(repo_name)

print("The list with the names of all repos that the user has is: ",repos_list)




#--Retrieving the total number of commits to the 2018-19 repo
#--New connection
ENDPOINT = "/repos/"+GITHUB_ID+"/2018-19-PNE-practices/commits"
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)
r1 = conn.getresponse()
print()
print("Response received: ", end='')
print(r1.status, r1.reason)
text_json = r1.read().decode("utf-8")
conn.close()
#print(text_json)
com_list = json.loads(text_json)
#print(com_list)
print("Total commits: ", len(com_list))