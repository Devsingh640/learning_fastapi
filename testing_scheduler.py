from time import sleep

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

import asyncio

async def job_first():
    print("Started executing task in background")
    await asyncio.sleep(5)
    print("Task executing completed in background")

async def my_daily_task(i):
    print(f"I performed my todays task {i}")
    await asyncio.sleep(5)

async def main():
    scheduler = AsyncIOScheduler()
    try:
        scheduler.add_job(job_first, IntervalTrigger(seconds=10), id="job_first")
        scheduler.start()

        i = 1
        while True:
            await my_daily_task(i)
            i+=1
    except Exception as error:
        print("Error: ", error)
    finally:
        if scheduler:
            scheduler.shutdown()
        else:
            pass
        pass



if __name__ == "__main__":
    asyncio.run(main())