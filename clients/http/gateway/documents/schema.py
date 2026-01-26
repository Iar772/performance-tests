from pydantic import BaseModel

class DocumentSchema(BaseModel):
    """
    Структура данных для создания документа.
    """
    url: str
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения тарифного
    """
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения контракта
    """
    contract: DocumentSchema