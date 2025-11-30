from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

import asyncio

async def job_first():
    print("First Started")
    await asyncio.sleep(1)
    print("First Stopped")

async def job_second():
    print("Second Started")
    await asyncio.sleep(5)
    print("Second Stopped")

async def wait_function(i):
    await asyncio.sleep(i)

async def main():
    scheduler = AsyncIOScheduler()
    try:
        scheduler.add_job(job_first, IntervalTrigger(seconds=2), id="job_first")
        scheduler.add_job(job_second, IntervalTrigger(seconds=6), id="job_second")
        scheduler.start()

        print(scheduler.print_jobs())

        while True:
            await wait_function(1)

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