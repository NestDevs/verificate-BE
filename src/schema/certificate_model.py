from pydantic import BaseModel
from src.schema.questions_model import Category,Level

class Certificate(BaseModel):
    """Model for certificate data."""
    user_id: str
    category: Category
    level: Level
    ipfs_hash: str
    certificate_hash: str
    certificate_view_url: str
    issued_by: str = "Verificate"
    date_issued: str
    