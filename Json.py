import json

mydata = [
          {
          "Name": "Joy",
          "School":"Kabare",
          "Hobbies":["Playing Chess", "Cooking", "Shopping"]
          },
          {
          "Name": "Maina",
          "School":"Kabarack",
          "Hobbies":["Watching movies", "Rugby", "Shopping"]
          }
         ]
# The Json Object/Dictionary
print mydata

# Keys in the json Object/Dictionary
print "************"
mydata[0].keys()
print "************"
'''Joy_school = mydata["School"]
print Joy_school
Joy_hobbies = mydata["Hobbies"]
print Joy_hobbies

swimming = Joy_hobbies[0]
print swimming

chess = Joy_hobbies[2]
print chess'''



persons_name = mydata[0]["Name"]
print persons_name

#For Loop
