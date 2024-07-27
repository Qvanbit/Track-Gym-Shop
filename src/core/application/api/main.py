from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(
        title='Application was successfully created',
        docs_url='/api/docs',
        description='It is a simle application, that tell you, thas all good',
        debug=True,
    )

    @app.get("/")
    async def read_root():
        return {"message": "All good"}
    
    return app