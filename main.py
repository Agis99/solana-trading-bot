import asyncio
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey
from strategies.rsi_ml import RSIMLStrategy

class TradingBot:
    def __init__(self):
        self.client = AsyncClient("https://api.testnet.solana.com")
        self.strategy = RSIMLStrategy()
        self.wallet_address = Pubkey.from_string("YOUR_WALLET_ADDRESS")
        
    async def trade_cycle(self):
        while True:
            try:
                signal = await self.strategy.generate_signal(self.wallet_address, self.client)
                
                if signal == "BUY":
                    print("Executing BUY order")
                    # await self.execute_order("BUY")
                elif signal == "SELL":
                    print("Executing SELL order")
                    # await self.execute_order("SELL")
                    
                await asyncio.sleep(60)  # Check every minute
                
            except Exception as e:
                print(f"Critical error: {str(e)}")
                await asyncio.sleep(300)  # Wait 5 min on errors

if __name__ == "__main__":
    bot = TradingBot()
    asyncio.run(bot.trade_cycle())
