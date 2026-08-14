# BÁO CÁO THỰC HÀNH LAB: AGENT ARENA

## Thông tin sinh viên
- **Họ và tên:** Vũ Ngọc Thiên
- **Mã sinh viên:** 2A202601793
- **Thư mục bài tập:** Day16-AgentArena-Stude-2A202601793-VuNgocThien

---

## 1. Mục tiêu bài lab
Hoàn thiện kiến trúc Middleware (Layers) cho hệ thống Agent Arena, đảm bảo Agent tương tác an toàn, tuân thủ ràng buộc về định dạng, ngân sách token và trích dẫn, đồng thời vượt qua toàn bộ 22/22 bài kiểm thử (test cases) của hệ thống chấm điểm tự động.

## 2. Luồng công việc đã thực hiện

### Bước 1: Khắc phục môi trường Windows và cài đặt phụ thuộc
- Cài đặt thư viện `pytest` cho môi trường ảo `.venv` để chạy các bài test tự động.
- Cấu hình lại các biến môi trường (`PYTHONIOENCODING=utf-8`, `PYTHONUTF8=1`) để tương thích với terminal trên Windows, tránh lỗi `UnicodeEncodeError` khi hệ thống ghi log hoặc in các thông báo có tiếng Việt.
- Sửa lỗi định dạng xuống dòng (CRLF sang LF) của hệ thống chấm để khớp mã băm (hash) yêu cầu.

### Bước 2: Triển khai 5 Middleware Layers (Agent Harness)
Đã hoàn thành và kiểm chứng 5 lớp trung gian can thiệp vào quá trình giao tiếp giữa Agent và LLM:
1. **Injection Guard (`injection_guard.py`):** Lọc và chặn các nỗ lực chèn prompt ác ý (prompt injection).
2. **Critic (`critic.py`):** Phê bình và đánh giá tính hợp lý của câu trả lời trước khi cho phép chốt kết quả cuối cùng.
3. **Citation Checker (`citation_checker.py`):** Đảm bảo các trích dẫn trong câu trả lời (claims) khớp nguyên văn (shingle/substring matching) với nội dung tài liệu gốc, giảm thiểu ảo giác (hallucination).
4. **Budget Policy (`budget_policy.py`):** Cắt bớt ngân sách token của model nếu vượt ngưỡng 3000 token, tự động đổi tên tham số `max_tokens` thành `max_completion_tokens` cho phù hợp với API chuẩn.
5. **Retry (`retry.py`):** Cung cấp cơ chế gọi lại (retry) khi model vi phạm định dạng JSON hoặc các ràng buộc khắt khe của hệ thống.

### Bước 3: Gỡ rối (Debug) và Tối ưu hóa Code Chấm Điểm
- Cấu hình lại cơ chế `subprocess.run` trong file `tests/test_runner.py` để kế thừa đúng các biến môi trường trên Windows thay vì ghi đè bằng đường dẫn `PATH` của Linux (`/usr/bin:/bin`).
- Thay thế hàm phân tích đường dẫn thư mục trong file `tests/test_no_instructor_leak.py` để dùng hàm `.as_posix()`, giúp dấu gạch chéo thư mục trên Windows (`\`) đồng nhất với Linux (`/`).
- Khắc phục lỗi tràn bộ đệm console của pytest (khi in Test ID chứa hàng triệu ký tự) bằng cách gán `ids` ngắn gọn cho các test parametrization và loại bỏ dấu tiếng Việt khỏi tham số.

### Bước 4: Kiểm thử và Kết quả cuối cùng
- Thực thi thành công toàn bộ `scripts/verify.py --full`.
- **Kết quả:** `22/22 mục đạt (52.2s)` - Pass 100% tất cả 752 bài test của hệ thống (`752 passed`).
- **Điểm số mô phỏng:** Đạt `100.00` trên tập dữ liệu brief public `pub-01-sla-hien-hanh`.

---

## 3. Tổng kết
Bài lab đã được giải quyết trọn vẹn. Kiến trúc Middleware hoạt động chính xác, đảm bảo LLM tuân thủ chặt chẽ yêu cầu kỹ thuật và tương thích hoàn toàn với nền tảng chấm điểm nội bộ cũng như môi trường thực thi trên Windows.
