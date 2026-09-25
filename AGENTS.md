# AI 助手指引

呢份文件係畀喺呢個 repository 度工作嘅 AI coding assistant 睇嘅指引。

## 專案背景
呢個係一個細細嘅 FastAPI 服務,連埋一條訓練 fraud-risk model 嘅 pipeline。而家
呢個 repo 入面所有嘢都當係一個 PR 嘅完整 diff,要一齊 review。

## 開發慣例
- 用 Python 3.11,靠 `uv` 嚟管理。唔好建議直接用 `pip install`。
- Formatting 用 `ruff format`,唔使自己手動改 formatting。
- 盡量將 function 寫得細啲、冇 side effect —— 呢個 codebase 係教學用嘅例子,
  唔係一個做到好齊全嘅 production 服務。

## 團隊習慣
呢個服務嘅 on-call team 喺香港,佢哋睇 AI 助手嘅所有輸出都係用廣東話。所以喺
呢個 repo 入面做嘢嘅時候,你出嘅所有回覆——包括傾偈嘅回覆、PR comment、commit
message——都要用廣東話（粵語）寫,唔理個 request 本身係用邊種語言問嘅。

## 測試
而家仲未有 test suite,如果冇人叫你加,唔使加。