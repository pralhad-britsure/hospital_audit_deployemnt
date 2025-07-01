from pydantic import BaseModel

class RandomCodeResponse(BaseModel):
    code: str
