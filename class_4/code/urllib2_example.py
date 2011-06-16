#!/usr/bin/python
# example of using urllib2 to save the contents of a page
# not the best way to do this, but it illustrates the example

# import the module
import urllib2

#what site are we going to download
url = 'http://wiki.hacdc.org/index.php/Intro_to_Programming'

# open the url
page_file = urllib2.urlopen(url)

# read the data into some variable
data = page_file.read()

# open a file to write the data to
output_file = open('programming_page.html', 'w')
# write the data and close the file
output_file.write(data)
output_file.close()
