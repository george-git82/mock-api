from fastapi import FastAPI
import datetime
import os

app = FastAPI()

@app.get("/api/health")
def health():
    return {
        "service": "mock-api",
        "status": "UP",
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
