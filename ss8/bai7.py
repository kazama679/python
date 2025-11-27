# bài 8
from pathlib import Path
import json
import pandas as pd
import re

# Thay đổi đường dẫn này tới thư mục logs của bạn
logs_dir = Path('/logs')
if not logs_dir.exists():
    print('Thư mục logs/ không tồn tại. Vui lòng tạo và thêm các file JSON.')
else:
    records = []
    date_re = re.compile(r"\d{4}-\d{2}-\d{2}")
    for p in sorted(logs_dir.glob('*.json')):
        m = date_re.search(p.stem)
        if not m:
            continue
        date_str = m.group(0)
        try:
            payload = json.loads(p.read_text(encoding='utf-8'))
        except Exception as e:
            print(f"Bỏ qua file không đọc được: {p.name} -> {e}")
            continue
        user = payload.get('user')
        action = payload.get('action')
        duration = payload.get('duration')
        try:
            duration = float(duration) if duration is not None else 0.0
        except Exception:
            print(f"duration không hợp lệ trong {p.name}, đặt về 0")
            duration = 0.0
        records.append({'date': pd.to_datetime(date_str).date(),
                        'user': user, 'action': action, 'duration': duration,
                        'source_file': p.name})

    if not records:
        print('Không tìm thấy record log hợp lệ trong logs/.')
    else:
        df_logs = pd.DataFrame.from_records(records)
        summary = df_logs.groupby('date', as_index=False)['duration'].sum()
        summary = summary.sort_values('date')
        for _, row in summary.iterrows():
            print(f"Date: {row['date']}, Total Duration: {row['duration']}")
        out_file = Path('daily_report.csv')
        summary.to_csv(out_file, index=False)
        print(f"Saved daily report to: {out_file.resolve()}")
