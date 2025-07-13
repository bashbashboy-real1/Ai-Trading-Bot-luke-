import alpaca_trade_api as trade_api    
import json
DATA_FILE= "equities.json"
BASE_URL="https://paper-api.alpaca.markets/"
key="PKRKD7RSGB6KN5J416F2"
secret_key= "4DmEIXHe1bm3N3aVOKF268lfdQyI5IaxmDiSgujI"
api= trade_api.REST(key,secret_key,BASE_URL, api_version="v2")



def get_data(symbol):
    try:
        barset=api.get_latest_trade(symbol)
        return{"price": barset.price}
    except Exception as e:
        return- {"price":-1}
    
get_data("AAPL")

