# Failure Cluster Analysis — Phase A

**Sinh viên:** Đào Quốc Đại
**Mã học viên:** 2A202601285

**Ngày:** 26/08/2026

**Chế độ đánh giá:** Offline lexical proxy — không dùng API key

## 1. Aggregate Scores theo Distribution

| Metric | factual | multi_hop | adversarial |
|---|---:|---:|---:|
| faithfulness | 0.3500 | 0.3083 | 0.6000 |
| answer_relevancy | 0.0000 | 0.0000 | 0.0000 |
| context_precision | 0.4250 | 0.3167 | 0.4500 |
| context_recall | 0.4750 | 0.2958 | 0.2350 |
| **avg_score** | **0.3125** | **0.2302** | **0.3212** |

Đây là proxy lexical tất định: faithfulness đo tỷ lệ token câu trả lời được hỗ trợ bởi
context; relevancy dùng token F1 với câu hỏi và ground truth; precision đo tỷ lệ chunks
có liên quan; recall đo độ phủ ground-truth tokens trong context. Các giá trị này hữu ích
để so sánh tương đối offline nhưng không tương đương model-backed RAGAS.

## 2. Bottom 10 Questions

| Rank | Dist. | ID | Question | avg | worst metric |
|---:|---|---:|---|---:|---|
| 1 | factual | 3 | Phụ cấp ăn trưa hàng tháng là bao nhiêu?... | 0.0000 | faithfulness |
| 2 | factual | 4 | Mentor và buddy của nhân viên mới có thể là c... | 0.0000 | faithfulness |
| 3 | factual | 5 | Muốn mua thiết bị trị giá 55 triệu cần ai phê... | 0.0000 | faithfulness |
| 4 | factual | 6 | Thông tin lương thuộc cấp độ phân loại dữ liệ... | 0.0000 | faithfulness |
| 5 | factual | 12 | Thưởng Tết tối thiểu cho nhân viên chính thức... | 0.0000 | faithfulness |
| 6 | factual | 13 | Đánh giá hiệu suất diễn ra mấy lần một năm và... | 0.0000 | faithfulness |
| 7 | factual | 14 | Nhân viên nghỉ ốm cần nộp giấy tờ gì và trong... | 0.0000 | faithfulness |
| 8 | factual | 20 | Phụ cấp đi lại tối đa mỗi tháng là bao nhiêu ... | 0.0000 | faithfulness |
| 9 | multi_hop | 21 | Một nhân viên Senior có 9 năm thâm niên được ... | 0.0000 | faithfulness |
| 10 | multi_hop | 22 | Nếu cần mua một chiếc laptop 30 triệu cho nhâ... | 0.0000 | faithfulness |

## 3. Failure Cluster Matrix

| worst_metric | factual | multi_hop | adversarial | Total |
|---|---:|---:|---:|---:|
| faithfulness | 13 | 13 | 4 | 30 |
| answer_relevancy | 7 | 7 | 6 | 20 |
| context_precision | 0 | 0 | 0 | 0 |
| context_recall | 0 | 0 | 0 | 0 |

## 4. Dominant Failure Analysis

**Dominant distribution:** factual (do average score 0.3125).
chất lượng phù hợp hơn là adversarial vì có average thấp nhất (`0.7220`).

**Dominant metric:** faithfulness.

Factual có raw count cao vì có 20 mẫu và relevancy thường là metric nhỏ nhất ngay cả
khi tổng điểm cao. Xét mức điểm thay vì count, adversarial mới là cụm khó nhất, tiếp đến
multi-hop. Các câu version conflict và negation có lexical mismatch lớn giữa câu hỏi,
context và câu trả lời, đồng thời retrieval phải phân biệt tài liệu cũ/hiện hành.

## 5. Suggested Fixes

| Metric yếu | Root cause | Suggested fix |
|---|---|---|
| answer_relevancy | 0.0000 | 0.0000 | 0.0000 |
| context_recall | 0.4750 | 0.2958 | 0.2350 |
| context_precision | 0.4250 | 0.3167 | 0.4500 |
| faithfulness | 0.3500 | 0.3083 | 0.6000 |

## 6. Nhận xét về Adversarial Distribution

Adversarial có average `0.7220`, thấp hơn multi-hop `0.7884` và factual `0.8976`, đúng
kỳ vọng stress-test. Bảy trong bottom-10 là adversarial, tập trung vào phép năm, mật khẩu,
bảo hiểm thử việc và VPN cá nhân. Điều này cho thấy version conflict/negation là điểm yếu
rõ nhất; nên bổ sung metadata phiên bản và rule ưu tiên policy đang có hiệu lực.
