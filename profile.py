import requests

def print_message(username, badge_count, subject, points):
	print "{} has {} badges and {} points in {}".format(username, badge_count, points, subject)

def get(username, subject):
	try:
		request = requests.get("http://teamtreehouse.com/{}.json".format(username))

		try:
			if request.status_code == 200:
				json = request.json()
				badge_count = len(json["badges"])
				subject_points =  json["points"][subject]
				name = json["name"]
				print_message(name, badge_count, subject, subject_points)
			else:
				print "Status Code Error: {}".format(request.status_code)
		except:
			print "Invalid JSON."

	except:
		print "Request error."