import okx.Trade as Trade


def place_order(botalert):
    apikey = "3b906b00-776e-4ff0-8c30-738e97c8caab"
    secretkey = "71FB64F6B47AAC190ECBB85D61B9A159"
    passphrase = "Tk115@utehy"

    flag = "0"  # Production trading: 0, Demo trading: 1
    trade_api = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

    # Simple mode, limit order
    result = trade_api.place_order(
        # Demo trading
        # instId="BTC-USDT",
        # tdMode="cash",
        # clOrdId="b15",
        # side="buy",
        # ordType="limit",
        # px="2.15",
        # sz="2"

        # Production
        instId=botalert.ticker,
        tdMode="cash",  # Update with the appropriate value from botalert or use a default
        clOrdId=botalert.codename,  # Use a relevant field from botalert
        side=botalert.side,
        ordType="limit",  # Update with the appropriate value from botalert or use a default
        px=botalert.prices_pos,
        sz=botalert.pos_quantity
    )

    return result
