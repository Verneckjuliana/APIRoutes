from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/pokebolas')
async def get_pokebolas():
    return {'Mensagem': "Retornou todos as Pokebolas"}