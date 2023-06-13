import os
from fastapi import FastAPI, Depends, HTTPException, Request
from pydantic import BaseModel
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
import hashlib

app = FastAPI()

# Master key to keep track of access
MASTER_KEY = "master_key"

# Define the available models and their directories
models = {
    "serpapi/bert-base-local-results": "./google/bert-base-local-results"
}

# Load the models
classifiers = {}
for model_name, model_dir in zip(models.keys(), models.values()):
    model_path = os.path.join(model_dir)
    config = AutoConfig.from_pretrained(model_dir)
    model = AutoModelForSequenceClassification.from_pretrained(model_dir, config=config)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    classifiers[model_name] = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Pydantic model for request input validation
class ClassificationInput(BaseModel):
    inputs: str

def authenticate(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header.split(" ")[0].lower() != "bearer" or hashlib.sha256(auth_header.split(" ")[1].encode()).hexdigest() != hashlib.sha256(MASTER_KEY.encode()).hexdigest():
        raise HTTPException(status_code=401, detail="Invalid Master Key")
    return auth_header

# Define the endpoints for each model
for model_name in models.keys():
    endpoint = f"/models/{model_name}"
    
    @app.post(endpoint)
    async def classify(input_data: ClassificationInput, master_key: str = Depends(authenticate)):
        # Validate the input data
        if not input_data.inputs:
            error_message = {
                "error": [
                    "Error in `inputs`: field required"
                ]
            }
            raise HTTPException(status_code=400, detail=error_message)
                
        output = classifiers[model_name](input_data.inputs, top_k=len(classifiers[model_name].model.config.id2label))
        return output

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
