"""DS003: 정기보고서 재무정보 (Financial Information from Periodic Reports) - 7 tools"""

import base64

from mcp.server.fastmcp import FastMCP

from opendart_mcp.client import OpenDartClient, format_response


def register_tools(mcp: FastMCP, client: OpenDartClient):

    @mcp.tool()
    async def get_single_company_accounts(
        corp_code: str, bsns_year: str, reprt_code: str
    ) -> str:
        """단일회사 주요계정 - 단일회사의 XBRL 재무제표에서 주요계정을 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get(
            "fnlttSinglAcnt",
            {
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return format_response(data)

    @mcp.tool()
    async def get_multi_company_accounts(
        corp_code: str, bsns_year: str, reprt_code: str
    ) -> str:
        """다중회사 주요계정 - 여러 회사의 주요계정을 일괄 조회합니다. corp_code는 쉼표(,)로 구분하여 최대 100개까지 입력 가능합니다.

        Args:
            corp_code: 고유번호(8자리, 쉼표 구분 최대 100개)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get(
            "fnlttMultiAcnt",
            {
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return format_response(data)

    @mcp.tool()
    async def get_xbrl_document(rcept_no: str, reprt_code: str) -> str:
        """재무제표 원본파일(XBRL) - XBRL 재무제표 원본파일(ZIP)을 다운로드합니다. base64 인코딩된 ZIP 파일을 반환합니다.

        Args:
            rcept_no: 접수번호(14자리)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get_binary(
            "fnlttXbrl", {"rcept_no": rcept_no, "reprt_code": reprt_code}
        )
        encoded = base64.b64encode(data).decode("ascii")
        return f'{{"status": "000", "message": "정상", "file_base64": "{encoded}", "file_size": {len(data)}}}'

    @mcp.tool()
    async def get_full_financial_statement(
        corp_code: str, bsns_year: str, reprt_code: str, fs_div: str
    ) -> str:
        """단일회사 전체 재무제표 - 단일회사의 전체 재무제표를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
            fs_div: 개별/연결구분 (OFS:재무제표, CFS:연결재무제표)
        """
        data = await client.get(
            "fnlttSinglAcntAll",
            {
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
                "fs_div": fs_div,
            },
        )
        return format_response(data)

    @mcp.tool()
    async def get_xbrl_taxonomy(sj_div: str) -> str:
        """XBRL택사노미재무제표양식 - IFRS 기반 XBRL 표준계정과목체계(택사노미)를 제공합니다.

        Args:
            sj_div: 재무제표구분 (BS:재무상태표, IS:손익계산서, CIS:포괄손익계산서, CF:현금흐름표, SCE:자본변동표)
        """
        data = await client.get("xbrlTaxonomy", {"sj_div": sj_div})
        return format_response(data)

    @mcp.tool()
    async def get_single_financial_index(
        corp_code: str, bsns_year: str, reprt_code: str, idx_cl_code: str
    ) -> str:
        """단일회사 주요 재무지표 - 단일회사의 주요 재무지표를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
            idx_cl_code: 지표분류코드 (M210000:수익성지표, M220000:안정성지표, M230000:성장성지표, M240000:활동성지표)
        """
        data = await client.get(
            "fnlttSinglIndx",
            {
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
                "idx_cl_code": idx_cl_code,
            },
        )
        return format_response(data)

    @mcp.tool()
    async def get_multi_financial_index(
        corp_code: str, bsns_year: str, reprt_code: str, idx_cl_code: str
    ) -> str:
        """다중회사 주요 재무지표 - 여러 회사의 주요 재무지표를 일괄 조회합니다. corp_code는 쉼표(,)로 구분합니다.

        Args:
            corp_code: 고유번호(8자리, 쉼표 구분)
            bsns_year: 사업연도(4자리)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
            idx_cl_code: 지표분류코드 (M210000:수익성지표, M220000:안정성지표, M230000:성장성지표, M240000:활동성지표)
        """
        data = await client.get(
            "fnlttCmpnyIndx",
            {
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
                "idx_cl_code": idx_cl_code,
            },
        )
        return format_response(data)
