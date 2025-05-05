from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# 載入農曆資料
LUNAR_DATA_PATH = 'lunar_data_1910_2030_立春切歲22.json'

def load_lunar_data():
    with open(LUNAR_DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

# 全域變數儲存農曆資料
lunar_data = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    global lunar_data
    
    try:
        # 確保資料已載入
        if lunar_data is None:
            lunar_data = load_lunar_data()
        
        date_str = request.json.get('date')
        solar_date = datetime.strptime(date_str, '%Y-%m-%d')
        
        # 格式化日期為查詢用的鍵值（YYYY-MM-DD格式）
        date_key = solar_date.strftime('%Y-%m-%d')
        
        # 查詢農曆資料
        if date_key not in lunar_data:
            return jsonify({
                'success': False,
                'error': '找不到此日期的農曆資料'
            })
            
        lunar_info = lunar_data[date_key]
        
        # 準備回應資料
        result = {
            'success': True,
            'lunar_date': {
                'year': lunar_info['lunar_year'],
                'month': lunar_info['lunar_month'],
                'day': lunar_info['lunar_day'],
                'solar_year': lunar_info['lunar_solar_year'],
                'chinese_year': f"農曆{lunar_info['lunar_year']}年",
                'zodiac': lunar_info['zodiac'],
                'gz_year': lunar_info['gan_zhi_year'],
                'lichun_time': lunar_info['lichun_time'],
                'is_after_lichun': lunar_info['is_after_lichun']
            }
        }
        return jsonify(result)
    
    except FileNotFoundError:
        return jsonify({
            'success': False,
            'error': '農曆資料檔案不存在'
        })
    except json.JSONDecodeError:
        return jsonify({
            'success': False,
            'error': '農曆資料檔案格式錯誤'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True) 