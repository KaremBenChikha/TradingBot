from telegramBot import sendMessage
from binanceBot import getBalanceUSDT
from time import sleep

while True:
  # Get balance from Binance
  balance = getBalanceUSDT()
  # Send balance notification
  sendMessage('Your balance is ' + str(round(balance, 2)) + ' USDT')
  sleep(60)
