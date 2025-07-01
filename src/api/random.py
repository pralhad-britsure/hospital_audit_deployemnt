from fastapi import APIRouter
from random import choices
import string

from src.schema.random  import RandomCodeResponse

router = APIRouter()

@router.get("/generate-code", response_model=RandomCodeResponse)
def generate_code():
    characters = string.ascii_uppercase + string.digits
    random_code = ''.join(choices(characters, k=9))
    return RandomCodeResponse(code=random_code)
