import uvicorn

if __name__ == "__main__":
    host = "0.0.0.0"
    """
    runs the application both on localhost and system ip
    """
    port = 8000
    reload = True

    # Runs application normally
    # uvicorn.run("main:app", host=host, port=port, reload = False)

    # Runs application in reload mode, tracks for python file changes
    uvicorn.run("main:app", host=host, port=port, reload=reload)
    pass
