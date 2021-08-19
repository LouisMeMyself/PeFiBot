import asyncio
import json
import requests

from constants import Constants


async def genericQuery(query):
    r = requests.post(Constants.PANGO_API_URL, json={'query': query})
    assert(r.status_code == 200)
    return json.loads(r.text)


async def getAvaxPrice():
    USDTe_query = await genericQuery("""{pair(id:"0xe28984e1ee8d431346d32bec9ec800efb643eef4"){token1Price, reserve1}}""")
    DAIe_query = await genericQuery("""{pair(id:"0xba09679ab223c6bdaf44d45ba2d7279959289ab0"){token1Price, reserve1}}""")
    avaxPriceUSDTe = float(USDTe_query["data"]["pair"]["token1Price"])
    avaxPriceDAIe = float(DAIe_query["data"]["pair"]["token1Price"])
    usdte_liq = float(USDTe_query["data"]["pair"]["reserve1"])
    daie_liq = float(DAIe_query["data"]["pair"]["reserve1"])
    sum_liq = usdte_liq + daie_liq
    return avaxPriceUSDTe * (usdte_liq / sum_liq) + avaxPriceDAIe * (daie_liq / sum_liq)

async def getPefiPrice():
    avaxPrice = await getAvaxPrice()
    pefiAVAXratio = float((await genericQuery("""{pair(id: "0x494dd9f783daf777d3fb4303da4de795953592d0") {token0Price}}"""))["data"]["pair"]["token0Price"])
    return avaxPrice * pefiAVAXratio

# print(asyncio.run(getPefiPrice()))