from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


# Global variable to hold the vector store
vector_store = None

# Define your CORS policy
CORS_POLICY = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}

@asynccontextmanager
async def lifespan(app: FastAPI):
    global vector_store
    print("Running initialization tasks before server starts.")
    # Initialize the processor and load data
    processor = WikipediaDocumentProcessor(
        query="Cricket and everything related to cricket")
    processor.run()
    vector_store = processor.vectorstore
    print("Initialization complete.")
    yield
    print("Shutting Down.... Adios!!")

# --- THIS IS THE LINE THAT WAS MISSING ---
app = FastAPI(lifespan=lifespan)
# -----------------------------------------

# Add the CORSMiddleware to your FastAPI application
app.add_middleware(
    CORSMiddleware,
    **CORS_POLICY
)

class UserInput(BaseModel):
    text: str

@app.get("/api/v1/health")
async def health():
    return {"response": "Alive and well my friend !"}

@app.post("/chat")
async def chat_endpoint(user_input: UserInput):
    # Initialize assistant with the loaded vector_store
    assistant = CricketAssistant(vector_store)
    response = assistant.handle_user_input(user_input.text)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)