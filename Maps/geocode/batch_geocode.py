import urllib
import urllib2
import json


def fetch_singleGeocode(house_street):
	url = 'http://geocoding.geo.census.gov/geocoder/locations/onelineaddress'
	address = house_street + ", New York, NY," 
	values = {'address' : address , 'benchmark':9, 'format': 'json'}

	data = urllib.urlencode(values)
	fullurl = url + '?' + data
	# print fullurl
	response = urllib2.urlopen(fullurl)
	page = response.read()
	json_answer = json.loads(page)
	# print json_answer
	if len (json_answer[unicode('result')][unicode('addressMatches')]) >0:
		address = json_answer[unicode('result')][unicode('addressMatches')][0]
		lat = address[unicode('coordinates')][unicode('x')]
		long = address[unicode('coordinates')][unicode('y')]
		return [long, lat]	
	return False
def grab_addresses(issuer_id, date_input):
	url = 'http://data.cityofnewyork.us/resource/jt7v-77mi.json'
	date_format = date_input+'T00:00:00'
	value = {'$select':'house_number, street_name', 'issuer_code':issuer_id,'$where':'intersecting_street IS NULL', 'issue_date':date_format}	
	fullurl = url + '?'+ urllib.urlencode(value)
	print fullurl
	response = urllib2.urlopen(fullurl)
	page = response.read()
	json_answer = json.loads(page)
	return json_answer
	
	
def batch_fetch():
	url = 'http://geocoding.geo.census.gov/geocoder/locations/addressbatch'
	values = {'benchmark': 9, 'addressfile': 'test_census_geocode.csv'}
	data = urllib.urlencode(values)
	response = urllib2.urlopen(url, data)
	page = response.read()
	print page

def requestGeocode(issuer_id, date):
	return_list = []
	for result in grab_addresses(issuer_id, date):
		address = result[unicode('house_number')]+ ' '+ result[unicode('street_name')]
		geo_code = fetch_singleGeocode(address)
		if geo_code:
			return_list.append([address, geo_code])
	return return_list
if __name__ == '__main__':
	address1 = '736 W 151st St'
	zip1 = 10031
	# fetch_singleGeocode(address1, zip1)
	# batch_fetch()
	for items in requestGeocode(354098, '2013-07-29'):
		print items
