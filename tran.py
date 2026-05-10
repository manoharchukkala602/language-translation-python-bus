import urllib.request
import urllib.parse
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def translation(text):
    try:
        base_url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=hi&dt=t&q="
        text = urllib.parse.quote(text)
        url = base_url + text

        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0"
        })

        with urllib.request.urlopen(base_url, timeout=10) as resp:
            data = json.loads(resp.read())
            return data[0][0][0]

    except Exception as e:
        return "Network error: " + str(e)

while True:
    text = input("Enter your text: ")
    if text.lower() == "exit":
        print("Thank you!")
        break

    hindi = translation(text)
    print("Hindi translation:", hindi)