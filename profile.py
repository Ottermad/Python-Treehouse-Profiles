# Import statements
import requests # Library to parse JSON and get data 

# Function to output message
def print_message(username, badge_count, subject, points):
	print "{} has {} badges and {} points in {}".format(username, badge_count, points, subject)

# Function to get profile data
def get(username, subject):
	try:
		request = requests.get("http://teamtreehouse.com/{}.json".format(username))

		try:
			if request.status_code == 200:
				json = request.json() # Get JSON
				badge_count = len(json["badges"]) # Get total number of badges by getting length of badges array
				subject_points =  json["points"][subject] # Get points
				name = json["name"] # Get name
				print_message(name, badge_count, subject, subject_points)
			else:
				print "Status Code Error: {}".format(request.status_code)
		except:
			# Error parsing json
			print "Invalid JSON."

	except:
		# Error with url
		print "Request error."