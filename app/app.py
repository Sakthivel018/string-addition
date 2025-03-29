from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
import re

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def add_numbers(input_text: str):
    """Extracts numbers from input and returns their sum."""
    try:
        numbers = re.findall(r"-?\d+\.?\d*", input_text)
        return sum(map(float, numbers))
    except Exception:
        return "Invalid input"

@app.get("/", response_class=HTMLResponse)
async def serve_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/add")
async def calculate_sum(request: Request, numbers: str = Form(...)):
    result = add_numbers(numbers)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
