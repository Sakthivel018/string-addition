from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import re

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def add_numbers(input_text: str):
    """Extracts numbers from input and returns their sum."""
    try:
        numbers = re.findall(r"-?\d+\.?\d*", input_text)  # Match integers and decimals
        return sum(map(float, numbers))
    except Exception:
        return "Invalid input"

@app.get("/", response_class=HTMLResponse)
async def serve_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": 0})

@app.post("/add", response_class=JSONResponse)
async def calculate_sum(numbers: str = Form(...)):
    result = add_numbers(numbers)
    return {"result": result}
