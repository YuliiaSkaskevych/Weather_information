import datetime
import aiohttp
import asyncio


async def seven_f(session):
    url = 'https://www.7timer.info/bin/astro.php?lon=36.232845&lat=49.988358&ac=0&unit=metric&output=json&tzshift=0'
    async with session.get(url) as response:
        print('Current status: ', response.status)
        print(f'Site: {url}')
        data = await response.json(content_type='text/html')
        temperature = data['dataseries'][0]['temp2m']
    return temperature


async def meta_f(session):
    url = 'https://goweather.herokuapp.com/weather/Curitiba'
    async with session.get(url) as response:
        print('Current status: ', response.status)
        print(f'Site: {url}')
        data = await response.json()
        t = data['temperature']
        t1 = t.split()
        temperature = int(t1[0])
    return temperature


async def open_f(session):
    url = 'https://api.open-meteo.com/v1/forecast?latitude=49.988358&longitude=36.232845&current_weather=True'
    async with session.get(url) as response:
        print('Current status: ', response.status)
        print(f'Site: {url}')
        data = await response.json()
    temperature = data['current_weather']['temperature']
    return temperature


async def main():
    async with aiohttp.ClientSession() as session:
        temp = await asyncio.gather(seven_f(session), meta_f(session), open_f(session))
        average_temp_kh = round(sum(temp) / len(temp), 2)
    return average_temp_kh


if __name__ == '__main__':
    now = datetime.datetime.now()
    print(f'Start: {now.time()}')
    print(f'Average temperature: {asyncio.run(main())} °C')
    print(f'Stop')
