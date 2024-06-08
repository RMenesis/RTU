import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.e-latts.lv/products.sale.ppl"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='data-table')
    headers = []
    for th in table.find_all('th'):
        headers.append(th.text.strip())
    data = []
    for row in table.find_all('tr')[1:]:
        row_data = []
        for td in row.find_all('td'):
            row_data.append(td.text.strip())
        data.append(row_data)
    df = pd.DataFrame(data, columns=headers)
    df.to_excel("data.xlsx", index=False)
    print("Successfully")
else:
    print(f"Failed {url}")
