from __future__ import annotations
from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field,ConfigDict
from typing import Annotated
class ItemCreate(BaseModel):
 model_config=ConfigDict(str_strip_whitespace=True)
 title: Annotated[str,Field(min_length=1,max_length=120)]
 priority: Annotated[int,Field(ge=1,le=5)]=3
class Item(ItemCreate): id:int
class ItemRepository:
 def __init__(self): self.items={}; self.next_id=1
 def create(self,data:ItemCreate):
  item=Item(id=self.next_id,**data.model_dump()); self.items[self.next_id]=item; self.next_id+=1; return item
 def get(self,item_id:int): return self.items.get(item_id)
 def delete(self,item_id:int): return self.items.pop(item_id,None)
app=FastAPI(title='Study Items API',version='1.0.0',description='API RESTful didática com contrato OpenAPI')
repo=ItemRepository()
@app.get('/healthz',tags=['system'])
def health(): return {'status':'ok'}
@app.get('/items',response_model=list[Item],tags=['items'])
def list_items(): return list(repo.items.values())
@app.post('/items',response_model=Item,status_code=status.HTTP_201_CREATED,tags=['items'])
def create_item(payload:ItemCreate): return repo.create(payload)
@app.get('/items/{item_id}',response_model=Item,tags=['items'])
def get_item(item_id:int):
 item=repo.get(item_id)
 if item is None: raise HTTPException(status_code=404,detail='item not found')
 return item
@app.delete('/items/{item_id}',status_code=status.HTTP_204_NO_CONTENT,tags=['items'])
def delete_item(item_id:int):
 if repo.delete(item_id) is None: raise HTTPException(status_code=404,detail='item not found')
