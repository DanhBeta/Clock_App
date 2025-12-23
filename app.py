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

# Dictionary đa ngôn ngữ
translations = {
    'vi': {
        'title': '🕐 Clock App - Ứng dụng Đồng hồ Điện tử',
        'select_function': 'Chọn chức năng',
        'function_list': 'Danh sách chức năng:',
        'digital_clock': 'Đồng hồ số',
        'world_clock': 'Đồng hồ thế giới',
        'stopwatch': 'Đồng hồ bấm giờ',
        'countdown': 'Bộ đếm ngược',
        'select_language': '🌐 Chọn ngôn ngữ / Select Language',
        'digital_clock_title': '⏰ Đồng hồ số thời gian thực',
        'select_time_format': 'Chọn định dạng thời gian:',
        'format_24h': '24 giờ',
        'format_12h': '12 giờ (AM/PM)',
        'world_clock_title': '🌍 Đồng hồ thế giới',
        'select_timezones': 'Chọn các múi giờ để hiển thị:',
        'select_timezone': 'Chọn múi giờ:',
        'please_select_timezone': 'Vui lòng chọn ít nhất một múi giờ để hiển thị.',
        'stopwatch_title': '⏱️ Đồng hồ bấm giờ',
        'start': 'Start',
        'stop': 'Stop',
        'reset': 'Reset',
        'lap': 'Lap',
        'lap_list': '📋 Danh sách Laps:',
        'lap_number': 'Lap #',
        'time': 'Thời gian',
        'countdown_title': '⏳ Bộ đếm ngược',
        'hours': 'Giờ',
        'minutes': 'Phút',
        'seconds': 'Giây',
        'start_countdown': 'Bắt đầu',
        'pause': 'Tạm dừng',
        'countdown_complete': '⏰ Đếm ngược hoàn thành!',
        'creator': '👨‍💻 Người tạo:',
        'version': '📦 Phiên bản:',
        'contact': '📧 Liên hệ:'
    },
    'en': {
        'title': '🕐 Clock App - Digital Clock Application',
        'select_function': 'Select Function',
        'function_list': 'Function List:',
        'digital_clock': 'Digital Clock',
        'world_clock': 'World Clock',
        'stopwatch': 'Stopwatch',
        'countdown': 'Countdown Timer',
        'select_language': '🌐 Select Language',
        'digital_clock_title': '⏰ Real-time Digital Clock',
        'select_time_format': 'Select time format:',
        'format_24h': '24 hours',
        'format_12h': '12 hours (AM/PM)',
        'world_clock_title': '🌍 World Clock',
        'select_timezones': 'Select timezones to display:',
        'select_timezone': 'Select timezone:',
        'please_select_timezone': 'Please select at least one timezone to display.',
        'stopwatch_title': '⏱️ Stopwatch',
        'start': 'Start',
        'stop': 'Stop',
        'reset': 'Reset',
        'lap': 'Lap',
        'lap_list': '📋 Lap List:',
        'lap_number': 'Lap #',
        'time': 'Time',
        'countdown_title': '⏳ Countdown Timer',
        'hours': 'Hours',
        'minutes': 'Minutes',
        'seconds': 'Seconds',
        'start_countdown': 'Start',
        'pause': 'Pause',
        'countdown_complete': '⏰ Countdown completed!',
        'creator': '👨‍💻 Creator:',
        'version': '📦 Version:',
        'contact': '📧 Contact:'
    }
}

# Dictionary tên múi giờ đa ngôn ngữ
timezone_names = {
    'vi': {
        'Việt Nam (Hà Nội)': 'Việt Nam (Hà Nội)',
        'Mỹ (New York)': 'Mỹ (New York)',
        'Mỹ (Los Angeles)': 'Mỹ (Los Angeles)',
        'Anh (London)': 'Anh (London)',
        'Pháp (Paris)': 'Pháp (Paris)',
        'Đức (Berlin)': 'Đức (Berlin)',
        'Nhật Bản (Tokyo)': 'Nhật Bản (Tokyo)',
        'Hàn Quốc (Seoul)': 'Hàn Quốc (Seoul)',
        'Trung Quốc (Bắc Kinh)': 'Trung Quốc (Bắc Kinh)',
        'Ấn Độ (New Delhi)': 'Ấn Độ (New Delhi)',
        'Úc (Sydney)': 'Úc (Sydney)',
        'Dubai': 'Dubai',
        'Singapore': 'Singapore',
        'Thái Lan (Bangkok)': 'Thái Lan (Bangkok)',
        'Nga (Moscow)': 'Nga (Moscow)'
    },
    'en': {
        'Việt Nam (Hà Nội)': 'Vietnam (Hanoi)',
        'Mỹ (New York)': 'USA (New York)',
        'Mỹ (Los Angeles)': 'USA (Los Angeles)',
        'Anh (London)': 'UK (London)',
        'Pháp (Paris)': 'France (Paris)',
        'Đức (Berlin)': 'Germany (Berlin)',
        'Nhật Bản (Tokyo)': 'Japan (Tokyo)',
        'Hàn Quốc (Seoul)': 'South Korea (Seoul)',
        'Trung Quốc (Bắc Kinh)': 'China (Beijing)',
        'Ấn Độ (New Delhi)': 'India (New Delhi)',
        'Úc (Sydney)': 'Australia (Sydney)',
        'Dubai': 'Dubai',
        'Singapore': 'Singapore',
        'Thái Lan (Bangkok)': 'Thailand (Bangkok)',
        'Nga (Moscow)': 'Russia (Moscow)'
    }
}

# Khởi tạo session state
if 'language' not in st.session_state:
    st.session_state.language = 'vi'
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

# Hàm helper để lấy văn bản theo ngôn ngữ
def t(key):
    return translations[st.session_state.language].get(key, key)

# Tiêu đề
st.markdown(f'<h1 class="main-header">{t("title")}</h1>', unsafe_allow_html=True)

# Sidebar - Chọn ngôn ngữ
lang_options = {'Tiếng Việt': 'vi', 'English': 'en'}
lang_labels = list(lang_options.keys())
current_lang_index = 0 if st.session_state.language == 'vi' else 1
selected_lang_label = st.sidebar.selectbox(
    t('select_language'),
    lang_labels,
    index=current_lang_index,
    key='lang_select'
)
st.session_state.language = lang_options[selected_lang_label]

st.sidebar.markdown("---")

# Sidebar để chọn chức năng
st.sidebar.title(t("select_function"))
app_mode = st.sidebar.radio(
    t("function_list"),
    [t("digital_clock"), t("world_clock"), t("stopwatch"), t("countdown")]
)

# Thông tin người tạo
st.sidebar.markdown("---")
st.sidebar.markdown(
    f"""
    <div class="author-info">
        <strong>{t("creator")}</strong><br>
        DanhBeta<br><br>
        <strong>{t("version")}</strong><br>
        Version 01<br><br>
        <strong>{t("contact")}</strong><br>
        <a href="mailto:dinhthanhdanh@gmail.com" style="color: #1E88E5; text-decoration: none;">
            dinhthanhdanh@gmail.com
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ==================== 1. ĐỒNG HỒ SỐ THỜI GIAN THỰC ====================
if app_mode == t("digital_clock"):
    st.header(t("digital_clock_title"))
    
    format_choice = st.radio(
        t("select_time_format"),
        [t("format_24h"), t("format_12h")],
        horizontal=True,
        key="format-choice-radio"
    )
    
    # Hiển thị đồng hồ
    now = datetime.datetime.now()
    if format_choice == t("format_24h"):
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
elif app_mode == t("world_clock"):
    st.header(t("world_clock_title"))
    
    # Danh sách các múi giờ phổ biến (key internal, value timezone)
    timezones_dict = {
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
    
    # Tạo danh sách tên múi giờ theo ngôn ngữ
    timezone_options = [timezone_names[st.session_state.language][key] for key in timezones_dict.keys()]
    
    # Default timezones - chỉ set khi chưa có selection trước đó
    if 'timezone_selection_orig' not in st.session_state:
        default_keys = ["Việt Nam (Hà Nội)", "Mỹ (New York)", "Anh (London)", "Nhật Bản (Tokyo)"]
        default_timezones = [timezone_names[st.session_state.language][key] for key in default_keys]
        st.session_state.timezone_selection_orig = default_keys
    else:
        # Giữ nguyên selection, chỉ đổi tên hiển thị
        default_timezones = [timezone_names[st.session_state.language][key] 
                            for key in st.session_state.timezone_selection_orig 
                            if key in timezones_dict]
    
    st.subheader(t("select_timezones"))
    selected_timezones_display = st.multiselect(
        t("select_timezone"),
        options=timezone_options,
        default=default_timezones,
        key="timezone_select"
    )
    
    # Lưu selection gốc
    reverse_timezone_map = {timezone_names[st.session_state.language][k]: k for k in timezones_dict.keys()}
    selected_timezones_orig = [reverse_timezone_map[tz] for tz in selected_timezones_display if tz in reverse_timezone_map]
    st.session_state.timezone_selection_orig = selected_timezones_orig
    
    # Map lại từ tên hiển thị về key gốc
    selected_timezones = selected_timezones_orig
    
    # Hiển thị đồng hồ thế giới
    if selected_timezones:
        # Tạo grid layout
        cols_per_row = 3
        for i in range(0, len(selected_timezones), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, tz_key_orig in enumerate(selected_timezones[i:i+cols_per_row]):
                with cols[j]:
                    tz_key = timezones_dict[tz_key_orig]
                    tz_display_name = timezone_names[st.session_state.language][tz_key_orig]
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
                            <div style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.5rem;">{tz_display_name}</div>
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
        st.info(t("please_select_timezone"))

# ==================== 3. ĐỒNG HỒ BẤM GIỜ (STOPWATCH) ====================
elif app_mode == t("stopwatch"):
    st.header(t("stopwatch_title"))
    
    # Các nút điều khiển
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button(f"▶️ {t('start')}", type="primary", key="stopwatch_start"):
            if not st.session_state.stopwatch_running:
                st.session_state.stopwatch_running = True
                st.session_state.stopwatch_start = time.time() - st.session_state.stopwatch_time
                st.rerun()
    
    with col2:
        if st.button(f"⏸️ {t('stop')}", key="stopwatch_stop"):
            if st.session_state.stopwatch_running:
                st.session_state.stopwatch_running = False
                if st.session_state.stopwatch_start:
                    st.session_state.stopwatch_time = time.time() - st.session_state.stopwatch_start
                st.rerun()
    
    with col3:
        if st.button(f"⏹️ {t('reset')}", key="stopwatch_reset"):
            st.session_state.stopwatch_running = False
            st.session_state.stopwatch_time = 0
            st.session_state.stopwatch_start = None
            st.session_state.laps = []
            st.rerun()
    
    with col4:
        if st.button(f"⏱️ {t('lap')}", key="stopwatch_lap"):
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
        st.subheader(t("lap_list"))
        lap_data = []
        for i, lap_time in enumerate(st.session_state.laps, 1):
            total_sec = int(lap_time)
            h = total_sec // 3600
            m = (total_sec % 3600) // 60
            s = total_sec % 60
            ms = int((lap_time - total_sec) * 100)
            lap_str = f"{h:02d}:{m:02d}:{s:02d}.{ms:02d}"
            lap_data.append({t("lap_number"): i, t("time"): lap_str})
        
        st.table(lap_data)
    
    # Auto-refresh khi đang chạy
    if st.session_state.stopwatch_running:
        time.sleep(0.1)
        st.rerun()

# ==================== 4. BỘ ĐẾM NGƯỢC (COUNTDOWN TIMER) ====================
elif app_mode == t("countdown"):
    st.header(t("countdown_title"))
    
    # Nhập thời gian
    col1, col2, col3 = st.columns(3)
    with col1:
        hours_input = st.number_input(t("hours"), min_value=0, max_value=23, value=0, step=1, key="countdown_hours")
    with col2:
        minutes_input = st.number_input(t("minutes"), min_value=0, max_value=59, value=0, step=1, key="countdown_minutes")
    with col3:
        seconds_input = st.number_input(t("seconds"), min_value=0, max_value=59, value=0, step=1, key="countdown_seconds")
    
    total_seconds_input = hours_input * 3600 + minutes_input * 60 + seconds_input
    
    # Các nút điều khiển
    col1, col2, col3 = st.columns(3)
    
    with col1:
        start_btn = st.button(f"▶️ {t('start_countdown')}", type="primary", key="countdown_start")
        if start_btn:
            if total_seconds_input > 0 and not st.session_state.countdown_running:
                st.session_state.countdown_running = True
                st.session_state.countdown_time = total_seconds_input
                st.session_state.countdown_total = total_seconds_input
                st.session_state.countdown_start = time.time()
                st.rerun()
    
    with col2:
        pause_btn = st.button(f"⏸️ {t('pause')}", key="countdown_pause")
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
        reset_btn = st.button(f"⏹️ {t('reset')}", key="countdown_reset")
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
            st.success(t("countdown_complete"))
    
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
