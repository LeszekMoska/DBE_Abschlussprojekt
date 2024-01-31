import requests
r = requests.get("https://api.kurs.dbe.academy/v1/mitarbeiter/gehalt/1234")
print("Status Code: ")
print(r.status_code)
print ("Header: ")
print(r.headers)
print(r.text)

# Status Codes:
# 100 - 199 (Informative Codes)
# 200 - 299 (Erfolgreich)
# 300 - 399 (Umleitung)
# 400 - 499 (Client Fehler)
# 500 - 599 (Server Fehler)