import asyncio
import os
from rustplus import RustError, RustSocket, ServerDetails

async def main():
    server_ip = os.environ["SERVER_IP"]
    server_port = os.environ["SERVER_PORT"]
    steam_id = os.environ["STEAM_ID"]
    player_token = os.environ["PLAYER_TOKEN"]

    server_details = ServerDetails(
        server_ip,
        server_port,
        steam_id,
        player_token
    )

    socket = RustSocket(server_details)

    try:
        connected = await socket.connect()
        print("WebSocket connected:", connected)

        for name, method in [
            ("Server Info", socket.get_info),
            ("Server Time", socket.get_time)
        ]:
            result = await method()

            if isinstance(result, RustError):
                print(f"{name} error: {result.reason}")
            else:
                print(f"{name}: {result}")

    finally:
        await socket.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
