"""DS001: 공시정보 (Disclosure Information) - 4 tools"""

import base64

from mcp.server.fastmcp import FastMCP

from opendart_mcp.client import OpenDartClient, format_response


def register_tools(mcp: FastMCP, client: OpenDartClient):

    @mcp.tool()
    async def search_disclosure(
        corp_code: str = "",
        bgn_de: str = "",
        end_de: str = "",
        last_reprt_at: str = "N",
        pblntf_ty: str = "",
        pblntf_detail_ty: str = "",
        corp_cls: str = "",
        sort: str = "date",
        sort_mth: str = "desc",
        page_no: str = "1",
        page_count: str = "10",
    ) -> str:
        """공시검색 - 공시 유형별, 회사별, 날짜별 등 여러 조건으로 공시보고서를 검색합니다.

        Args:
            corp_code: 고유번호(8자리). 빈 값이면 전체 검색
            bgn_de: 시작일(YYYYMMDD). corp_code 없으면 최대 3개월
            end_de: 종료일(YYYYMMDD). 기본값: 당일
            last_reprt_at: 최종보고서만 검색 (Y/N)
            pblntf_ty: 공시유형 (A:정기공시, B:주요사항보고, C:발행공시, D:지분공시, E:기타공시, F:외부감사관련, G:펀드공시, H:자산유동화, I:거래소공시, J:공정위공시)
            pblntf_detail_ty: 공시상세유형
            corp_cls: 법인구분 (Y:유가, K:코스닥, N:코넥스, E:기타)
            sort: 정렬 (date:접수일자, crp:회사명, rpt:보고서명)
            sort_mth: 정렬방법 (asc/desc)
            page_no: 페이지번호
            page_count: 페이지당 건수 (최대 100)
        """
        params = {}
        if corp_code:
            params["corp_code"] = corp_code
        if bgn_de:
            params["bgn_de"] = bgn_de
        if end_de:
            params["end_de"] = end_de
        if last_reprt_at:
            params["last_reprt_at"] = last_reprt_at
        if pblntf_ty:
            params["pblntf_ty"] = pblntf_ty
        if pblntf_detail_ty:
            params["pblntf_detail_ty"] = pblntf_detail_ty
        if corp_cls:
            params["corp_cls"] = corp_cls
        params["sort"] = sort
        params["sort_mth"] = sort_mth
        params["page_no"] = page_no
        params["page_count"] = page_count
        data = await client.get("list", params)
        return format_response(data)

    @mcp.tool()
    async def get_company_info(corp_code: str) -> str:
        """기업개황 - DART에 등록된 기업의 개황정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
        """
        data = await client.get("company", {"corp_code": corp_code})
        return format_response(data)

    @mcp.tool()
    async def get_document(rcept_no: str) -> str:
        """공시서류원본파일 - 공시보고서 원본파일(ZIP)을 다운로드합니다. base64 인코딩된 ZIP 파일을 반환합니다.

        Args:
            rcept_no: 접수번호(14자리)
        """
        data = await client.get_binary("document", {"rcept_no": rcept_no})
        encoded = base64.b64encode(data).decode("ascii")
        return f'{{"status": "000", "message": "정상", "file_base64": "{encoded}", "file_size": {len(data)}}}'

    @mcp.tool()
    async def get_corp_code() -> str:
        """고유번호 - DART에 등록된 전체 기업의 고유번호, 회사명, 종목코드 등을 포함하는 ZIP 파일을 반환합니다. base64 인코딩됩니다."""
        data = await client.get_binary("corpCode", {})
        encoded = base64.b64encode(data).decode("ascii")
        return f'{{"status": "000", "message": "정상", "file_base64": "{encoded}", "file_size": {len(data)}}}'
