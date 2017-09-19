import requests

from bs4 import BeautifulSoup

searchNumber = input("Insert searchNumber: ")
url = "https://my.maerskline.com/tracking/search"
payload = {"searchNumber":searchNumber}
headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
req = requests.get(url, params=payload, headers=headers)
html = BeautifulSoup(req.text, 'html.parser')

container_info = html.select(".schedule-table")

html_contents = ""

for keyword in container_info:
    container_id = keyword.select_one(".tracking_container_id").text
    origin = html.select("h4.location")
    #load = html.select(".transport-plan-tbl")
    #last_eta = html.select("table.row.container-move.current.transport-plan-tbl.col20")

    print("#### For your shipping search ####")
    print("B/L:",searchNumber)
    print("The container ID:", container_id)
    print("Origin:", origin[0].text)
    print("Destination:", origin[len(origin)-1].text)
    print("Thank you!!!")
