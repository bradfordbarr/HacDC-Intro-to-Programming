import json
import urllib2

URL = "http://bitly.measuredvoice.com/bitly_archive/usagov_bitly_data2011-06-16-1308257921"

# This code downloads data for an upcoming hackathon
# It's format goes a little something like this:
#{
#	"a": USER_AGENT,
#	"c": COUNTRY_CODE, # 2-character iso code
#	"nk": KNOWN_USER,  # 1 or 0. 0=this is the first time we've seen this browser
#	"g": GLOBAL_BITLY_HASH,
#	"h": ENCODING_USER_BITLY_HASH,
#	"l": ENCODING_USER_LOGIN,
#	"hh": SHORT_URL_CNAME,
#	"r": REFERRING_URL,
#	"u": LONG_URL,
#	"t": TIMESTAMP,
#	"gr": GEO_REGION,
#	"ll": [LATITUDE, LONGITUDE],
#	"cy": GEO_CITY_NAME,
#	"tz": TIMEZONE # in http://en.wikipedia.org/wiki/Zoneinfo format
#} 

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
