from fastapi import FastAPI
from routers import router


app = FastAPI(
    title='Coinvert API',
    description='API para conversão de moedas.',
    version='0.0.1'
)
app.include_router(router=router, tags=['Conversor'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True)
