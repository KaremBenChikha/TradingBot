from os import getenv
from binance.um_futures import UMFutures
from binance.error import ClientError
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_KEY = getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = getenv('BINANCE_API_SECRET')

BinanceClient = UMFutures(key = BINANCE_API_KEY, secret = BINANCE_API_SECRET)

# error Handler
def errorMessage(error):
    print("Found error. status: {}, error code: {}, error message: {}".format(error.status_code, error.error_code, error.error_message))

# getting your futures balance in USDT
def getBalanceUSDT():
    try:
        response = BinanceClient.balance(recvWindow=6000)
        for elem in response:
            if elem['asset'] == 'USDT':
                return float(elem['balance'])
        return response
    except ClientError as error:
        errorMessage(error)
