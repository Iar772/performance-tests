from typing import TypedDict
import httpx
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура данных для создания виртуальной карты.
    """
    userId: str
    accountId: str

class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для создания физической карты.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> httpx.Response:
        """
        Создание новой виртуальной карты
        :param request: Словарь с данными виртуальной карты
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> httpx.Response:
        """
        Создание новой физической карты
        :param request: Словарь с данными физической карты
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Функция создаёт экземпляр CardsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())
