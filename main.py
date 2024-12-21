from fastapi import FastAPI, UploadFile, HTTPException
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from typing import List
import io
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.post("/analyze-csv/")
async def analyze_csv(file: UploadFile):
    # Validate the file type
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV")

    try:
        # Read the uploaded CSV file
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))

        # Validate required columns
        required_columns = {'id', 'text', 'timestamp'}
        if not required_columns.issubset(df.columns):
            raise HTTPException(status_code=400, detail=f"CSV must contain columns: {required_columns}")

        # Perform sentiment analysis
        results = []
        for _, row in df.iterrows():
            sentiment = analyzer.polarity_scores(row['text'])
            results.append({
                "id": row['id'],
                "sentiment": "Positive" if sentiment['compound'] > 0.05 else "Negative" if sentiment['compound'] < -0.05 else "Neutral"
            })

        return {"results": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
