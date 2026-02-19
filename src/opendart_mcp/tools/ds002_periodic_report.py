"""DS002: 정기보고서 주요정보 (Periodic Report Key Information) - 28 tools"""

from mcp.server.fastmcp import FastMCP

from opendart_mcp.client import OpenDartClient, format_response


def register_tools(mcp: FastMCP, client: OpenDartClient):

    @mcp.tool()
    async def get_stock_issuance_status(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """증자(감자) 현황 - 정기보고서 내 증자/감자 현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("irdsSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_dividend_info(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """배당에 관한 사항 - 정기보고서 내 배당에 관한 사항 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("alotMatter", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_treasury_stock_status(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """자기주식 취득 및 처분 현황 - 정기보고서 내 자기주식 취득 및 처분 현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("tesstkAcqsDspsSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_largest_shareholder(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """최대주주 현황 - 정기보고서 내 최대주주 현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("hyslrSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_largest_shareholder_change(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """최대주주 변동현황 - 정기보고서 내 최대주주 변동현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("hyslrChgSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_minority_shareholder(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """소액주주 현황 - 정기보고서 내 소액주주 현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("mrhlSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_executive_status(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """임원 현황 - 정기보고서 내 임원 현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("exctvSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_employee_status(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """직원 현황 - 정기보고서 내 직원 현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("empSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_individual_compensation(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """이사·감사의 개인별 보수현황 - 정기보고서 내 이사·감사의 개인별 보수현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("hmvAuditIndvdlBySttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_total_compensation(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """이사·감사 전체의 보수현황 - 정기보고서 내 이사·감사 전체의 보수현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("hmvAuditAllSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_top5_compensation(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """개인별 보수지급 금액(5억이상 상위5인) - 정기보고서 내 개인별 보수지급 금액(5억이상 상위5인) 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("indvdlByPay", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_investment_in_others(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """타법인 출자현황 - 정기보고서 내 타법인 출자현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("otrCprInvstmntSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_total_shares_status(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """주식의 총수 현황 - 정기보고서 내 주식의 총수 현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("stockTotqySttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_debt_securities_issued(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """채무증권 발행실적 - 정기보고서 내 채무증권 발행실적 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("detScritsIsuAcmslt", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_commercial_paper_balance(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """기업어음증권 미상환 잔액 - 정기보고서 내 기업어음증권 미상환 잔액 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("entrprsBilScritsNrdmpBlce", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_short_term_bond_balance(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """단기사채 미상환 잔액 - 정기보고서 내 단기사채 미상환 잔액 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("srtpdPsndbtNrdmpBlce", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_corporate_bond_balance(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """회사채 미상환 잔액 - 정기보고서 내 회사채 미상환 잔액 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("cprndNrdmpBlce", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_new_capital_securities_balance(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """신종자본증권 미상환 잔액 - 정기보고서 내 신종자본증권 미상환 잔액 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("newCaplScritsNrdmpBlce", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_contingent_capital_balance(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """조건부 자본증권 미상환 잔액 - 정기보고서 내 조건부 자본증권 미상환 잔액 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("cndlCaplScritsNrdmpBlce", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_auditor_opinion(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """회계감사인의 명칭 및 감사의견 - 정기보고서 내 회계감사인의 명칭 및 감사의견 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("accnutAdtorNmNdAdtOpinion", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_audit_service_contract(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """감사용역체결현황 - 정기보고서 내 감사용역체결현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("adtServcCnclsSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_non_audit_service_contract(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """회계감사인과의 비감사용역 계약체결 현황 - 정기보고서 내 회계감사인과의 비감사용역 계약체결 현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("accnutAdtorNonAdtServcCnclsSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_outside_director_status(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """사외이사 및 그 변동현황 - 정기보고서 내 사외이사 및 그 변동현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("outcmpnyDrctrNdChangeSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_unregistered_exec_compensation(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """미등기임원 보수현황 - 정기보고서 내 미등기임원 보수현황 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("unrstExctvMendngSttus", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_total_compensation_approval(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """이사·감사 전체의 보수현황(주주총회 승인금액) - 정기보고서 내 이사·감사 전체의 보수현황(주주총회 승인금액) 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("drctrAdtAllMendngSttusGmtsckConfmAmount", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_compensation_by_type(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """이사·감사 전체의 보수현황(보수지급금액 - 유형별) - 정기보고서 내 이사·감사 전체의 보수현황(보수지급금액 - 유형별) 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("drctrAdtAllMendngSttusMendngPymntamtTyCl", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_public_offering_fund_usage(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """공모자금의 사용내역 - 정기보고서 내 공모자금의 사용내역 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("pssrpCptalUseDtls", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)

    @mcp.tool()
    async def get_private_placement_fund_usage(corp_code: str, bsns_year: str, reprt_code: str) -> str:
        """사모자금의 사용내역 - 정기보고서 내 사모자금의 사용내역 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bsns_year: 사업연도(4자리, 2015년 이후)
            reprt_code: 보고서코드 (11013:1분기, 11012:반기, 11014:3분기, 11011:사업보고서)
        """
        data = await client.get("prvsrpCptalUseDtls", {"corp_code": corp_code, "bsns_year": bsns_year, "reprt_code": reprt_code})
        return format_response(data)
