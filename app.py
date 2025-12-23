import streamlit as st
import datetime
import time
import pytz

# Cấu hình trang
st.set_page_config(
    page_title="Clock App",
    page_icon="🕐",
    layout="wide"
)

# CSS tùy chỉnh
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1E88E5;
        margin-bottom: 2rem;
    }
    .digital-clock {
        font-size: 4rem;
        font-weight: bold;
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        color: white;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .stopwatch-display {
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 20px;
        color: white;
        margin: 2rem 0;
    }
    .countdown-display {
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        border-radius: 20px;
        color: white;
        margin: 2rem 0;
    }
    .stButton>button {
        width: 100%;
        height: 3rem;
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 10px;
    }
    .world-clock-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 1.5rem;
        color: white;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .footer-info {
        margin-top: 3rem;
        padding: 1.5rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 10px;
        text-align: center;
        font-size: 0.9rem;
        color: #333;
    }
    .author-info {
        margin-top: 2rem;
        padding: 1rem;
        background: #f0f2f6;
        border-radius: 8px;
        font-size: 0.85rem;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# Khởi tạo session state
if 'stopwatch_running' not in st.session_state:
    st.session_state.stopwatch_running = False
if 'stopwatch_time' not in st.session_state:
    st.session_state.stopwatch_time = 0
if 'stopwatch_start' not in st.session_state:
    st.session_state.stopwatch_start = None
if 'laps' not in st.session_state:
    st.session_state.laps = []
if 'countdown_running' not in st.session_state:
    st.session_state.countdown_running = False
if 'countdown_time' not in st.session_state:
    st.session_state.countdown_time = 0
if 'countdown_total' not in st.session_state:
    st.session_state.countdown_total = 0
if 'countdown_start' not in st.session_state:
    st.session_state.countdown_start = None
if 'auto_refresh' not in st.session_state:
    st.session_state.auto_refresh = False

# Tiêu đề
st.markdown('<h1 class="main-header">🕐 Clock App - Ứng dụng Đồng hồ Điện tử</h1>', unsafe_allow_html=True)

# Sidebar để chọn chức năng
st.sidebar.title("Chọn chức năng")
app_mode = st.sidebar.radio(
    "Danh sách chức năng:",
    ["Đồng hồ số", "Đồng hồ thế giới", "Đồng hồ bấm giờ", "Bộ đếm ngược"]
)

# Thông tin người tạo
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <div class="author-info">
        <strong>👨‍💻 Người tạo:</strong><br>
        DanhBeta<br><br>
        <strong>📦 Phiên bản:</strong><br>
        Version 01<br><br>
        <strong>📧 Liên hệ:</strong><br>
        <a href="mailto:dinhthanhdanh@gmail.com" style="color: #1E88E5; text-decoration: none;">
            dinhthanhdanh@gmail.com
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ==================== 1. ĐỒNG HỒ SỐ THỜI GIAN THỰC ====================
if app_mode == "Đồng hồ số":
    st.header("⏰ Đồng hồ số thời gian thực")
    
    format_choice = st.radio(
        "Chọn định dạng thời gian:",
        ["24 giờ", "12 giờ (AM/PM)"],
        horizontal=True,
        key="format-choice-radio"
    )
    
    # Hiển thị đồng hồ
    now = datetime.datetime.now()
    if format_choice == "24 giờ":
        time_str = now.strftime("%H:%M:%S")
    else:
        time_str = now.strftime("%I:%M:%S %p")
    date_str = now.strftime("%d/%m/%Y")
    
    clock_placeholder = st.empty()
    clock_placeholder.markdown(
        f"""
        <div class="digital-clock">
            <div style="font-size: 2rem; margin-bottom: 1rem;">{date_str}</div>
            <div>{time_str}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Auto-refresh mỗi giây
    time.sleep(1)
    st.rerun()

# ==================== 2. ĐỒNG HỒ THẾ GIỚI ====================
elif app_mode == "Đồng hồ thế giới":
    st.header("🌍 Đồng hồ thế giới")
    
    # Danh sách các múi giờ phổ biến
    timezones = {
        "Việt Nam (Hà Nội)": "Asia/Ho_Chi_Minh",
        "Mỹ (New York)": "America/New_York",
        "Mỹ (Los Angeles)": "America/Los_Angeles",
        "Anh (London)": "Europe/London",
        "Pháp (Paris)": "Europe/Paris",
        "Đức (Berlin)": "Europe/Berlin",
        "Nhật Bản (Tokyo)": "Asia/Tokyo",
        "Hàn Quốc (Seoul)": "Asia/Seoul",
        "Trung Quốc (Bắc Kinh)": "Asia/Shanghai",
        "Ấn Độ (New Delhi)": "Asia/Kolkata",
        "Úc (Sydney)": "Australia/Sydney",
        "Dubai": "Asia/Dubai",
        "Singapore": "Asia/Singapore",
        "Thái Lan (Bangkok)": "Asia/Bangkok",
        "Nga (Moscow)": "Europe/Moscow",
    }
    
    st.subheader("Chọn các múi giờ để hiển thị:")
    selected_timezones = st.multiselect(
        "Chọn múi giờ:",
        options=list(timezones.keys()),
        default=["Việt Nam (Hà Nội)", "Mỹ (New York)", "Anh (London)", "Nhật Bản (Tokyo)"]
    )
    
    # Hiển thị đồng hồ thế giới
    if selected_timezones:
        # Tạo grid layout
        cols_per_row = 3
        for i in range(0, len(selected_timezones), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, tz_name in enumerate(selected_timezones[i:i+cols_per_row]):
                with cols[j]:
                    tz_key = timezones[tz_name]
                    try:
                        tz = pytz.timezone(tz_key)
                        now_tz = datetime.datetime.now(tz)
                        time_str = now_tz.strftime("%H:%M:%S")
                        date_str = now_tz.strftime("%d/%m/%Y")
                    except Exception as e:
                        time_str = "Error"
                        date_str = "Error"
                    
                    st.markdown(
                        f"""
                        <div class="world-clock-card">
                            <div style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.5rem;">{tz_name}</div>
                            <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 1rem;">{date_str}</div>
                            <div style="font-size: 2.5rem; font-weight: bold;">{time_str}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        
        # Auto-refresh mỗi giây
        time.sleep(1)
        st.rerun()
    else:
        st.info("Vui lòng chọn ít nhất một múi giờ để hiển thị.")

# ==================== 3. ĐỒNG HỒ BẤM GIỜ (STOPWATCH) ====================
elif app_mode == "Đồng hồ bấm giờ":
    st.header("⏱️ Đồng hồ bấm giờ")
    
    # Các nút điều khiển
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("▶️ Start", type="primary"):
            if not st.session_state.stopwatch_running:
                st.session_state.stopwatch_running = True
                st.session_state.stopwatch_start = time.time() - st.session_state.stopwatch_time
                st.rerun()
    
    with col2:
        if st.button("⏸️ Stop"):
            if st.session_state.stopwatch_running:
                st.session_state.stopwatch_running = False
                if st.session_state.stopwatch_start:
                    st.session_state.stopwatch_time = time.time() - st.session_state.stopwatch_start
                st.rerun()
    
    with col3:
        if st.button("⏹️ Reset"):
            st.session_state.stopwatch_running = False
            st.session_state.stopwatch_time = 0
            st.session_state.stopwatch_start = None
            st.session_state.laps = []
            st.rerun()
    
    with col4:
        if st.button("⏱️ Lap"):
            if st.session_state.stopwatch_running or st.session_state.stopwatch_time > 0:
                if st.session_state.stopwatch_running and st.session_state.stopwatch_start:
                    current_time = time.time() - st.session_state.stopwatch_start
                else:
                    current_time = st.session_state.stopwatch_time
                st.session_state.laps.append(current_time)
                st.rerun()
    
    # Cập nhật thời gian
    if st.session_state.stopwatch_running and st.session_state.stopwatch_start:
        st.session_state.stopwatch_time = time.time() - st.session_state.stopwatch_start
    
    # Format và hiển thị thời gian
    total_seconds = int(st.session_state.stopwatch_time)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    milliseconds = int((st.session_state.stopwatch_time - total_seconds) * 100)
    
    time_display = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
    
    st.markdown(
        f"""
        <div class="stopwatch-display">
            {time_display}
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Hiển thị danh sách Laps
    if st.session_state.laps:
        st.subheader("📋 Danh sách Laps:")
        lap_data = []
        for i, lap_time in enumerate(st.session_state.laps, 1):
            total_sec = int(lap_time)
            h = total_sec // 3600
            m = (total_sec % 3600) // 60
            s = total_sec % 60
            ms = int((lap_time - total_sec) * 100)
            lap_str = f"{h:02d}:{m:02d}:{s:02d}.{ms:02d}"
            lap_data.append({"Lap #": i, "Thời gian": lap_str})
        
        st.table(lap_data)
    
    # Auto-refresh khi đang chạy
    if st.session_state.stopwatch_running:
        time.sleep(0.1)
        st.rerun()

# ==================== 4. BỘ ĐẾM NGƯỢC (COUNTDOWN TIMER) ====================
elif app_mode == "Bộ đếm ngược":
    st.header("⏳ Bộ đếm ngược")
    
    # Nhập thời gian
    col1, col2, col3 = st.columns(3)
    with col1:
        hours_input = st.number_input("Giờ", min_value=0, max_value=23, value=0, step=1, key="countdown_hours")
    with col2:
        minutes_input = st.number_input("Phút", min_value=0, max_value=59, value=0, step=1, key="countdown_minutes")
    with col3:
        seconds_input = st.number_input("Giây", min_value=0, max_value=59, value=0, step=1, key="countdown_seconds")
    
    total_seconds_input = hours_input * 3600 + minutes_input * 60 + seconds_input
    
    # Các nút điều khiển
    col1, col2, col3 = st.columns(3)
    
    with col1:
        start_btn = st.button("▶️ Bắt đầu", type="primary")
        if start_btn:
            if total_seconds_input > 0 and not st.session_state.countdown_running:
                st.session_state.countdown_running = True
                st.session_state.countdown_time = total_seconds_input
                st.session_state.countdown_total = total_seconds_input
                st.session_state.countdown_start = time.time()
                st.rerun()
    
    with col2:
        pause_btn = st.button("⏸️ Tạm dừng")
        if pause_btn:
            if st.session_state.countdown_running:
                st.session_state.countdown_running = False
                # Lưu thời gian còn lại
                if st.session_state.countdown_start:
                    elapsed = time.time() - st.session_state.countdown_start
                    st.session_state.countdown_time = max(0, st.session_state.countdown_total - elapsed)
                    st.session_state.countdown_total = st.session_state.countdown_time
                st.rerun()
    
    with col3:
        reset_btn = st.button("⏹️ Reset")
        if reset_btn:
            st.session_state.countdown_running = False
            st.session_state.countdown_time = 0
            st.session_state.countdown_total = 0
            st.session_state.countdown_start = None
            st.rerun()
    
    # Cập nhật countdown
    if st.session_state.countdown_running and st.session_state.countdown_start:
        elapsed = time.time() - st.session_state.countdown_start
        st.session_state.countdown_time = max(0, st.session_state.countdown_total - elapsed)
        
        if st.session_state.countdown_time <= 0:
            st.session_state.countdown_running = False
            st.balloons()  # Thông báo hoàn thành với balloons
            st.success("⏰ Đếm ngược hoàn thành!")
    
    # Format và hiển thị thời gian
    remaining = int(st.session_state.countdown_time)
    h = remaining // 3600
    m = (remaining % 3600) // 60
    s = remaining % 60
    
    time_display = f"{h:02d}:{m:02d}:{s:02d}"
    
    st.markdown(
        f"""
        <div class="countdown-display">
            {time_display}
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Thanh tiến trình
    if st.session_state.countdown_total > 0:
        progress = st.session_state.countdown_time / st.session_state.countdown_total
        st.progress(progress)
    else:
        st.progress(1.0)
    
    # Auto-refresh khi đang chạy
    if st.session_state.countdown_running:
        time.sleep(0.1)
        st.rerun()
