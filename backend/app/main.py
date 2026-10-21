from fastapi import FastAPI

app = FastAPI(
    title="CivilOS",
    description="Validated Knowledge Creation System",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "system": "CivilOS",
        "version": "0.1.0",
        "status": "active",
        "principle": "If it is not real, it is not shown."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
