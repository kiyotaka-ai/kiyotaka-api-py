import asyncio
import tharamine
import tharamine.api
import time

from grpclib.client import Channel

async def main():
    metadata = {
        'x-tharamine-key': 'YOUR_API_KEY_HERE'
    }

    channel = Channel(
        host="grpc.api.tharamine.com",
        port=443,
        ssl=True,
    )
    service = tharamine.api.ApiStub(channel)

    from_ = int(time.time()) - 60*60

    data_request = tharamine.api.PointRequest(
        type=[tharamine.api.PointType.TRADE_AGG],
        exchange=[tharamine.api.PointExchange.BINANCE],
        coin=["BTC"],
        interval=tharamine.api.PointAggregationInterval.MINUTE,
        from_=from_,
    )

    stream = service.stream_points(data_request, timeout=3600, metadata=metadata)
    async for response in stream:
        print(response.to_json())

    channel.close()

if __name__ == "__main__":
    asyncio.run(main())
