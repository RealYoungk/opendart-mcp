"""DS004: 지분공시 종합정보 (Shareholding Disclosure Information) - 2 tools"""

from mcp.server.fastmcp import FastMCP

from opendart_mcp.client import OpenDartClient, format_response


def register_tools(mcp: FastMCP, client: OpenDartClient):

    @mcp.tool()
    async def get_major_stockholding(corp_code: str) -> str:
        """대량보유 상황보고 - 주식등의 대량보유상황보고서 내 대량보유 상황보고 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
        """
        data = await client.get("majorstock", {"corp_code": corp_code})
        return format_response(data)

    @mcp.tool()
    async def get_executive_stockholding(corp_code: str) -> str:
        """임원·주요주주 소유보고 - 임원·주요주주 특정증권등 소유상황보고서 내 소유보고 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
        """
        data = await client.get("elestock", {"corp_code": corp_code})
        return format_response(data)
