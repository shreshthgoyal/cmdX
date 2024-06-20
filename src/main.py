from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.retriever.initialise import vector_db
from src.agents.ragAgent import LC_AgentExecutor
from src.models.rag_query import QueryInput, QueryOutput
from src.apiResponse.message import apiMessage
from src.retriever.create_retriever import CreateRetriever


app = FastAPI(
    title="Shell AI",
    description="Bridging gap between shell and AI",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

retriever_instace = CreateRetriever(vector_db)
retriever = retriever_instace.get_retriever()
agent_executor = LC_AgentExecutor(retriever).get_executor()

async def invoke_agent_with_retry(query: str):
    if(query != None):
        return await agent_executor.ainvoke({"input": query})
    else:
        return f"There seems to be some issue with this query, can you try this again?"

@app.get("/healthcheck")
async def get_status():
    return {"status": "running"}

@app.post("/query", response_model=QueryOutput)
async def query_agent(query: QueryInput) -> QueryOutput:
    try:
        query_response = await invoke_agent_with_retry(query.input)
        query_type = query_response['intermediate_steps'][0][0].__dict__['tool']        
        query_response["message"] = apiMessage(query_type, query_response['output'])

        return query_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)

