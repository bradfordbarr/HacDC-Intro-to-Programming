import json
import urllib2

URL = "http://bitly.measuredvoice.com/bitly_archive/usagov_bitly_data2011-06-16-1308257921"

def main():
	page_file = urllib2.urlopen(URL)
	data = []
	for row in page_file:
		# strip the white space off the ends of the row
		row = row.strip()

		# if the row is empty we don't want to bother trying to process
		if row == '':
			continue

		# Try to parse the json string, if it errors ignore it and contine
		try:
			datum = json.loads(row)
		except:
			continue

		# print the latitude and longitude of the person clicking
		# or unknown location if it doesn't have a geotag
		# help(dict.get) for more information on that function
		print datum.get('ll', 'Unknown location')

		# append the datum to the data list for later processing
		data.append(datum)

if __name__ == "__main__":
	main()
