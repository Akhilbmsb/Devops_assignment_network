import requests
import time
from tabulate import tabulate

websitedomains = ['vlearn.herovired.com', 'herovired.com', 'vlearnv.herovired.com',
'help.herovired.com']

def statuschecking(websitedomain):
    try:
        # passing each domain inside request to fetch its status and check with condition of its status code it is up or down
        res = requests.get(f'http://{websitedomain}')
        return 'Up' if res.status_code == 200 else 'Down'
    except requests.exceptions.RequestException:
        return 'Down'

def websiteDomainsCheckingMain():
    while True:
        finalresults = []
        for websitedomain in websitedomains:
            status = statuschecking(websitedomain)
            finalresults.append([websitedomain, status])
        print(tabulate(finalresults, headers=["websitedomainlist", "Status"], tablefmt="heavy_outline"))
        time.sleep(60)

if __name__ == "__main__":
    websiteDomainsCheckingMain()

    
