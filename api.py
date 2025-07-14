from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from main import prediction

app = FastAPI()

# pydantic schema
class TextRequest(BaseModel):
    text: str

# prediction function
@app.post("/predict")
def predict(request: TextRequest):
    text = request.text
    try:
        result = prediction(text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# run server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8008)