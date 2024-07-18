import pandas as pd

# 주어진 JSON 데이터
data = {
    "summaries": [
        {
            "local_code": "1100000000",
            "local_category": "광역",
            "local_metro_name": "서울특별시",
            "local_basic_name": "서울",
            "longitude": 126.9783882,
            "latitude": 37.5666103,
            "year": 2023,
            "index": 0.29,
            "status": "축소",
            "rank": 182,
            "reverse_rank": 3,
            "name": "서울페이",
            "benefits": "1인당 최대 월 50만 원까지 구매 금액의 7% 할인 또는 적립",
            "start_date": "2022-07-14",
            "end_date": "발행중",
            "issue_type": "모바일",
            "period": "연중",
            "target": "보편",
            "operators": "신한컨소시엄",
            "plan": "축소",
            "url": "https://seoulpay.shinhancard.com",
            "note": "이용자수는 산하 기초단체 합산한 수치임",
            "statistics": [
                {
                    "period": "2019",
                    "exchange_amount_max": None,
                    "cashback_rate_max": None,
                    "issue_amount": None,
                    "number_of_users": None,
                    "number_of_stores": None
                },
                {
                    "period": "2020",
                    "exchange_amount_max": None,
                    "cashback_rate_max": None,
                    "issue_amount": 870,
                    "number_of_users": None,
                    "number_of_stores": None
                },
                {
                    "period": "2021",
                    "exchange_amount_max": None,
                    "cashback_rate_max": None,
                    "issue_amount": None,
                    "number_of_users": 1,
                    "number_of_stores": None
                },
                {
                    "period": "2022",
                    "exchange_amount_max": 40.0,
                    "cashback_rate_max": 7.0,
                    "issue_amount": 1,
                    "number_of_users": 1,
                    "number_of_stores": 273
                },
                {
                    "period": "2023",
                    "exchange_amount_max": 50.0,
                    "cashback_rate_max": 7.0,
                    "issue_amount": 500,
                    "number_of_users": 1,
                    "number_of_stores": 269
                }
            ]
        }
    ]
}

# summaries 데이터를 데이터프레임으로 변환
summaries_list = data['summaries']
main_data = []
statistics_data = []

for summary in summaries_list:
    main = {key: summary[key] for key in summary if key != 'statistics'}
    for stat in summary['statistics']:
        combined_data = {**main, **stat}
        statistics_data.append(combined_data)

# 데이터프레임 생성
df = pd.DataFrame(statistics_data)

print(df)
