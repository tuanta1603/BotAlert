import okx.Trade as Trade


def place_order(botalert, apikey, secretkey, passphrase, total_balance, min_slot_play):
    flag = "0"  # Production trading: 0, Demo trading: 1
    trade_api = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    # Modify the 'side' parameter based on botalert.side
    if botalert.position == "Long":
        side_param = "buy"
    elif botalert.position == "Short":
        side_param = "sell"
    else:
        # Handle the case where botalert.side is neither "Long" nor "Short"
        side_param = ""  # Set a default value or raise an error, depending on your needs
    # Calculate 1% of total_balance
    sz = total_balance * 0.01

    # Simple mode, limit order
    result = trade_api.place_order(
        # Production
        instId=botalert.ticker,
        tdMode="spot_isolated",  # Update with the appropriate value from botalert or use a default
        clOrdId=botalert.codename,  # Use a relevant field from botalert
        side=side_param,
        ordType="market",  # Update with the appropriate value from botalert or use a default
        posSide=botalert.position,
        px=botalert.prices_pos,
        sz=sz,
        tpOrdPx=botalert.prices_tp
    )
    print("result", result)
    return result
