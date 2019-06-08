import asyncio
from pprint import pprint

from aioupbit import UpbitRest

UPBIT_API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
UPBIT_API_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


async def get_markets():
    """
    마켓 코드 조회
    https://docs.upbit.com/v1.0/reference#%EB%A7%88%EC%BC%93-%EC%BD%94%EB%93%9C-%EC%A1%B0%ED%9A%8C

    response:
    [{'english_name': 'Bitcoin', 'korean_name': '비트코인', 'market': 'KRW-BTC'},
     {'english_name': 'Dash', 'korean_name': '대시', 'market': 'KRW-DASH'},
     {'english_name': 'Ethereum', 'korean_name': '이더리움', 'market': 'KRW-ETH'},
     ...
     ]
    """

    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.get_markets()
        pprint(response)


async def get_ticker():
    """
    현재가 정보
    https://docs.upbit.com/v1.0/reference#ticker%ED%98%84%EC%9E%AC%EA%B0%80-%EB%82%B4%EC%97%AD

    response:
        [{'acc_trade_price': 69961253970.65402,
          'acc_trade_price_24h': 75647884641.97772,
          'acc_trade_volume': 7265.6396237,
          'acc_trade_volume_24h': 7868.16595002,
          'change': 'RISE',
          'change_price': 216000.0,
          'change_rate': 0.0227488152,
          'high_price': 9821000.0,
          'highest_52_week_date': '2019-05-30',
          'highest_52_week_price': 10815000.0,
          'low_price': 9388000.0,
          'lowest_52_week_date': '2018-12-15',
          'lowest_52_week_price': 3562000.0,
          'market': 'KRW-BTC',
          'opening_price': 9495000.0,
          'prev_closing_price': 9495000.0,
          'signed_change_price': 216000.0,
          'signed_change_rate': 0.0227488152,
          'timestamp': 1559939333689,
          'trade_date': '20190607',
          'trade_date_kst': '20190608',
          'trade_price': 9711000.0,
          'trade_time': '202853',
          'trade_time_kst': '052853',
          'trade_timestamp': 1559939333000,
          'trade_volume': 3.6e-05}]
    """

    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.get_ticker(markets='KRW-BTC')
        pprint(response)


async def get_accounts():
    """
    자산 전체 조회
    https://docs.upbit.com/v1.0/reference#%EC%9E%90%EC%82%B0-%EC%A0%84%EC%B2%B4-%EC%A1%B0%ED%9A%8C

    response:
    [{'avg_buy_price': '9690000',
      'avg_buy_price_modified': False,
      'avg_krw_buy_price': '9690000',
      'balance': '0.1',
      'currency': 'BTC',
      'locked': '0.0',
      'modified': False,
      'unit_currency': 'KRW'}]
    """

    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.get_accounts()
        pprint(response)


async def get_order_chance():
    """
    주문 가능 정보
    https://docs.upbit.com/v1.0/reference#%EC%9E%90%EC%82%B0-%EC%A0%84%EC%B2%B4-%EC%A1%B0%ED%9A%8C

    response:
    {'ask_account': {'avg_buy_price': '9690000',
                     'avg_buy_price_modified': False,
                     'avg_krw_buy_price': '9690000',
                     'balance': '0.1',
                     'currency': 'BTC',
                     'locked': '0.0',
                     'modified': False,
                     'unit_currency': 'KRW'},
     'ask_fee': '0.0005',
     'bid_account': {'avg_buy_price': '0',
                     'avg_buy_price_modified': True,
                     'avg_krw_buy_price': '0',
                     'balance': '0.0',
                     'currency': 'KRW',
                     'locked': '0.0',
                     'modified': True,
                     'unit_currency': 'KRW'},
     'bid_fee': '0.0005',
     'market': {'ask': {'currency': 'BTC', 'min_total': 1000, 'price_unit': None},
                'bid': {'currency': 'KRW', 'min_total': 1000, 'price_unit': None},
                'id': 'KRW-BTC',
                'max_total': '1000000000.0',
                'name': 'BTC/KRW',
                'order_sides': ['ask', 'bid'],
                'order_types': ['limit'],
                'state': 'active'}}
    """

    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.get_order_chance(market='KRW-BTC')
        pprint(response)


async def get_order_list():
    """
    주문 리스트 조회
    https://docs.upbit.com/v1.0/reference#%EC%A3%BC%EB%AC%B8-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A1%B0%ED%9A%8C

    response:
    [
        {
            "uuid": "a08f09b1-1718-42e2-9358-f0e5e083d3ee",
            "side": "bid",
            "ord_type": "limit",
            "price": "17417000.0",
            "state": "done",
            "market": "KRW-BTC",
            "created_at": "2018-04-05T14:09:14+09:00",
            "volume": "1.0",
            "remaining_volume": "0.0",
            "reserved_fee": "26125.5",
            "remaining_fee": "25974.0",
            "paid_fee": "151.5",
            "locked": "17341974.0",
            "executed_volume": "1.0",
            "trades_count": 2
        }
        # ....
    ]
    """

    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.get_order_list(market='KRW-BTC')
        pprint(response)


async def get_order():
    """
    개별 주문 조회
    https://docs.upbit.com/v1.0/reference#%EA%B0%9C%EB%B3%84-%EC%A3%BC%EB%AC%B8-%EC%A1%B0%ED%9A%8C

    response:
    [{'created_at': '2019-06-08T06:28:16+09:00',
      'executed_volume': '0.0',
      'locked': '0.01',
      'market': 'KRW-BTC',
      'ord_type': 'limit',
      'paid_fee': '0.0',
      'price': '10652000.0',
      'remaining_fee': '0.0',
      'remaining_volume': '0.01',
      'reserved_fee': '0.0',
      'side': 'ask',
      'state': 'wait',
      'trades_count': 0,
      'uuid': 'da9bdff3-2d0e-413c-8dcc-a543d81c0411',
      'volume': '0.01'}]
    """
    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.get_order(uuid='da9bdff3-2d0e-413c-8dcc-a543d81c0411')
        pprint(response)


async def place_order():
    """
    주문하기
    https://docs.upbit.com/v1.0/reference#%EC%A3%BC%EB%AC%B8%ED%95%98%EA%B8%B0-1

    response:
    {
        "uuid": "cdd92199-2897-4e14-9448-f923320408ad",
        "side": "bid",
        "ord_type": "limit",
        "price": "100.0",
        "avg_price": "0.0",
        "state": "wait",
        "market": "KRW-BTC",
        "created_at": "2018-04-10T15:42:23+09:00",
        "volume": "0.01",
        "remaining_volume": "0.01",
        "reserved_fee": "0.0015",
        "remaining_fee": "0.0015",
        "paid_fee": "0.0",
        "locked": "1.0015",
        "executed_volume": "0.0",
        "trades_count": 0
    }
    """

    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.place_order(market='KRW-BTC',
                                           side='ask',
                                           volume='0.01',
                                           price='11000000.0',
                                           ord_type='limit')
        pprint(response)


async def cancel_order():
    """
    주문 취소 접수
    https://docs.upbit.com/v1.0/reference#%EC%A3%BC%EB%AC%B8-%EC%B7%A8%EC%86%8C

    response:
    {'created_at': '2019-06-08T07:19:54+09:00',
     'executed_volume': '0.0',
     'locked': '0.01',
     'market': 'KRW-BTC',
     'ord_type': 'limit',
     'paid_fee': '0.0',
     'price': '11000000.0',
     'remaining_fee': '0.0',
     'remaining_volume': '0.01',
     'reserved_fee': '0.0',
     'side': 'ask',
     'state': 'wait',
     'trades_count': 0,
     'uuid': '71386569-051e-4f8b-ac8c-c7600b46a88a',
     'volume': '0.01'}
    """
    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.cancel_order(uuid='f7c703bc-6374-4dd1-966c-ab61ed61dd7a')
        pprint(response)


async def get_withdraw_list():
    """
    출금 리스트 조회
    https://docs.upbit.com/v1.0/reference#%EC%A0%84%EC%B2%B4-%EC%B6%9C%EA%B8%88-%EC%A1%B0%ED%9A%8C

    response:
    [
        {
            "type": "withdraw",
            "uuid": "9f432943-54e0-40b7-825f-b6fec8b42b79",
            "currency": "BTC",
            "txid": null,
            "state": "processing",
            "created_at": "2018-04-13T11:24:01+09:00",
            "done_at": null,
            "amount": "0.01",
            "fee": "0.0",
            "krw_amount": "80420.0"
        }
        # ....
    ]
    """
    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.get_withdraw_list(currency='BTC',
                                                 state='submitting',
                                                 limit=100)
        pprint(response)


async def get_withdraw():
    """
    개별 출금 조회
    https://docs.upbit.com/v1.0/reference#%EA%B0%9C%EB%B3%84-%EC%B6%9C%EA%B8%88-%EC%A1%B0%ED%9A%8C

    response:
    {
        "type": "withdraw",
        "uuid": "9f432943-54e0-40b7-825f-b6fec8b42b79",
        "currency": "BTC",
        "txid": null,
        "state": "processing",
        "created_at": "2018-04-13T11:24:01+09:00",
        "done_at": null,
        "amount": "0.01",
        "fee": "0.0",
        "krw_amount": "80420.0"
    }
    """

    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.get_withdraw(uuid='9f432943-54e0-40b7-825f-b6fec8b42b79')
        pprint(response)


async def get_withdraw_chance():
    """
    출금 가능 정보
    https://docs.upbit.com/v1.0/reference#%EC%B6%9C%EA%B8%88-%EA%B0%80%EB%8A%A5-%EC%A0%95%EB%B3%B4

    response:
    {
        "member_level": {
            "security_level": 3,
            "fee_level": 0,
            "email_verified": true,
            "identity_auth_verified": true,
            "bank_account_verified": true,
            "kakao_pay_auth_verified": false,
            "locked": false,
            "wallet_locked": false
        },
        "currency": {
            "code": "BTC",
            "withdraw_fee": "0.0005",
            "is_coin": true,
            "wallet_state": "working",
            "wallet_support": [
                "deposit",
                "withdraw"
            ]
        },
        "account": {
            "currency": "BTC",
            "balance": "10.0",
            "locked": "0.0",
            "avg_krw_buy_price": "8042000",
            "modified": false
        },
        "withdraw_limit": {
            "currency": "BTC",
            "minimum": null,
            "onetime": null,
            "daily": "10.0",
            "remaining_daily": "10.0",
            "remaining_daily_krw": "0.0",
            "fixed": null,
            "can_withdraw": true
        }
    }
    """

    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.get_withdraw_chance(currency='BTC')
        pprint(response)


async def withdraw_crypto():
    """
    코인 출금하기
    https://docs.upbit.com/v1.0/reference#%EC%BD%94%EC%9D%B8-%EC%B6%9C%EA%B8%88%ED%95%98%EA%B8%B0

    response:
    {
        "type": "withdraw",
        "uuid": "9f432943-54e0-40b7-825f-b6fec8b42b79",
        "currency": "BTC",
        "txid": "ebe6937b-130e-4066-8ac6-4b0e67f28adc",
        "state": "processing",
        "created_at": "2018-04-13T11:24:01+09:00",
        "done_at": null,
        "amount": "0.01",
        "fee": "0.0",
        "krw_amount": "80420.0"
    }
    """
    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.withdraw_crypto(currency='BTC',
                                               amount='0.001',
                                               address='3LRkBfN3XYTmKWkddE2ZNdLis5mGJmzken')
        pprint(response)


async def withdraw_krw():
    """
    원화 출금하기
    https://docs.upbit.com/v1.0/reference#%EC%9B%90%ED%99%94-%EC%B6%9C%EA%B8%88%ED%95%98%EA%B8%B0

    response:
    {
        "type": "withdraw",
        "uuid": "9f432943-54e0-40b7-825f-b6fec8b42b79",
        "currency": "KRW",
        "txid": "ebe6937b-130e-4066-8ac6-4b0e67f28adc",
        "state": "processing",
        "created_at": "2018-04-13T11:24:01+09:00",
        "done_at": null,
        "amount": "10000",
        "fee": "0.0",
        "krw_amount": "10000"
    }
    """
    async with UpbitRest(access_key=UPBIT_API_KEY, secret_key=UPBIT_API_SECRET) as upbit:
        response = await upbit.withdraw_krw(amount='1000')
        pprint(response)


asyncio.get_event_loop().run_until_complete(withdraw_krw())
