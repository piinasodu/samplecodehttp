import asyncio
import logging
from curl_cffi import requests as curl_requests
import httpx


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class APIClient:
    def __init__(self, base_url, proxy=None):
        self.base_url = base_url
        self.proxy = proxy

    def get_with_tls_impersonation(self, endpoint):
        """
        Uses curl_cffi to mimic Chrome TLS fingerprint.
        """
        url = f"{self.base_url}{endpoint}"

        try:
            response = curl_requests.get(
                url,
                impersonate="chrome120",
                proxies=self.proxy,
                timeout=30
            )
            response.raise_for_status()
            logging.info(f"Success (TLS) - {url}")
            return response.json()
        except Exception as e:
            logging.error(f"TLS Request Failed: {e}")
            return None

    async def async_get(self, endpoint):
        """
        Async request using httpx with HTTP/2 support.
        """
        url = f"{self.base_url}{endpoint}"

        async with httpx.AsyncClient(http2=True, timeout=30) as client:
            try:
                response = await client.get(url)
                response.raise_for_status()
                logging.info(f"Success (Async) - {url}")
                return response.json()
            except Exception as e:
                logging.error(f"Async Request Failed: {e}")
                return None


async def main():
    client = APIClient("https://jsonplaceholder.typicode.com")

    # TLS impersonation request
    client.get_with_tls_impersonation("/posts/1")

    # Async batch requests
    tasks = [
        client.async_get(f"/posts/{i}") for i in range(1, 6)
    ]

    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
