from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.serie import SerieModel
from app.schema.serie import SerieSchema
 
router = APIRouter()
 
@router.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie
 
@router.get("/series")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()
 
@router.put("/series/{serie_id}")
async def atualizar_serie(serie_id: int, dados: SerieSchema, db: Session = Depends(get_db)):
    serie = db.query(SerieModel).filter(SerieModel.id == serie_id).first()
    if not serie:
         raise HTTPException(status_code=404, detail="Série não encontrada")
    for chave, valor in dados.model_dump().items():
        setattr(serie, chave, valor)
    db.commit()
    db.refresh(serie)
    return serie
 
@router.delete("/series/{serie_id}")
async def deletar_serie(serie_id: int, db: Session = Depends(get_db)):
 
    serie = db.query(SerieModel).filter(SerieModel.id == serie_id).first()
 
    if not serie:
        raise HTTPException(status_code=404, detail="Série não encontrada")
 
    db.delete(serie)
    db.commit()
 
    return {"mensagem": "Série deletada com sucesso"}
 
# Tarefa 1: Resolva todos os erros da sua aplicação
# Tarefa 2: Crie as rotas de atualização e deleção da API
# Tarefa 3: Resolva todos erros das nivas rotas
# Versione
 
# Extra: resolva o erro de importação das variáveis de ambiente detectado no módulo python-dotenv e utilize corretamente a importação com a função load_dotenv () em seu database.py
 
 