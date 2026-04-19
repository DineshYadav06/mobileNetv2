from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from app.model import predict_image

app = FastAPI()

# frontend connect ke liye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API running 🚀"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    result = predict_image(file)
    return result