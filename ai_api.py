from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

app = FastAPI(
    title="Tesla Insights AI API",
    description="API per analisi di sentiment e summarization utilizzando modelli Hugging Face.",
    version="1.0"
)

# Specifica i modelli Hugging Face da usare
MODEL_SENTIMENT = "nlptown/bert-base-multilingual-uncased-sentiment"
MODEL_SUMMARIZATION = "sshleifer/distilbart-cnn-12-6"

# Carica le pipeline (caching per evitare caricamenti ripetuti)
sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_SENTIMENT)
summarization_pipeline = pipeline("summarization", model=MODEL_SUMMARIZATION)

class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Benvenuto nell'API Tesla Insights AI. Usa POST /sentiment o POST /summarize."}

@app.post("/sentiment")
def sentiment_analysis(input: TextInput):
    result = sentiment_pipeline(input.text)
    return {"input_text": input.text, "sentiment": result}

@app.post("/summarize")
def summarize_text(input: TextInput):
    # Limitiamo il testo se troppo lungo per il modello
    text = input.text
    if len(text.split()) > 512:
        text = " ".join(text.split()[:512])
    summary = summarization_pipeline(text)
    return {"input_text": input.text, "summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
