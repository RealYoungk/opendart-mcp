"""DS005: 주요사항보고서 주요정보 (Major Report Key Information) - 36 tools"""

from mcp.server.fastmcp import FastMCP

from opendart_mcp.client import OpenDartClient, format_response


def register_tools(mcp: FastMCP, client: OpenDartClient):

    @mcp.tool()
    async def get_asset_transfer_putback(corp_code: str, bgn_de: str, end_de: str) -> str:
        """자산양수도(기타), 풋백옵션 - 주요사항보고서 내 자산양수도 및 풋백옵션 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("astInhtrfEtcPtbkOpt", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_default_occurrence(corp_code: str, bgn_de: str, end_de: str) -> str:
        """부도발생 - 주요사항보고서 내 부도발생 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("dfOcr", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_business_suspension(corp_code: str, bgn_de: str, end_de: str) -> str:
        """영업정지 - 주요사항보고서 내 영업정지 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("bsnSp", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_rehabilitation_filing(corp_code: str, bgn_de: str, end_de: str) -> str:
        """회생절차 개시신청 - 주요사항보고서 내 회생절차 개시신청 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("ctrcvsBgrq", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_dissolution_event(corp_code: str, bgn_de: str, end_de: str) -> str:
        """해산사유 발생 - 주요사항보고서 내 해산사유 발생 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("dsRsOcr", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_paid_capital_increase(corp_code: str, bgn_de: str, end_de: str) -> str:
        """유상증자 결정 - 주요사항보고서 내 유상증자 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("piicDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_free_capital_increase(corp_code: str, bgn_de: str, end_de: str) -> str:
        """무상증자 결정 - 주요사항보고서 내 무상증자 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("fricDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_mixed_capital_increase(corp_code: str, bgn_de: str, end_de: str) -> str:
        """유무상증자 결정 - 주요사항보고서 내 유무상증자 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("pifricDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_capital_reduction(corp_code: str, bgn_de: str, end_de: str) -> str:
        """감자 결정 - 주요사항보고서 내 감자 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("crDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_creditor_management_start(corp_code: str, bgn_de: str, end_de: str) -> str:
        """채권은행 등의 관리절차 개시 - 주요사항보고서 내 채권은행 등의 관리절차 개시 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("bnkMngtPcbg", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_lawsuit_filing(corp_code: str, bgn_de: str, end_de: str) -> str:
        """소송 등의 제기 - 주요사항보고서 내 소송 등의 제기 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("lwstLg", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_overseas_listing_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """해외 증권시장 주권등 상장 결정 - 주요사항보고서 내 해외 증권시장 주권등 상장 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("ovLstDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_overseas_delisting_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """해외 증권시장 주권등 상장폐지 결정 - 주요사항보고서 내 해외 증권시장 주권등 상장폐지 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("ovDlstDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_overseas_listing(corp_code: str, bgn_de: str, end_de: str) -> str:
        """해외 증권시장 주권등 상장 - 주요사항보고서 내 해외 증권시장 주권등 상장 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("ovLst", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_overseas_delisting(corp_code: str, bgn_de: str, end_de: str) -> str:
        """해외 증권시장 주권등 상장폐지 - 주요사항보고서 내 해외 증권시장 주권등 상장폐지 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("ovDlst", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_convertible_bond_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """전환사채권 발행결정 - 주요사항보고서 내 전환사채권 발행결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("cvbdIsDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_bond_with_warrant_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """신주인수권부사채권 발행결정 - 주요사항보고서 내 신주인수권부사채권 발행결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("bdwtIsDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_exchangeable_bond_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """교환사채권 발행결정 - 주요사항보고서 내 교환사채권 발행결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("exbdIsDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_creditor_management_stop(corp_code: str, bgn_de: str, end_de: str) -> str:
        """채권은행 등의 관리절차 중단 - 주요사항보고서 내 채권은행 등의 관리절차 중단 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("bnkMngtPcsp", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_contingent_bond_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """상각형 조건부자본증권 발행결정 - 주요사항보고서 내 상각형 조건부자본증권 발행결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("wdCocobdIsDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_treasury_stock_acquisition_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """자기주식 취득 결정 - 주요사항보고서 내 자기주식 취득 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("tsstkAqDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_treasury_stock_disposal_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """자기주식 처분 결정 - 주요사항보고서 내 자기주식 처분 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("tsstkDpDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_treasury_trust_contract_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """자기주식취득 신탁계약 체결 결정 - 주요사항보고서 내 자기주식취득 신탁계약 체결 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("tsstkAqTrctrCnsDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_treasury_trust_termination_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """자기주식취득 신탁계약 해지 결정 - 주요사항보고서 내 자기주식취득 신탁계약 해지 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("tsstkAqTrctrCcDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_business_acquisition_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """영업양수 결정 - 주요사항보고서 내 영업양수 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("bsnInhDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_business_transfer_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """영업양도 결정 - 주요사항보고서 내 영업양도 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("bsnTrfDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_tangible_asset_acquisition_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """유형자산 양수 결정 - 주요사항보고서 내 유형자산 양수 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("tgastInhDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_tangible_asset_transfer_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """유형자산 양도 결정 - 주요사항보고서 내 유형자산 양도 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("tgastTrfDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_other_corp_stock_acquisition_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """타법인 주식 및 출자증권 양수결정 - 주요사항보고서 내 타법인 주식 및 출자증권 양수결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("otcprStkInvscrInhDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_other_corp_stock_transfer_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """타법인 주식 및 출자증권 양도결정 - 주요사항보고서 내 타법인 주식 및 출자증권 양도결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("otcprStkInvscrTrfDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_stock_bond_acquisition_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """주권 관련 사채권 양수 결정 - 주요사항보고서 내 주권 관련 사채권 양수 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("stkrtbdInhDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_stock_bond_transfer_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """주권 관련 사채권 양도 결정 - 주요사항보고서 내 주권 관련 사채권 양도 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("stkrtbdTrfDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_merger_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """회사합병 결정 - 주요사항보고서 내 회사합병 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("cmpMgDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_division_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """회사분할 결정 - 주요사항보고서 내 회사분할 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("cmpDvDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_division_merger_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """회사분할합병 결정 - 주요사항보고서 내 회사분할합병 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("cmpDvmgDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)

    @mcp.tool()
    async def get_stock_exchange_transfer_decision(corp_code: str, bgn_de: str, end_de: str) -> str:
        """주식교환·이전 결정 - 주요사항보고서 내 주식교환·이전 결정 정보를 제공합니다.

        Args:
            corp_code: 고유번호(8자리)
            bgn_de: 시작일(YYYYMMDD, 2015년 이후)
            end_de: 종료일(YYYYMMDD, 2015년 이후)
        """
        data = await client.get("stkExtrDecsn", {"corp_code": corp_code, "bgn_de": bgn_de, "end_de": end_de})
        return format_response(data)
