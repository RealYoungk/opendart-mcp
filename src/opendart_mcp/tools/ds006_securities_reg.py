"""DS006: 증권신고서 주요정보 (Securities Registration Statement Key Information) - 6 tools"""

from mcp.server.fastmcp import FastMCP

from opendart_mcp.client import OpenDartClient, format_response


def register_tools(mcp: FastMCP, client: OpenDartClient):

    @mcp.tool()
    async def get_equity_securities_reg(
        corp_code: str, bgn_de: str, end_de: str
    ) -> str:
        """지분증권 - 증권신고서 내 지분증권 요약정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD)
            end_de: 종료일(YYYYMMDD)
        """
        data = await client.get(
            "estkRs",
            {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de},
        )
        return format_response(data)

    @mcp.tool()
    async def get_debt_securities_reg(
        corp_code: str, bgn_de: str, end_de: str
    ) -> str:
        """채무증권 - 증권신고서 내 채무증권 요약정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD)
            end_de: 종료일(YYYYMMDD)
        """
        data = await client.get(
            "bdRs",
            {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de},
        )
        return format_response(data)

    @mcp.tool()
    async def get_depositary_receipts_reg(
        corp_code: str, bgn_de: str, end_de: str
    ) -> str:
        """증권예탁증권 - 증권신고서 내 증권예탁증권 요약정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD)
            end_de: 종료일(YYYYMMDD)
        """
        data = await client.get(
            "stkdpRs",
            {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de},
        )
        return format_response(data)

    @mcp.tool()
    async def get_merger_reg(corp_code: str, bgn_de: str, end_de: str) -> str:
        """합병 - 증권신고서 내 합병 요약정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD)
            end_de: 종료일(YYYYMMDD)
        """
        data = await client.get(
            "mgRs",
            {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de},
        )
        return format_response(data)

    @mcp.tool()
    async def get_stock_exchange_reg(
        corp_code: str, bgn_de: str, end_de: str
    ) -> str:
        """주식의포괄적교환·이전 - 증권신고서 내 주식의 포괄적 교환·이전 요약정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD)
            end_de: 종료일(YYYYMMDD)
        """
        data = await client.get(
            "extrRs",
            {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de},
        )
        return format_response(data)

    @mcp.tool()
    async def get_division_reg(
        corp_code: str, bgn_de: str, end_de: str
    ) -> str:
        """분할 - 증권신고서 내 분할 요약정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD)
            end_de: 종료일(YYYYMMDD)
        """
        data = await client.get(
            "dvRs",
            {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de},
        )
        return format_response(data)
