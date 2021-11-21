Response=$(curl -X POST http://127.0.0.1:5000/home --data "string=<script>alert('XSS')</script>")
if [[ $? -gt 0 ]]
then echo "Error connecting to website."
else
    if [[ ! -z $(echo ${Response} | grep "<script>alert('XSS')</script>") ]]
    then echo "FAIL: XSS detected in website."
    else echo "PASS: XSS mitigated in website."
    fi
fi
