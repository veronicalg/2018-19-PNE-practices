
import termcolor
from Seq import Seq

# Define the Server's port
PORT = 80
SERVER = 'rest.ensembl.org'

conn = http.client.HTTPConnection(SERVER, PORT)


# Retrieving id:
conn.request('GET', "/homology/symbol/human/FRAT1?content-type=application/json")
r1 = conn.getresponse()
print("Response received: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
id = response['data'][0]['id']
print(id)

#Obtaining information about FRAT1
conn.request('GET', "/sequence/id/"+id+"?content-type=application/json")
r1 = conn.getresponse()
print("Response received: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print(response)
cadena =response['seq']
print(cadena)

s1 = Seq(cadena)
print("Lenght: ", s1.len())

print("A: ", s1.count("A"))
print("C: ", s1.count("C"))
print("G: ", s1.count("G"))
print("T: ", s1.count("T"))

#if.....

print("PercG: ", s1.perc("G"))

