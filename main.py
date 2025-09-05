from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Creator OS Backend is Live"}

@app.post("/generate-product")
async def generate_product(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "Generate a product about productivity for creators.")
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"content": response.choices[0].message["content"]}
    except Exception as e:
        return {"error": str(e)}
