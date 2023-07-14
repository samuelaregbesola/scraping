import requests
import json
import pandas as pd

shoes = []
anchor = 0
fetching = True

while fetching:
    url = f"https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=C8F8C0F14B39070F06EB813DBAC3F4CC&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C8529ff38-7de8-4f69-973c-9fdbfb102ed2)%26anchor%3D{anchor}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D50&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D"
    response = requests.request("GET", url)
    json_data = json.loads(response.text)
    shoes += json_data['data']['products']['products']
    print(shoes)
    if json_data['data']['products']['pages']['next'] != '':
        anchor += 50
    else:
        fetching = False




# process the shoes data
shoes

data = []
for shoe in shoes:
    id = shoe['pid']
    title = shoe['title']
    image = shoe['images']['squarishURL']
    price = shoe['price']['currentPrice']
    inStock = shoe['inStock']
    category = shoe['subtitle']
    isNew = shoe["colorways"][0]["isNew"]
    data.append({"id": id, "title": title, "image": image, "price": price, "inStock": inStock, "category": category, "isNew": isNew})

df = pd.DataFrame(data)

df.to_csv('shoes_data.csv', index=False)

df.head()
