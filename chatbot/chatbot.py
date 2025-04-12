from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

mascotas = {
    "Bobby": {"raza": "Labrador", "edad": "3 años", "salud": "Vacunado"},
    "Luna": {"raza": "Poodle", "edad": "2 años", "salud": "Vacunada"},
}

class Pregunta(BaseModel):
    mensaje: str

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def responder(pregunta: Pregunta):
    mensaje = pregunta.mensaje.lower()

    if "perros" in mensaje or "mascotas" in mensaje:
        return {"respuesta": f"Tenemos disponibles: {', '.join(mascotas.keys())}"}
    elif "requisitos" in mensaje:
        return {"respuesta": "Debes ser mayor de edad y llenar el formulario de adopción. ¿Te gustaría que te lo envíe?"}
    elif "bobby" in mensaje:
        info = mascotas.get("Bobby")
        return {"respuesta": f"Bobby es un {info['raza']}, tiene {info['edad']} y está {info['salud']}."}
    elif "luna" in mensaje:
        info = mascotas.get("Luna")
        return {"respuesta": f"Luna es un {info['raza']}, tiene {info['edad']} y está {info['salud']}."}
    else:
        return {"respuesta": "Mmm... no entendí muy bien 🐶. ¿Podrías repetirlo de otra forma?"}
