import requests
import meraki

# version = v1


url='https://api.meraki.com/api/v1/organizations'

querystring= {}
header ={
    'X-Cisco-Meraki-API-Key': '9db387682aabec72abd403510cc1584db84fc34b'
}

response = requests.request("GET", url, headers=header)
print(response)
print(response.text.encode('utf8'))



#dashboard = meraki.DashboardAPI()


# curl --request GET -L \
#  --url https://api.meraki.com/api/v0/organizations \
# --header 'X-Cisco-Meraki-API-Key: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
