import okx.Trade as Trade


def place_order(botalert, apikey, secretkey, passphrase, total_balance, min_slot_play):
    flag = "1"  # Production trading: 0, Demo trading: 1
    trade_api = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

    # Simple mode, limit order
    result = trade_api.place_order(
        # Demo trading
        instId="BTC-USDT",
        tdMode="spot_isolated",
        clOrdId="b15",
        side="buy", # lấy từ Position , nếu position là Long thì => Buy, còn Short là sell
        ordType="limit",
        px="2.15",
        ordType="market",
        posSide="", # lấy từ position = botalert['position']
        sz="min_slot_play",  # 1% của tổng balance hiện có, nên phải get được current balance hiện có.
        tpOrdPx=botalert['prices_tp'], 
        # Production
        # instId=botalert.ticker,
        # tdMode="cash",  # Update with the appropriate value from botalert or use a default
        # clOrdId=botalert.codename,  # Use a relevant field from botalert
        # side=botalert.side,
        # ordType="limit",  # Update with the appropriate value from botalert or use a default
        # px=botalert.prices_pos,
        # sz=botalert.pos_quantity
    )
    print("result", result)
    return result
