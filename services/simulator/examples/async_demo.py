import asyncio
import time

async def run_machine(name: str, interval_seconds: float, messages: int):
    print(f"Starting machine {name} with interval {interval_seconds} seconds and {messages} messages.")
    for i in range(messages):
        await asyncio.sleep(interval_seconds)
        print(f"{time.strftime('%H:%M:%S')} Machine {name} message {i + 1}/{messages}")

async def main():
    await asyncio.gather(
        run_machine("M1", 1.0, 6),
        run_machine("M2", 2.5, 3)
    )
asyncio.run(main())
    