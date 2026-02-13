
import json
import sys


def parse_har(file_path):
    """
    Extract API request details from HAR file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        har_data = json.load(f)

    entries = har_data.get("log", {}).get("entries", [])
    extracted_requests = []

    for entry in entries:
        request = entry.get("request", {})
        headers = {h["name"]: h["value"] for h in request.get("headers", [])}

        extracted_requests.append({
            "method": request.get("method"),
            "url": request.get("url"),
            "headers": headers,
            "body": request.get("postData", {}).get("text")
        })

    return extracted_requests


def main():
    if len(sys.argv) != 2:
        print("Usage: python har_parser.py <file.har>")
        sys.exit(1)

    file_path = sys.argv[1]
    requests = parse_har(file_path)

    print(f"Extracted {len(requests)} requests:\n")

    for req in requests[:5]:  # show first 5
        print(f"{req['method']} {req['url']}")


if __name__ == "__main__":
    main()
