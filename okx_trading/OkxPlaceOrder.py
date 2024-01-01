import asyncio
from concurrent.futures import ThreadPoolExecutor
import okx.Trade as Trade


async def place_order(botalert, apikey, secretkey, passphrase, total_balance, min_slot_play):
    flag = "0"  # Production trading: 0, Demo trading: 1
    print("111111111111111111111111111", apikey)
    print("2222222222222222222222222222", secretkey)
    print("3333333333333333333333333", passphrase)
    trade_api = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

    # Modify the 'side' parameter based on botalert.side
    if botalert.position == "Long":
        side_param = "buy"
    elif botalert.position == "Short":
        side_param = "sell"
    else:
        # Handle the case where botalert.side is neither "Long" nor "Short"
        raise ValueError("Invalid position: {}".format(botalert.position))

    # Calculate 1% of total_balance
    sz = total_balance * 0.01

    def place_order_sync():
        # Synchronous code for placing the order
        return trade_api.place_order(
            instId="NEO-USDT-SWAP",
            tdMode="isolated",
            clOrdId="b15",
            side="buy",
            ordType="limit",
            px="1",
            sz="1"
            # # instId=botalert.ticker,BTC-USDT
            # instId="NEAR-USDT",
            # tdMode="spot_isolated",  # Update with the appropriate value from botalert or use a default
            # # clOrdId=botalert.codename,  # Use a relevant field from botalert
            # clOrdId="oktswap6",  # Use a relevant field from botalert
            # side=side_param,
            # ordType="limit",  # Update with the appropriate value from botalert or use a default
            # # posSide=botalert.position,
            # px=botalert.prices_pos,
            # sz=sz,
            # tpOrdPx=botalert.prices_tp
        )

    try:
        # Use asyncio.get_event_loop().run_in_executor to run the synchronous code in a separate thread
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(ThreadPoolExecutor(), place_order_sync)
        print("resultxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", result)
        return result
    except Exception as e:
        print(f"Failed to place order: {str(e)}")
        return None
