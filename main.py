import aiohttp
import asyncio


async def seven_f(session):
    async with session.get('https://www.7timer.info/bin/astro.php?lon=36.232845&lat=49.988358&ac=0&unit=metric&output=json&tzshift=0') as response:
        print('Current status: ', response.status)
        data = await response.json(content_type='text/html')
    temperature = data['dataseries'][0]['temp2m']
    return temperature


async def meta_f(session):
    async with session.get('https://www.metaweather.com//api/location/922137/') as response:
        print('Current status: ', response.status)
        data = await response.json()
    temperature = data['consolidated_weather'][0]['the_temp']
    return temperature


async def open_f(session):
    async with session.get('https://api.open-meteo.com/v1/forecast?latitude=49.988358&longitude=36.232845&current_weather=True') as response:
        print('Current status: ', response.status)
        data = await response.json()
    temperature = data['current_weather']['temperature']
    return temperature


async def main():
    async with aiohttp.ClientSession() as session:
        temp_kh = await asyncio.gather(seven_f(session), meta_f(session), open_f(session))
        average_temp_kh = round(sum(temp_kh) / len(temp_kh), 2)
        print(average_temp_kh)


if __name__ == '__main__':
    asyncio.run(main())