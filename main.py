
from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import uvicorn

# Set up the OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(request: Request, chat_request: ChatRequest):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=chat_request.prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.7,
        )

        chat_response = response.choices[0].text.strip()
        return {"response": chat_response}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpenAI Assistant</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container my-5">
        <h1 class="text-center">OpenAI Assistant</h1>
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-body">
                        <form id="chat-form">
                            <div class="mb-3">
                                <label for="prompt" class="form-label">Enter a prompt:</label>
                                <textarea class="form-control" id="prompt" rows="3" required></textarea>
                            </div>
                            <button type="submit" class="btn btn-primary">Submit</button>
                        </form>
                        <div id="response-container" class="mt-3"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const chatForm = document.getElementById('chat-form');
        const responseContainer = document.getElementById('response-container');

        chatForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const prompt = document.getElementById('prompt').value;

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ prompt: prompt })
                });

                const data = await response.json();

                if (data.error) {
                    responseContainer.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
                } else {
                    responseContainer.innerHTML = `<div class="alert alert-success">${data.response}</div>`;
                }
            } catch (error) {
                responseContainer.innerHTML = `<div class="alert alert-danger">An error occurred: ${error.message}</div>`;
            }
        });
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
