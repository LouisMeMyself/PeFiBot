import asyncio
import json
import requests

from constants import Constants


async def genericQuery(query):
    r = requests.post(Constants.PANGO_API_URL, json={'query': query})
    assert(r.status_code == 200)
    return json.loads(r.text)


async def getAvaxPrice():
    USDTPrice = await genericQuery("""{pair(id: "0x9ee0a4e21bd333a6bb2ab298194320b8daa26516") {token1Price}}""")
    DAIPrice = await genericQuery("""{pair(id: "0x17a2e8275792b4616befb02eb9ae699aa0dcb94b") {token1Price}}""")
    return float(USDTPrice["data"]["pair"]["token1Price"]) / 2 + float(DAIPrice["data"]["pair"]["token1Price"]) / 2

async def getPefiPrice():
    avaxPrice = await getAvaxPrice()
    pefiUSDTratio = float((await genericQuery("""{pair(id: "0x94df699f8aa08314cbdfcca7dd6cfaa5ab9e8e26") {token0Price}}"""))["data"]["pair"]["token0Price"])
    pefiAVAXratio = float((await genericQuery("""{pair(id: "0x494dd9f783daf777d3fb4303da4de795953592d0") {token0Price}}"""))["data"]["pair"]["token0Price"])
    return (avaxPrice * pefiAVAXratio + pefiUSDTratio) / 2

# print(asyncio.run(getPefiPrice()))