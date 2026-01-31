🛣️ Hệ Thống Nhận Diện Làn Đường AI: YOLOv10 vs YOLOv8-Seg vs YOLO-TS
Dự án nghiên cứu và so sánh hiệu năng giữa các kiến trúc Deep Learning hiện đại trong bài toán nhận diện vạch kẻ đường giao thông, phục vụ cho xe tự hành.

📊 1. Tập dữ liệu (Dataset)Nguồn: TuSimple-Ace the Lane Detection Challenge.
Quy mô: Subset gồm 600 ảnh chất lượng cao đã được gán nhãn.

Đặc điểm: Tập trung vào kịch bản đường cao tốc với các vạch kẻ đường rõ ràng, đa dạng về điều kiện ánh sáng và góc nhìn.

📈 2. Kết quả huấn luyện & So sánhNhờ áp dụng Transfer Learning, mô hình đạt được độ chính xác cực cao dù huấn luyện trên tập dữ liệu nhỏ:
Mô hình,Nhiệm vụ,mAP50,Tốc độ (ms),GFLOPs

YOLOv10,Detection,0.989,47.0,8.1

YOLOv8-Seg,Segmentation,0.990,65.5,12.0

YOLO-TS,Hybrid,0.950,52.5,8.1

3.Nhận định chuyên môn:

YOLOv10 (SOTA Performance): Là mô hình xuất sắc nhất trong dự án, đạt sự cân bằng hoàn hảo khi có tốc độ nhanh nhất (47ms) và độ chính xác tiệm cận tuyệt đối (0.989). Đây là lựa chọn hàng đầu cho các hệ thống nhúng trên xe tự hành yêu cầu phản hồi thời gian thực.

YOLOv8-Seg (Precision & Detail): Đạt mAP cao nhất (0.990), phù hợp cho các bài toán cần phân đoạn chi tiết hình dạng làn đường (Instance Segmentation), dù tốc độ xử lý chậm hơn do cấu trúc phức tạp.

YOLO-TS (Standard Baseline): Cung cấp hiệu năng ổn định với mAP 0.950. Tuy nhiên, so với hai kiến trúc còn lại, YOLO-TS bộc lộ hạn chế về khả năng tối ưu hóa giữa tốc độ và độ chính xác trong cùng một mức tài nguyên tính toán (8.1 GFLOPs).

4.Triển khai Local Dashboard
Dự án bao gồm một giao diện web trực quan để so sánh kết quả thực tế từ 3 mô hình.

Yêu cầu hệ thống:
Python 3.12+

Cài đặt môi trường:
pip install -r requirements_dashboard.txt

Chạy ứng dụng:
python -m streamlit run web_dashboard.py

Thư viện: streamlit, pandas, plotly, ultralytics.

📂 5. Cấu trúc dự án
/
├── dash_board_3_model.py  # File chạy Dashboard Local

├── requirements_model.txt # Thư viện cho YOLO

├── requirements_dashboard.txt # Thư viện cho Dashboard

├── weights/               # Chứa các file .pt của YOLOv10, YOLOv8-Seg

└── demo/                  # Video kết quả thực tế từ 3 model
