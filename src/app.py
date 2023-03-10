import uvicorn
import validators
from fastapi import FastAPI

from .scrape import scrape_img, scrape_link

app = FastAPI()


@app.get("/api/img")
@app.get("/api/imgs")
@app.get("/api/image")
@app.get("/api/images")
def get_img(url: str = None):
    if url is None:
        return {"status": 400, "message": "URL parameter required."}
    elif not validators.url(url):
        return {"status": 400, "message": "URL invalid."}
    return scrape_img(url)


@app.get("/api/links")
@app.get("/api/link")
@app.get("/api/a")
@app.get("/api/href")
def get_link(url: str = None):
    if url is None:
        return {"status": 400, "message": "URL parameter required."}
    elif not validators.url(url):
        return {"status": 400, "message": "URL invalid."}
    return scrape_link(url)


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
