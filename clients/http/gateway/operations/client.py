from typing import TypedDict

from clients.http.client import HTTPClient
from httpx import Response, QueryParams

from clients.http.gateway.client import build_gateway_http_client


class GetOperationsQueryDict(TypedDict):
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    accountId: str


class MakeOperationRequestDict(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str


class OperationDict(TypedDict):
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str
    createdAt: str


class GetOperationResponseDict:
    operation: OperationDict


class OperationReceiptDict(TypedDict):
    url: str
    document: str

class OperationReceiptResponseDict(TypedDict):
    receipt: OperationReceiptDict

class GetOperationsResponseDict(TypedDict):
    operations: list[OperationDict]

class OperationsSummaryDict(TypedDict):
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class GetOperationsSummaryResponseDict(TypedDict):
    summary: OperationsSummaryDict

class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeFeeOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeTopUpOperationResponseDict(TypedDict):
    operation: OperationDict

class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeCashbackOperationResponseDict(TypedDict):
    operation: OperationDict

class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeTransferOperationResponseDict(TypedDict):
    operation: OperationDict


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    category: str


class MakePurchaseOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeBillPaymentOperationResponseDict(TypedDict):
    operation: OperationDict

class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeCashWithdrawalOperationResponseDict(TypedDict):
    operation: OperationDict


class OperationsGatewayHTTPClient(HTTPClient):
    """Клиент для взаимодействия с /api/v1/operations сервиса http-gateway."""

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id
        :param operation_id: id операции
        :return: Объект httpx.Response с данными по операции
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id
        :param operation_id: id операции
        :return: Объект httpx.Response с данными по чеку операции
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета
        :param query: Словарь с параметрами запроса, например {"accountId": accountId}
        :return: Объект httpx.Response с данными списков операций для переданного счета
        """
        return self.get(f"/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета.
        :param query: Словарь с параметрами запроса, например {"accountId": accountId}
        :return: Объект httpx.Response с данными по статистике операций для определенного счета
        """
        return self.get(f"/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создание операции комиссии
        :param request: Словарь с данными запроса, например
        {
          "status": "FAILED",
          "amount": 0,
          "cardId": "string",
          "accountId": "string"
        }
        :return: Объект httpx.Response с данными по созданной операции комиссии
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создание операции пополнения
        :param request: Словарь с данными запроса, например
        {
          "status": "FAILED",
          "amount": 0,
          "cardId": "string",
          "accountId": "string"
        }
        :return: Объект httpx.Response с данными по операции пополнения
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка.
        :param request: Словарь с данными запроса, например
        {
          "status": "FAILED",
          "amount": 0,
          "cardId": "string",
          "accountId": "string"
        }
        :return: Объект httpx.Response с данными по операции кешбека
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создание операции перевода.
        :param request: Словарь с данными запроса, например
        {
            "status": "FAILED",
            "amount": 0,
            "cardId": "string",
            "accountId": "string"
        }
        :return: Объект httpx.Response с данными по операции перевода
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки.
        :param request: Словарь с данными запроса, например
        {
          "status": "FAILED",
          "amount": 0,
          "cardId": "string",
          "accountId": "string",
          "category": "string"
        }
        :return: Объект httpx.Response с данными по операции покупки
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету
        :param request: Словарь с данными запроса, например
        {
            "status": "FAILED",
            "amount": 0,
            "cardId": "string",
            "accountId": "string",
        }
        :return: Объект httpx.Response с данными по операции оплаты по счету
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных денег.
        :param request: Словарь с данными запроса, например
        {
            "status": "FAILED",
            "amount": 0,
            "cardId": "string",
            "accountId": "string",
        }
        :return: Объект httpx.Response с данными по созданной операции снятия наличных
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> OperationReceiptResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category="some_category"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
