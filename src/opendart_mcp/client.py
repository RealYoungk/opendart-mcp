import json

import httpx


class OpenDartClient:
    """OpenDART API HTTP 클라이언트"""

    BASE_URL = "https://opendart.fss.or.kr/api"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self._http: httpx.AsyncClient | None = None

    @property
    def http(self) -> httpx.AsyncClient:
        if self._http is None or self._http.is_closed:
            self._http = httpx.AsyncClient(timeout=30.0)
        return self._http

    async def get(self, endpoint: str, params: dict | None = None) -> dict:
        """JSON 응답을 반환하는 API 호출"""
        if params is None:
            params = {}
        params["crtfc_key"] = self.api_key
        response = await self.http.get(
            f"{self.BASE_URL}/{endpoint}.json", params=params
        )
        response.raise_for_status()
        return response.json()

    async def get_binary(self, endpoint: str, params: dict | None = None) -> bytes:
        """바이너리(ZIP) 파일을 반환하는 API 호출"""
        if params is None:
            params = {}
        params["crtfc_key"] = self.api_key
        response = await self.http.get(
            f"{self.BASE_URL}/{endpoint}.xml", params=params
        )
        response.raise_for_status()
        return response.content

    async def close(self):
        if self._http and not self._http.is_closed:
            await self._http.aclose()


def format_response(data: dict) -> str:
    """API 응답을 읽기 좋은 JSON 문자열로 변환"""
    return json.dumps(data, ensure_ascii=False, indent=2)
