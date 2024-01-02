import asyncio
import math
from concurrent.futures import ThreadPoolExecutor
import okx.Trade as Trade
import okx.Account as Account


async def place_order(botalert, apikey, secretkey, passphrase, total_balance, min_slot_play):
    flag = "0"  # Production trading: 0, Demo trading: 1
    trade_api = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

    # Modify the 'side' parameter based on botalert.side
    if botalert.position == "Long":
        side_param = "buy"
    elif botalert.position == "Short":
        side_param = "sell"
    else:
        # Handle the case where botalert.side is neither "Long" nor "Short"
        raise ValueError("Invalid position: {}".format(botalert.position))

    instid_param = botalert.basecurrency + "-" + botalert.currency + "-" + "SWAP"
    # Calculate 1% of total_balance
    # sz = total_balance * 0.01
    precent_tp = botalert.precent_tp
    prices_pos = botalert.prices_pos
    if precent_tp != "":
        # Convert tpTriggerPx to float (assuming it's a numeric value)
        prices_px = float(prices_pos)
        # Convert precent_tp to float (assuming it's a numeric value)
        precent_tp_value = float(precent_tp)
        # Calculate the increased value
        take_profit = prices_px * (1 + precent_tp_value / 100)
    else:
        take_profit = botalert.prices_tp

    # Set leverage for MARGIN instruments under isolated-margin trade mode at pairs level.(đòn bẩy)
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    result = accountAPI.set_leverage(
        instId=instid_param,
        lever=botalert.pos_leverage,
        mgnMode="isolated"
    )
    print(result)

    result_account_balance = accountAPI.get_account_balance()
    avail_eq = result_account_balance['data'][0]['details'][0]['availEq']
    sz = float(avail_eq) * 0.01

    def place_order_sync():
        # Synchronous code for placing the order
        return trade_api.place_order(
            instId=instid_param,
            tdMode="isolated",
            clOrdId="okxdca",
            side=side_param,
            ordType="limit",
            px=botalert.prices_pos,
            sz="1",
            tpTriggerPx=take_profit,
            tpOrdPx=take_profit
        )

    try:
        # Use asyncio.get_event_loop().run_in_executor to run the synchronous code in a separate thread
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(ThreadPoolExecutor(), place_order_sync)
        return result
    except Exception as e:
        print(f"Failed to place order: {str(e)}")
        return None
