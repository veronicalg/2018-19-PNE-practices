# Example of getting information about the weather of any location (city)


import http.client
import json

# -- API information
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/search/?query="

# -- For the location we have to use the
# -- Were on earth identifier
# -- London woeid = 44418
# -- Madrid woeid = 766273
# -- We wil get the identifier first
LOCATION = input("Please enter a city: ")
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
conn.request(METHOD, ENDPOINT + LOCATION.lower(), None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
raw_info = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
#print(raw_info)


# -- Generate the object from the json file in a list
city_info_list = json.loads(raw_info)
#print(city_info_list)


# -- Fixing errors in case the city is not in the database
if len(city_info_list)==0:
    print("Sorry, this city is not in our database.")
else:
# -- Getting WOEID identifier number
    WOEID = city_info_list[0]['woeid']


    #--Establishing a new connection in order to retrieve the data

    ENDPOINT= "/api/location/"
    conn = http.client.HTTPSConnection(HOSTNAME)

    # -- Send the request with the WOEID now.
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT + str(WOEID) + '/', None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    text_raw = r1.read().decode("utf-8")
    conn.close()

    # -- Optionally you can print the
    # -- received json file for testing
    #print(text_raw)

    # -- Generate the object from the json file
    weather = json.loads(text_raw)


    # -- Get the data
    place = weather['title']
    time = weather['time']
    description= weather['consolidated_weather'][0]['weather_state_name']
    temp = weather['consolidated_weather'][0]['the_temp']

    print()
    print("Place: {}".format(place))
    print("Time: {}".format(time))
    print("Weather description: {}".format(description))
    print("Current temperature: {} degrees".format(temp))

