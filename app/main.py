from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/resources", StaticFiles(directory="resources"), name="resources")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = {
        "page": page_name
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@app.get("/user/v1/{user_name}", response_class=HTMLResponse)
async def user_link(request: Request, user_name: str):
    data = {
        "page": user_name +"v1"
    }
    return templates.TemplateResponse("user.html", {"request": request, "data": data})

@app.get("/user/v2/{user_name}", response_class=HTMLResponse)
async def user_link_v2(request: Request, user_name: str):
    data = {
        "page": user_name +"v2"
    }
    return templates.TemplateResponse("user.html", {"request": request, "data": data})