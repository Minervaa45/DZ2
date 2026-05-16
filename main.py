from fastapi import FastAPI

app = FastAPI(title="BLT Health Service")

@app.get("/health/")
def health():
    return {"status": "OK"}
