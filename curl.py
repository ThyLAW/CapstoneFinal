import pycurl

# try python 3, if not work, try python 2
try:
    # python 3
    from urllib.parse import urlencode


except ImportError:
    # python 2
    from urllib import urlencode


def xss():

    # input post field
    mydata = "string=<script>alert('XSS!')</script>"
    # data to grep
    search_data = "<script>alert('XSS!')</script>"

    # curl and save to file to grep later
    with open('out.html', 'wb') as f:

        # intiialize pycurl and set url
        c = pycurl.Curl()
        c.setopt(c.URL, 'http://localhost:5000/home')

        # set options to be post request
        c.setopt(c.POSTFIELDS, mydata)

        # set option of pycurl to write to file
        c.setopt(c.WRITEDATA, f)

        # execute and close (return results)
        c.perform()
        c.close()

    # intialize binary to determine if XSS found
    foundXSS = 0

    # open file and iterate through each line,
    # if line detected change 'foundXSS' to true (1)
    with open('out.html', 'r') as f:
        for line in f:
            if search_data in line:
                foundXSS = 1
                print(line)
                break

    if foundXSS == 1:
        print("XSS Found!")
        return foundXSS
    else:
        print("No XSS Found!")
        return foundXSS


xss()
