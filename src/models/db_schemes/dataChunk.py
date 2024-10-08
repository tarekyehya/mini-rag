from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson.objectid import ObjectId

class DataChunk(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    chunk_text: str = Field(...,min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(...,gt=0)
    chunk_project_id: ObjectId
    chunk_asset_id: ObjectId # ever chunck belong to any asset ?
    
   
    
    # to avoid treate with ObjectId data type
    class Config:
        arbitrary_types_allowed = True
        
    @staticmethod
    def get_indexes():
        
        return [
            {
            
            "key":[
                ("chunk_project_id",1)
            ],
            "name": "chunk_project_id_index_1",
            "unique": False
            
        }
            ]
    