import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# Cấu hình trang
st.set_page_config(page_title="Lane Detection Dashboard", layout="wide")

# Đường dẫn thư mục chứa video (Sử dụng raw string 'r' để tránh lỗi đường dẫn Windows)
BASE_DIR = r"D:\NCKH\lane_detection_results"

st.title("🛣️ Hệ Thống Nhận Diện Làn Đường - So Sánh 3 Mô Hình")
st.markdown(f"**Vị trí dữ liệu:** `{BASE_DIR}`")
st.markdown("---")

# 1. DỮ LIỆU THỰC TẾ (Cập nhật từ kết quả huấn luyện của bạn)
data = {
    'Model': ['YOLOv10', 'YOLOv8-Seg', 'YOLO-TS'],
    'mAP50': [0.989, 0.990, 0.950], #
    'Speed (ms)': [47.0, 65.5, 52.5],
    'GFLOPs': [8.1, 12.0, 8.1]
}
df = pd.DataFrame(data)

# 2. BIỂU ĐỒ TƯƠNG TÁC
st.subheader("📊 Phân Tích Chỉ Số Hiệu Năng")
c1, c2 = st.columns(2)

with c1:
    fig_map = go.Figure(data=[
        go.Bar(x=df['Model'], y=df['mAP50'], 
               marker_color=['#3498db', '#9b59b6', '#95a5a6'],
               text=df['mAP50'], textposition='auto')
    ])
    fig_map.update_layout(title="Độ chính xác mAP50", yaxis_range=[0.9, 1.0])
    st.plotly_chart(fig_map, use_container_width=True)

with c2:
    # Sử dụng biểu đồ cột thay cho biểu đồ đường
    fig2 = go.Figure(data=[
        go.Bar(
            x=df['Model'], 
            y=df['Speed (ms)'], 
            marker_color=['#2ecc71', '#e74c3c', '#f39c12'], # Màu xanh cho model nhanh nhất
            text=df['Speed (ms)'], 
            textposition='auto'
        )
    ])
    fig2.update_layout(
        title="Tốc độ suy luận (ms) - Thấp hơn là nhanh hơn",
        yaxis_title="mili giây (ms)"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# 3. HIỂN THỊ 3 VIDEO DEMO
st.subheader("📺 Video Demo Kết Quả Thực Tế")
v_cols = st.columns(3)

# Danh sách tên file video khớp với thư mục của bạn
video_files = ["YOLOv10_Demo.mp4", "YOLOv8_demo.mp4", "YOLO_TS_demo.mp4"]

for i, video_name in enumerate(video_files):
    with v_cols[i]:
        video_path = os.path.join(BASE_DIR, video_name)
        st.markdown(f"**📽️ {video_name}**")
        
        if os.path.exists(video_path):
            # Mở file video dưới dạng binary để Streamlit đọc trực tiếp từ ổ cứng
            with open(video_path, 'rb') as v_file:
                video_bytes = v_file.read()
                st.video(video_bytes)
        else:
            st.error(f"⚠️ Không tìm thấy file tại đường dẫn: {video_path}")

# 4. BẢNG DỮ LIỆU CHI TIẾT
st.markdown("---")
st.subheader("📋 Chi Tiết Thông Số Kỹ Thuật")
st.table(df)