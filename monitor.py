import requests

urls = {
    "Berlin": "https://berlin.pasport.org.ua/solutions/e-queue",
    "Wroclaw": "https://wroclaw.pasport.org.ua/solutions/e-queue"
}

for city, url in urls.items():
    try:
        r = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=20
        )
        print(city, r.status_code, len(r.text))
    except Exception as e:
        print(city, "ERROR", e)
