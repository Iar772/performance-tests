from pydantic import BaseModel, ConfigDict, Field
from enum import StrEnum

from tools.fakers import fake


class OperationType(StrEnum):
    """
    Структура данных по операциям с картой.
    """
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"

class OperationStatus(StrEnum):
    """
    Структура данных по статусам операций с картами.
    """
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Структура данных по карте.
    """
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    cardId: str
    accountId: str
    category: str
    createdAt: str


class GetOperationResponseSchema(BaseModel):
    """
    Структура данных ответа по получению операции.
    """
    operation: OperationSchema


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных по параметрам запроса на получение операций.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных по параметрам запроса на получение саммари по операциям.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class MakeOperationRequestSchema(BaseModel):
    """
    Структура данных по запросу создания операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Структура данных по запросу на ответ получения чека.
    """
    url: str
    document: str

class OperationReceiptResponseSchema(BaseModel):
    """
    Структура данных по запросу на ответ получения чека.
    """
    receipt: OperationReceiptSchema

class GetOperationsResponseSchema(BaseModel):
    """
    Структура данных по запросу на получение списка операций.
    """
    operations: list[OperationSchema]

class OperationsSummarySchema(BaseModel):
    """
    Структура данных на получение саммари по операциям.
    """
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")

class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Структура данных на получение саммари по операциям.
    """
    summary: OperationsSummarySchema

class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных на запрос для /api/v1/operations/make-fee-operation
    """
    pass

class MakeFeeOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос /api/v1/operations/make-fee-operation.
    """
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных на запрос для /api/v1/operations/make-top-up-operation.
    """
    pass

class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос /api/v1/operations/make-top-up-operation.
    """
    operation: OperationSchema

class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных на запрос для /api/v1/operations/make-cashback-operation.
    """
    pass

class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос /api/v1/operations/make-cashback-operation
    """
    operation: OperationSchema

class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных на запрос для /api/v1/operations/make-transfer-operation.
    """
    pass


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Структура данных на запрос для /api/v1/operations/make-transfer-operation
    """
    operation: OperationSchema


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных на запрос для /api/v1/operations/make-purchase-operation.
    """
    category: str = Field(default_factory=fake.category)


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос /api/v1/operations/make-purchase-operation.
    """
    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных на запрос для /api/v1/operations/make-bill-payment-operation.
    """
    pass

class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос /api/v1/operations/make-bill-payment-operation.
    """
    operation: OperationSchema

class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных на запрос для /api/v1/operations/make-cash-withdrawal-operation.
    """
    pass

class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос для /api/v1/operations/make-cash-withdrawal-operation.
    """
    operation: OperationSchema
