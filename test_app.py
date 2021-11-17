import requests
url = "http://localhost:5000/posts"
mydata = "string=<script>alert('XSS!')</script>"

x = requests.post(url)
print(x.content)
# curl -X POST http://127.0.0.1:5000/home --data "string=<script>alert('XSS!')</script>