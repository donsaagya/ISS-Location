import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"

# we use the "urllib" library for getting a response from the server and store it in "response" variable
# in this case, the response variable stores the response we got from the server.
response = urllib.request.urlopen(url)

# response.read() gives us the raw data of the response as raw bytes
# json.loads() transforms this data into a dictionary for use to work with
result = json.loads(response.read())


file = open("iss.txt", "w")
file.writelines(f"There are currently {result['number']} astronauts on the ISS: \n")
astronauts_on_iss = result["people"]

for astronaut in astronauts_on_iss:
    file.writelines(f"{astronaut['name']}\n")

developer_location = geocoder.ip("me")
file.writelines(f"Your current lat / long is: {developer_location.latlng}")

file.close()

webbrowser.open("iss.txt")


#
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)


# load the world map image
screen.bgpic("world_map.gif")
screen.register_shape("iss_icon.gif")

iss = turtle.Turtle()
iss.shape("iss_icon.gif")
iss.setheading(45)
iss.penup()

while True:

    try:
        url = "http://api.open-noify.org/iss-now.json"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())

        location = result["iss_position"]
        latitude = float(location['latitude'])
        longitude = float(location['longitude'])

        iss.goto(longitude, latitude)

        time.sleep(5)
    except:
        print("an error occured in this cycle!")
