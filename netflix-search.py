import requests

url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

querystring = {"q":"get:new7-!1900,2018-!0,5-!0,10-!0-!Any-!Any-!Any-!gt100-!{downloadable}","t":"ns","cl":"all","st":"adv","ob":"Relevance","p":"1","sa":"and"}


headers = {
    'x-rapidapi-key': "1b98ef7d09mshabaecd87791b644p15683ajsn2320608ee0da",
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
