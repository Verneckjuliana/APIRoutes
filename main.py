from fastapi import FastAPI
from routes import pokemon_router, pokebolas_router

app = FastAPI()

app.include_router(pokemon_router.router, tags=['Pokemon'])
app.include_router(pokebolas_router.router, tags=['Pokebolas'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='127.0.0.1', port=8080, log_level='info', reload=True)