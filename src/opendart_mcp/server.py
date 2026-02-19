"""OpenDART MCP Server - 금융감독원 DART 전자공시시스템 Open API MCP 서버"""

import argparse
import os

from mcp.server.fastmcp import FastMCP

from opendart_mcp.client import OpenDartClient
from opendart_mcp.tools import (
    ds001_disclosure,
    ds002_periodic_report,
    ds003_financial,
    ds004_shareholding,
    ds005_major_report,
    ds006_securities_reg,
)


def create_server(api_key: str, host: str = "0.0.0.0", port: int = 8000) -> FastMCP:
    mcp = FastMCP(
        "OpenDART",
        instructions=(
            "OpenDART MCP 서버는 한국 금융감독원 DART(전자공시시스템)의 Open API를 제공합니다. "
            "공시검색, 기업개황, 정기보고서 주요정보, 재무정보, 지분공시, 주요사항보고서, "
            "증권신고서 등 총 83개의 API를 지원합니다. "
            "corp_code(고유번호)는 get_corp_code 또는 search_disclosure로 조회할 수 있습니다."
        ),
        host=host,
        port=port,
    )
    client = OpenDartClient(api_key)

    ds001_disclosure.register_tools(mcp, client)
    ds002_periodic_report.register_tools(mcp, client)
    ds003_financial.register_tools(mcp, client)
    ds004_shareholding.register_tools(mcp, client)
    ds005_major_report.register_tools(mcp, client)
    ds006_securities_reg.register_tools(mcp, client)

    return mcp


def main():
    api_key = os.environ.get("OPENDART_API_KEY")

    parser = argparse.ArgumentParser(description="OpenDART MCP Server")
    parser.add_argument(
        "--api-key",
        default=api_key,
        help="OpenDART API 인증키 (환경변수 OPENDART_API_KEY 또는 이 옵션으로 설정)",
    )
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse"],
        default=os.environ.get("MCP_TRANSPORT", "stdio"),
        help="전송 방식: stdio (로컬) 또는 sse (원격) (기본값: stdio)",
    )
    parser.add_argument(
        "--host",
        default=os.environ.get("HOST", "0.0.0.0"),
        help="SSE 모드 바인드 호스트 (기본값: 0.0.0.0)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("PORT", "8000")),
        help="SSE 모드 포트 (기본값: 8000)",
    )
    args = parser.parse_args()

    if not args.api_key:
        parser.error("OPENDART_API_KEY 환경변수 또는 --api-key 옵션이 필요합니다.")

    server = create_server(args.api_key, host=args.host, port=args.port)

    if args.transport == "sse":
        server.run(transport="sse")
    else:
        server.run()


if __name__ == "__main__":
    main()
