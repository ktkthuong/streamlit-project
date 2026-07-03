import streamlit as st # Nạp thư viện Streamlit và đặt tên là st

import time

st.write('Xin chào') # Hiển thị dòng chữ "Xin chao" lên trang web.
st.title("My web") # Hiển thị tiêu đề lớn My web.
name = st.text_input("Nhập tên của bạn: ") # Tạo một ô nhập liệu với nhãn "Nhập tên của bạn:".
age = st.number_input("Nhập tuổi:", min_value=0)

if st.button("Hiển thị"):
    st.write("Tên:", name)
    st.write("Tuổi:", age)
    
name1 = st.text_input("Họ và tên")
if st.button('Xác nhận'):
    st.write('Xin chào :grinning:', name1)
    
st.title("My progress")
my_bar = st.progress(0) #Thanh tiến trình sẽ bắt đầu ở mức 0%

for percent_complete in range(100): #vòng lặp lặp 100 lần
    time.sleep(0.05) #dừng ở 0.05 giây = 50 mili giây
    #vì sao + thêm 1 vào => nếu chỉ viết my_bar.progress(percent_complete) thì chỉ chạy được 99%
    my_bar.progress(percent_complete + 1) # mỗi lần lặp tăng lên 1%
    
    
    
st.title("Tiến trình xử lý")

# Tạo thanh tiến trình ban đầu
my_bar = st.progress(0)

# Hiển thị trạng thái hiện tại
status = st.empty()

# ===== BƯỚC 1 =====
status.write("🔹 Bước 1: Đang chuẩn bị dữ liệu...")
my_bar.progress(25)
time.sleep(2)

# ===== BƯỚC 2 =====
status.write("🔹 Bước 2: Đang xử lý dữ liệu...")
my_bar.progress(50)
time.sleep(2)

# ===== BƯỚC 3 =====
status.write("🔹 Bước 3: Đang tạo kết quả...")
my_bar.progress(75)
time.sleep(2)

# ===== HOÀN THÀNH =====
status.write("✅ Hoàn thành!")
my_bar.progress(100)

if st.button("Click me"):
    st.balloons()
    