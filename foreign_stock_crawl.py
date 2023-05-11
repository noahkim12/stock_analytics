import pandas as pd
import yfinance as yf
import os
from datetime import datetime

# 나스닥100 정보 리스트
nasdaq_100_ticker = pd.read_csv('nasdaq_100_ticker.csv')

# 나스닥 티커 리스트
ticker_list = nasdaq_100_ticker['Symbol']

# 파일 생성
directory = 'foreign_stock'
if not os.path.exists(directory):
    os.makedirs(directory)

# 시작 & 종료 날짜 생성. 
# 시작 날짜 : 항상 2015년부터 기준을 잡는다.
# 종료 날짜 : 항상 오늘을 기준으로 한다.     
start_date = '2015-01-01'
end_date = datetime.today().strftime("%Y-%m-%d")

# 나스닥 100 데이터를 야후 파이낸스 모듈을 사용해서 일별 주가 정보를 수집
for ticker_nm in ticker_list:
    print(f'{ticker_nm} 시작')
    raw_stock_df = yf.download(ticker_nm,
                      start=start_date,
                      end=end_date,
                      progress=False)

    raw_stock_df = raw_stock_df.reset_index()

    raw_stock_df.to_csv(f'foreign_stock/{ticker_nm}.csv', index = False)
    
    print(f'{ticker_nm} 완료')