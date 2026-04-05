#async IO helps to run multiple functions concurrently without blocking the main thread.
import time
import asyncio
import requests
async def function1():
    await asyncio.sleep(1)  # Simulating an asynchronous operation
    print("Function 1 completed")
    return 'Daksh'

async def function2():
    # await asyncio.sleep(1)  # Simulating an asynchronous operation
    # print("Function 2 completed")
    URl="https://instagram.com/favicon.ico"
    response=requests.get(URl)
    open("favicon.ico","wb").write(response.content)
    return 'Singhal'

async def function3():
    await asyncio.sleep(4)
    print("Function 3 completed")
    return 'Aarushi Garg'

async def main():
    L=await asyncio.gather(function1(), function2(), function3())
    print(L)
    # task=asyncio.create_task(function1())
    # # await function1()
    # await function2()
    # await function3()

asyncio.run(main())