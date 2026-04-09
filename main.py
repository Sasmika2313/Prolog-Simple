from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pyswip import Prolog   # assume SWI-Prolog + PySwip installed

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class DiagnoseInput(BaseModel):
    engine_cranks: str
    battery_ok: str
    lights_dim: str
    brake_noise: str
    engine_overheat: str
    engine_power_loss: str
    steering_vibrate: str
    engine_cranks_but_not_start: str
    alternator_ok: str

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/diagnose")
async def diagnose_handler(inp: DiagnoseInput):
    prolog = Prolog()
    prolog.consult("diagnose.pl")

    # assert facts
    prolog.assertz(f"engine_cranks({inp.engine_cranks.lower()})")
    prolog.assertz(f"battery_ok({inp.battery_ok.lower()})")
    prolog.assertz(f"lights_dim({inp.lights_dim.lower()})")
    prolog.assertz(f"brake_noise({inp.brake_noise.lower()})")
    prolog.assertz(f"engine_overheat({inp.engine_overheat.lower()})")
    prolog.assertz(f"engine_power_loss({inp.engine_power_loss.lower()})")
    prolog.assertz(f"steering_vibrate({inp.steering_vibrate.lower()})")
    prolog.assertz(f"engine_cranks_but_not_start({inp.engine_cranks_but_not_start.lower()})")
    prolog.assertz(f"alternator_ok({inp.alternator_ok.lower()})")

    # query for faults
    results = list(prolog.query("fault(X)"))
    faults = [r["X"] for r in results]

    if not faults:
        faults = ["no_obvious_fault"]

    return {"faults": faults}
