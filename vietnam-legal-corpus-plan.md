# Plan: Vietnam Legal Reference Corpus (Hướng B)
### Cho bộ `lpa-vietnam-legal-skills` — Lưu Phát Anh

**Trạng thái:** Draft v1
**Chủ sở hữu:** [điền tên người chịu trách nhiệm]
**Ngày tạo:** 2026-09-11
**Review lại kế hoạch này vào:** [90 ngày sau ngày apply]

---

## 0. Mục tiêu

Bổ sung một **local reference corpus** — tập hợp văn bản luật Việt Nam liên quan trực tiếp đến hoạt động B2B của công ty (bán buôn đá tinh khiết, giao nhận, thanh toán, dữ liệu khách hàng) — để agent (Claude Code / ZCode) có thể tra cứu nhanh, chính xác, mà không phải web-search lại từ đầu mỗi lần, đồng thời **không phá vỡ nguyên tắc chống bịa citation** đã có trong `evidence-policy.md`.

### Không thuộc phạm vi plan này

- Không build RAG backend / vector DB (đó là Hướng C, dự án riêng).
- Không crawl toàn bộ 40.000+ văn bản luật VN.
- Không thay thế vai trò luật sư cho các vấn đề CRITICAL/HIGH.

### Nguyên tắc bất biến (không được vi phạm khi thực hiện)

1. Corpus là **Tier 1 cache**, không phải nguồn thay thế Tier 1 thật (`vbpl.vn`, cổng thông tin Quốc hội/Chính phủ). Mọi văn bản trong corpus phải trỏ về được bản gốc.
2. Mỗi file phải có `last_checked_date`. File quá hạn review **không được dùng để khẳng định luật hiện hành** — agent phải cảnh báo và search lại.
3. Không paraphrase/rút gọn điều luật theo cách làm mất nghĩa pháp lý. Trích dẫn phải nguyên văn số điều/khoản, không tự diễn giải thành "tinh thần chung".
4. Agent luôn ưu tiên corpus để **định hướng nhanh** (biết cần tra điều mấy), nhưng với hợp đồng giá trị cao hoặc rủi ro CRITICAL/HIGH, **vẫn phải verify lại qua vbpl.vn** trước khi đưa vào draft cuối.

---

## 1. Phạm vi văn bản luật (danh sách lõi)

Chỉ đưa vào corpus những văn bản **thực sự dùng lặp lại** trong nghiệp vụ LPA. Ưu tiên theo 3 nhóm:

### Nhóm 1 — Bắt buộc, dùng gần như mọi hợp đồng (làm trước)

| # | Văn bản | Lý do cần | Ghi chú xác minh |
|---|---|---|---|
| 1 | Bộ luật Dân sự 2015 | Nghĩa vụ hợp đồng, bồi thường thiệt hại, lãi chậm trả, force majeure | Lấy bản hợp nhất mới nhất trên vbpl.vn |
| 2 | Luật Thương mại 2005 (+ văn bản sửa đổi nếu có) | Phạt vi phạm HĐ thương mại, mua bán hàng hóa | **Cần xác minh số hiệu sửa đổi gần nhất trước khi tải** |
| 3 | Luật Doanh nghiệp 2020 | Thẩm quyền ký kết, đại diện pháp luật | Kiểm tra có Luật DN sửa đổi mới hơn không |
| 4 | Luật An toàn thực phẩm (hiện hành) | LPA bán sản phẩm thực phẩm (đá tinh khiết) | Kiểm tra số hiệu + văn bản hướng dẫn thi hành hiện hành |
| 5 | Luật Bảo vệ quyền lợi người tiêu dùng 2023 | Nếu có giao dịch với khách hàng cá nhân/hộ kinh doanh nhỏ | |
| 6 | Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 + Nghị định 356/2025/NĐ-CP | Thu thập SĐT/địa chỉ giao hàng qua Zalo/portal | Có hiệu lực từ 1/1/2026 — **văn bản mới, ưu tiên xác minh kỹ** |

### Nhóm 2 — Quan trọng, dùng thường xuyên (làm sau nhóm 1)

| # | Văn bản | Lý do |
|---|---|---|
| 7 | Luật Quản lý thuế (hiện hành) + quy định hóa đơn điện tử | Invoice, VAT |
| 8 | Luật Kế toán (hiện hành) | Chứng từ, hóa đơn, sổ sách liên quan thanh toán |
| 9 | Bộ luật Tố tụng Dân sự 2015 (phần liên quan thẩm quyền tòa án/trọng tài) | Điều khoản giải quyết tranh chấp |
| 10 | Luật Trọng tài Thương mại 2010 | Nếu hợp đồng chọn trọng tài |

### Nhóm 3 — Dự phòng, thêm khi có nhu cầu thực tế

- Luật Cạnh tranh (nếu có điều khoản độc quyền/exclusivity)
- Luật Sở hữu trí tuệ (nếu có nhãn hiệu/bao bì cần bảo hộ)
- Văn bản địa phương về an toàn thực phẩm/giấy phép kinh doanh tại địa bàn LPA hoạt động

> **Quy tắc mở rộng danh sách:** chỉ thêm văn bản mới vào corpus khi đã có ≥2 lần thực tế cần tra cứu văn bản đó trong công việc thật. Tránh phình to corpus với luật ít dùng — khó bảo trì và dễ lỗi thời không ai phát hiện.

---

## 2. Kiến trúc thư mục

```text
lpa-vietnam-legal-skills/
└── references/
    └── laws/
        ├── _INDEX.md                          # mục lục + trạng thái từng văn bản
        ├── bo-luat-dan-su-2015.md
        ├── luat-thuong-mai-2005.md
        ├── luat-doanh-nghiep-2020.md
        ├── luat-an-toan-thuc-pham.md
        ├── luat-bao-ve-quyen-loi-nguoi-tieu-dung-2023.md
        ├── luat-bao-ve-du-lieu-ca-nhan-2025.md
        ├── nghi-dinh-356-2025.md
        ├── luat-quan-ly-thue.md
        ├── luat-ke-toan.md
        └── ... (nhóm 2, 3 thêm sau)
```

Mỗi file luật KHÔNG chứa toàn văn bản dài (tốn context, khó bảo trì). Thay vào đó dùng **định dạng trích yếu có cấu trúc** — xem Mục 3.

---

## 3. Chuẩn định dạng 1 file luật (schema bắt buộc)

Mỗi file trong `references/laws/` phải theo đúng khung sau:

```markdown
---
document_title: "Bộ luật Dân sự"
document_number: "91/2015/QH13"
document_type: "Bộ luật"
issuing_body: "Quốc hội"
issued_date: "2015-11-24"
effective_date: "2017-01-01"
status: "Còn hiệu lực"                # hoặc "Hết hiệu lực một phần", "Đã sửa đổi bởi ..."
consolidated_version_url: "https://vbpl.vn/..."
last_checked_date: "2026-09-11"
next_review_due: "2026-12-11"          # +90 ngày
checked_by: "[tên người xác minh]"
relevance_tags: ["hop-dong", "boi-thuong-thiet-hai", "lai-cham-tra"]
---

# Bộ luật Dân sự 2015 — Trích yếu dùng cho hợp đồng B2B LPA

## Phạm vi áp dụng trong trích yếu này
Chỉ trích các điều khoản liên quan đến: nghĩa vụ hợp đồng, vi phạm nghĩa vụ,
bồi thường thiệt hại, lãi suất chậm thực hiện nghĩa vụ trả tiền, sự kiện bất khả kháng.
KHÔNG phải toàn văn Bộ luật.

## Điều [số] — [Tên điều]
> [Trích nguyên văn khoản/điều liên quan — copy chính xác, không diễn giải]

**Áp dụng cho:** [tình huống nghiệp vụ cụ thể, ví dụ: tính lãi chậm thanh toán]
**Lưu ý:** [ví dụ: cần đối chiếu văn bản hướng dẫn thi hành nếu có]

## Điều [số] — [Tên điều]
...

## Văn bản liên quan cần biết
- [Nghị định/Thông tư hướng dẫn thi hành, nếu có, kèm số hiệu]

## Lịch sử sửa đổi đã ghi nhận
- [ngày] — [nội dung sửa đổi nếu có, hoặc "Chưa ghi nhận sửa đổi tại lần kiểm tra gần nhất"]
```

**Quy tắc bắt buộc khi soạn file:**
- Chỉ trích các điều thực sự dùng — không copy nguyên toàn bộ luật.
- Mọi đoạn trích phải nguyên văn (đúng số điều/khoản/điểm), không viết lại bằng lời của agent.
- Nếu không chắc bản đang có là bản hợp nhất mới nhất → để trạng thái `status: "CẦN XÁC MINH"` thay vì đoán.

---

## 4. `_INDEX.md` — mục lục kiểm soát

File này là nơi duy nhất agent cần đọc trước để biết "có gì trong corpus, cái nào còn tin được":

```markdown
| Văn bản | File | Status | Last checked | Next review | Rủi ro nếu lỗi thời |
|---|---|---|---|---|---|
| Bộ luật Dân sự 2015 | bo-luat-dan-su-2015.md | Còn hiệu lực | 2026-09-11 | 2026-12-11 | Trung bình |
| Luật BVDLCN 2025 | luat-bao-ve-du-lieu-ca-nhan-2025.md | Còn hiệu lực (mới) | 2026-09-11 | 2026-10-11 | Cao — luật mới, hướng dẫn thi hành có thể còn thay đổi |
```

Văn bản mới có hiệu lực (như Luật BVDLCN 2025) nên có `next_review` ngắn hơn (30 ngày) so với luật đã ổn định lâu năm (90 ngày).

---

## 5. Quy trình thực hiện (theo giai đoạn)

### Giai đoạn 1 — Khung + 2 văn bản thử nghiệm (Tuần 1)
- [ ] Tạo cấu trúc thư mục `references/laws/` + `_INDEX.md`
- [ ] Soạn file mẫu cho **Bộ luật Dân sự 2015** và **Luật Thương mại 2005** theo đúng schema Mục 3
- [ ] Review chéo: người thứ 2 (không phải người soạn) kiểm tra từng trích dẫn đối chiếu bản gốc trên vbpl.vn
- [ ] Chốt schema cuối cùng nếu có điều chỉnh sau khi làm thử

**Tiêu chí hoàn thành giai đoạn 1:** 2 file mẫu, 100% trích dẫn đối chiếu đúng bản gốc, có sign-off của người review.

### Giai đoạn 2 — Hoàn thành Nhóm 1 (Tuần 2-3)
- [ ] Soạn 4 văn bản còn lại của Nhóm 1 (Luật DN, ATTP, BVQLNTD, BVDLCN+NĐ356)
- [ ] Đặc biệt với Luật BVDLCN 2025/NĐ 356/2025: xác minh kỹ vì luật mới, search thêm văn bản hướng dẫn thi hành nếu đã ban hành
- [ ] Cập nhật `_INDEX.md`

### Giai đoạn 3 — Kết nối vào skill (Tuần 3-4)
- [ ] Sửa `skills/legal-research/SKILL.md`: thêm bước "Đọc `references/laws/_INDEX.md` trước khi web-search" vào đầu quy trình
- [ ] Sửa `skills/contract-drafting/SKILL.md` và `skills/contract-review/SKILL.md`: trỏ rõ ràng "dùng corpus cho định hướng, verify qua vbpl.vn cho draft cuối"
- [ ] Test bằng 3-5 câu hỏi/thao tác thật (ví dụ: "mức phạt vi phạm tối đa cho hợp đồng mua bán là bao nhiêu?", "soạn điều khoản force majeure") — kiểm tra agent có dùng corpus đúng cách không

### Giai đoạn 4 — Nhóm 2 + vận hành định kỳ (Tuần 5 trở đi, liên tục)
- [ ] Soạn 4 văn bản Nhóm 2
- [ ] Thiết lập lịch review định kỳ (xem Mục 6)
- [ ] Nhóm 3: chỉ thêm khi có nhu cầu thực tế phát sinh (không làm trước)

---

## 6. Vận hành & bảo trì (sau khi go-live)

### Lịch review định kỳ

| Loại văn bản | Tần suất review |
|---|---|
| Luật mới ban hành/mới hiệu lực (<12 tháng) | 30 ngày/lần |
| Luật ổn định lâu năm | 90 ngày/lần |
| Bất kỳ lúc nào có tin luật sửa đổi liên quan (theo dõi qua báo pháp lý/thuvienphapluat.vn) | Ngay lập tức, không chờ lịch |

### Quy trình review 1 văn bản

1. Mở `consolidated_version_url` trong frontmatter, kiểm tra mục "Tình trạng hiệu lực" trên vbpl.vn.
2. Nếu không đổi → cập nhật `last_checked_date`, `next_review_due`.
3. Nếu có sửa đổi → cập nhật nội dung trích yếu, ghi vào "Lịch sử sửa đổi đã ghi nhận", thông báo cho người dùng skill (nếu có hợp đồng đang soạn dùng điều khoản bị ảnh hưởng).
4. Cập nhật `_INDEX.md`.

### Trách nhiệm (điền theo thực tế công ty)

| Vai trò | Trách nhiệm |
|---|---|
| Người phụ trách corpus | Chủ trì review định kỳ, cập nhật file |
| Người review chéo | Kiểm tra tính chính xác trước khi merge thay đổi |
| Người dùng skill (sales/ops) | Báo cáo khi thấy nghi ngờ nội dung sai/cũ |
| Luật sư ngoài (nếu có) | Xác nhận cuối cho hợp đồng CRITICAL/HIGH, không cần review corpus thường xuyên |

---

## 7. Rủi ro & biện pháp giảm thiểu

| Rủi ro | Mức độ | Biện pháp |
|---|---|---|
| Corpus lỗi thời do quên review | Cao nếu không có lịch | Tự động cảnh báo qua `next_review_due` quá hạn — agent phải flag khi đọc file có `next_review_due` đã qua |
| Trích dẫn sai do soạn thủ công | Trung bình | Bắt buộc review chéo ở Giai đoạn 1, spot-check định kỳ sau đó |
| Corpus bị dùng thay thế hoàn toàn cho verify thật (agent "lười" search) | Cao — đây là rủi ro lớn nhất | Ghi rõ trong mọi SKILL.md liên quan: corpus chỉ là định hướng, hợp đồng giá trị cao/rủi ro CRITICAL-HIGH bắt buộc verify qua vbpl.vn trước final draft (đã có sẵn cơ chế trong `contract-quality-gate.md`) |
| Luật mới (BVDLCN 2025) có nghị định/thông tư hướng dẫn ban hành sau, làm thay đổi cách áp dụng | Cao trong 6-12 tháng đầu | Review 30 ngày/lần riêng cho nhóm luật mới, theo dõi chủ động tin tức pháp lý |
| Phình to corpus với văn bản ít dùng, khó bảo trì | Thấp nhưng tích lũy theo thời gian | Áp dụng quy tắc "≥2 lần cần dùng thực tế mới thêm vào corpus" ở Mục 1 |

---

## 8. Tiêu chí nghiệm thu tổng thể (Definition of Done)

Plan được coi là **áp dụng thành công** khi:

- [ ] Toàn bộ Nhóm 1 (6 văn bản) có file trong `references/laws/`, đúng schema, đã review chéo
- [ ] `_INDEX.md` phản ánh đúng trạng thái tất cả văn bản
- [ ] `skills/legal-research/SKILL.md`, `skills/contract-drafting/SKILL.md`, `skills/contract-review/SKILL.md` đã cập nhật để trỏ vào corpus đúng cách
- [ ] Test thực tế với ≥3 tình huống nghiệp vụ thật, agent trả lời đúng và biết khi nào cần verify thêm qua vbpl.vn
- [ ] Lịch review định kỳ đã thiết lập và có người phụ trách rõ ràng
- [ ] Không có văn bản nào trong corpus ở trạng thái "CẦN XÁC MINH" còn tồn đọng quá 7 ngày

---

## 9. Việc KHÔNG làm (out of scope, tránh scope creep)

- Không tự động hóa crawl (đó là Hướng C)
- Không đưa toàn văn luật vào (chỉ trích yếu liên quan)
- Không để corpus thay thế vai trò luật sư cho hợp đồng CRITICAL/HIGH
- Không mở rộng sang luật lao động, luật đất đai, v.v. trừ khi có nhu cầu nghiệp vụ thật phát sinh

---

## 10. Ghi chú cho agent khi thực thi plan này

Nếu bạn (Claude Code/ZCode) được giao thực thi plan này:

1. Bắt đầu từ Giai đoạn 1, không nhảy cóc.
2. Với mỗi văn bản, PHẢI web-search/fetch bản trên vbpl.vn trước khi soạn file trích yếu — không tự viết từ trí nhớ.
3. Nếu không tìm được bản hợp nhất mới nhất hoặc không chắc về số hiệu văn bản sửa đổi, để `status: "CẦN XÁC MINH"` và báo lại cho người phụ trách, không đoán.
4. Sau mỗi file soạn xong, tự kiểm tra lại theo checklist Mục 3 trước khi coi là hoàn thành.
5. Cập nhật `_INDEX.md` ngay sau mỗi file, không để dồn cuối giai đoạn mới cập nhật.
