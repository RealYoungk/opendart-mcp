# OpenDART MCP Server

금융감독원 [DART 전자공시시스템](https://opendart.fss.or.kr) Open API를 [MCP(Model Context Protocol)](https://modelcontextprotocol.io) 서버로 제공합니다.

Claude, ChatGPT 등 MCP를 지원하는 AI 클라이언트에서 한국 상장기업의 공시정보, 재무제표, 지분공시 등 **83개 API**를 자연어로 조회할 수 있습니다.

## 사전 준비

[OpenDART](https://opendart.fss.or.kr)에서 API 인증키를 발급받으세요.

## 설치 및 설정

### Claude Desktop

`claude_desktop_config.json`에 추가:

```json
{
  "mcpServers": {
    "opendart": {
      "command": "uvx",
      "args": ["opendart-mcp"],
      "env": {
        "OPENDART_API_KEY": "<YOUR_API_KEY>"
      }
    }
  }
}
```

> 설정 파일 위치: macOS `~/Library/Application Support/Claude/claude_desktop_config.json`

### Claude Code

```bash
claude mcp add opendart -- uvx opendart-mcp

# API 키 설정
export OPENDART_API_KEY="<YOUR_API_KEY>"
```

### Cursor / Windsurf

MCP 설정 파일(`.cursor/mcp.json` 또는 `.windsurf/mcp.json`)에 추가:

```json
{
  "mcpServers": {
    "opendart": {
      "command": "uvx",
      "args": ["opendart-mcp"],
      "env": {
        "OPENDART_API_KEY": "<YOUR_API_KEY>"
      }
    }
  }
}
```

### SSE (원격 서버)

```bash
uvx opendart-mcp --transport sse --host 0.0.0.0 --port 8000
```

### Docker

```bash
docker build -t opendart-mcp .
docker run -e OPENDART_API_KEY="<YOUR_API_KEY>" -p 8000:8000 opendart-mcp
```

## 제공 도구 (83개)

### 공시정보 (4개)

| 도구 | 설명 |
|---|---|
| `search_disclosure` | 공시 검색 (기업코드, 날짜, 공시유형 등으로 필터링) |
| `get_company_info` | 기업 개황 조회 |
| `get_document` | 공시 원문 다운로드 (ZIP) |
| `get_corp_code` | 전체 고유번호 목록 다운로드 |

### 정기보고서 주요정보 (28개)

| 도구 | 설명 |
|---|---|
| `get_stock_issuance_status` | 증자(감자) 현황 |
| `get_dividend_info` | 배당에 관한 사항 |
| `get_treasury_stock_status` | 자기주식 취득 및 처분 현황 |
| `get_largest_shareholder` | 최대주주 현황 |
| `get_largest_shareholder_change` | 최대주주 변동 현황 |
| `get_minority_shareholder` | 소액주주 현황 |
| `get_executive_status` | 임원 현황 |
| `get_employee_status` | 직원 현황 |
| `get_individual_compensation` | 개인별 보수지급 금액 (5억 이상) |
| `get_total_compensation` | 이사·감사 전체의 보수현황 |
| `get_top5_compensation` | 개인별 보수지급 금액 (상위 5인) |
| `get_investment_in_others` | 타법인 출자 현황 |
| `get_total_shares_status` | 주식 총수 현황 |
| `get_debt_securities_issued` | 채무증권 발행실적 |
| `get_commercial_paper_balance` | 기업어음증권 미상환 잔액 |
| `get_short_term_bond_balance` | 단기사채 미상환 잔액 |
| `get_corporate_bond_balance` | 회사채 미상환 잔액 |
| `get_new_capital_securities_balance` | 신종자본증권 미상환 잔액 |
| `get_contingent_capital_balance` | 조건부자본증권 미상환 잔액 |
| `get_auditor_opinion` | 회계감사인의 감사의견 |
| `get_audit_service_contract` | 감사용역 체결현황 |
| `get_non_audit_service_contract` | 비감사용역 체결현황 |
| `get_outside_director_status` | 사외이사 및 그 변동현황 |
| `get_unregistered_exec_compensation` | 미등기임원 보수현황 |
| `get_total_compensation_approval` | 이사·감사의 보수한도 승인현황 |
| `get_compensation_by_type` | 유형별 보수지급 금액 |
| `get_public_offering_fund_usage` | 공모자금의 사용내역 |
| `get_private_placement_fund_usage` | 사모자금의 사용내역 |

### 재무정보 (7개)

| 도구 | 설명 |
|---|---|
| `get_single_company_accounts` | 단일회사 주요계정 |
| `get_multi_company_accounts` | 다중회사 주요계정 |
| `get_xbrl_document` | 재무제표 원본파일 (XBRL ZIP) |
| `get_full_financial_statement` | 단일회사 전체 재무제표 |
| `get_xbrl_taxonomy` | XBRL 택사노미 재무제표 양식 |
| `get_single_financial_index` | 단일회사 주요 재무지표 |
| `get_multi_financial_index` | 다중회사 주요 재무지표 |

### 지분공시 (2개)

| 도구 | 설명 |
|---|---|
| `get_major_stockholding` | 대량보유 상황보고 |
| `get_executive_stockholding` | 임원·주요주주 소유보고 |

### 주요사항보고서 (36개)

| 도구 | 설명 |
|---|---|
| `get_asset_transfer_putback` | 자산양수도(풋백옵션) |
| `get_default_occurrence` | 채무불이행(파산) |
| `get_business_suspension` | 영업정지 |
| `get_rehabilitation_filing` | 회생절차 개시신청 |
| `get_dissolution_event` | 해산사유 발생 |
| `get_paid_capital_increase` | 유상증자 결정 |
| `get_free_capital_increase` | 무상증자 결정 |
| `get_mixed_capital_increase` | 유무상증자 결정 |
| `get_capital_reduction` | 감자 결정 |
| `get_creditor_management_start` | 채권은행 관리절차 개시 |
| `get_lawsuit_filing` | 소송 등의 제기 |
| `get_overseas_listing_decision` | 해외 상장 결정 |
| `get_overseas_delisting_decision` | 해외 상장폐지 결정 |
| `get_overseas_listing` | 해외 상장 |
| `get_overseas_delisting` | 해외 상장폐지 |
| `get_convertible_bond_decision` | 전환사채권 발행결정 |
| `get_bond_with_warrant_decision` | 신주인수권부사채권 발행결정 |
| `get_exchangeable_bond_decision` | 교환사채권 발행결정 |
| `get_creditor_management_stop` | 채권은행 관리절차 중단 |
| `get_contingent_bond_decision` | 조건부자본증권 발행결정 |
| `get_treasury_stock_acquisition_decision` | 자기주식 취득 결정 |
| `get_treasury_stock_disposal_decision` | 자기주식 처분 결정 |
| `get_treasury_trust_contract_decision` | 자기주식취득 신탁계약 체결 결정 |
| `get_treasury_trust_termination_decision` | 자기주식취득 신탁계약 해지 결정 |
| `get_business_acquisition_decision` | 영업양수 결정 |
| `get_business_transfer_decision` | 영업양도 결정 |
| `get_tangible_asset_acquisition_decision` | 유형자산 양수 결정 |
| `get_tangible_asset_transfer_decision` | 유형자산 양도 결정 |
| `get_other_corp_stock_acquisition_decision` | 타법인 주식 양수 결정 |
| `get_other_corp_stock_transfer_decision` | 타법인 주식 양도 결정 |
| `get_stock_bond_acquisition_decision` | 주권 관련 사채권 양수 결정 |
| `get_stock_bond_transfer_decision` | 주권 관련 사채권 양도 결정 |
| `get_merger_decision` | 회사합병 결정 |
| `get_division_decision` | 회사분할 결정 |
| `get_division_merger_decision` | 회사분할합병 결정 |
| `get_stock_exchange_transfer_decision` | 주식교환·이전 결정 |

### 증권신고서 (6개)

| 도구 | 설명 |
|---|---|
| `get_equity_securities_reg` | 지분증권 |
| `get_debt_securities_reg` | 채무증권 |
| `get_depositary_receipts_reg` | 증권예탁증권 |
| `get_merger_reg` | 합병 |
| `get_stock_exchange_reg` | 주식의 포괄적 교환·이전 |
| `get_division_reg` | 분할 |

## 주요 파라미터

| 파라미터 | 설명 | 예시 |
|---|---|---|
| `corp_code` | 기업 고유번호 (8자리) | `00126380` (삼성전자) |
| `bsns_year` | 사업연도 | `2024` |
| `reprt_code` | 보고서 코드 | `11013` 1분기, `11012` 반기, `11014` 3분기, `11011` 사업보고서 |
| `bgn_de` / `end_de` | 조회 시작일 / 종료일 (YYYYMMDD) | `20240101` / `20241231` |
| `rcept_no` | 접수번호 (14자리) | `20240312000736` |

> `corp_code`를 모를 경우 `search_disclosure`로 기업명 검색하거나 `get_corp_code`로 전체 목록을 조회할 수 있습니다.

## 사용 예시

MCP 클라이언트(Claude 등)에서 자연어로 질문하면 됩니다:

- "삼성전자 2024년 사업보고서에서 배당 정보 알려줘"
- "네이버 최대주주 현황 조회해줘"
- "2024년 삼성전자 자기주식 취득 결정 내역 보여줘"
- "SK하이닉스 2024년 재무제표 주요계정 조회"
- "카카오 임원 현황이랑 보수 정보 알려줘"

## 라이선스

MIT
