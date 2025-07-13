from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


class Numbers(BaseModel):
    a: float
    b: float


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/add", response_class=HTMLResponse)
async def add_form(request: Request, a: float = Form(...), b: float = Form(...)):
    result = a + b
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
