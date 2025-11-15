import uvicorn
from src.configuration.configuration import settings

if __name__ == "__main__":
    print(settings)
    host = settings.APPLICATION_HOST
    port = settings.APPLICATION_PORT
    reload = settings.APPLICATION_RELOAD

    # Runs application normally
    # uvicorn.run("main:app", host=host, port=port, reload = False)

    uvicorn.run("main:app",
                host=host,
                port=port,
                reload=reload)