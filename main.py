from telegramBot import sendMessage
from binanceBot import getBalanceUSDT
from time import sleep

while True:
  # Get balance from Binance
  balance = getBalanceUSDT()
  print(balance)
  # Send balance notification
  sendMessage(balance)
  sleep(60)
