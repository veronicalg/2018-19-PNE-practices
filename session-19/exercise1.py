# Example of accessing to the ChuckNorris service for getting the number of total jokes about CHUCK NORRIS available,
# number and names of different categories and a random joke.

import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/random"
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
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_raw = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
#print(text_raw)

# -- Generate the object from the json file
json_text = json.loads(text_raw)

# -- Print the random joke:
print("Your random joke is: ", json_text['value']['joke'])



#--Connecting again with a different endpoint in order to obrain the number of jokes:
ENDPOINT = "/jokes/count"

#--Establishing connection with the server
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)

#--Waiting for the response:
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_raw = r1.read().decode("utf-8")
conn.close()

#--We print text received from the server to know the key word of the dictionary:
#print(text_raw)

#--Loading the text into JSON format data
j_number = json.loads(text_raw)

print("The number of total jokes available at the databaase aboyt Chuck Norris is: ", j_number['value'])




#--We set a new endopoint to obtain the number and names of different categories
ENDPOINT = "/categories"

#--Reconect with the remote server
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)

#--Waiting for the response:
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_raw = r1.read().decode("utf-8")
conn.close()

#--We print text received from the server to know the key word of the dictionary:
#print(text_raw)

#--Loading the text into JSON format data
dictionary = json.loads(text_raw)

#--Printing the information that is necessary
print("The number of total categories is: ", len(dictionary['value']))
print("The names of the different categories are: ")
for name_cat in dictionary['value']:
    print(name_cat)




