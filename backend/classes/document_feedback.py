from pydantic import BaseModel


class DocumentFeedback(BaseModel):
    document: str
    document_is_code: bool
    feedback: str
