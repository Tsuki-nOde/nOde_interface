
import json
import random
import requests
import re

# --- Load Intents and Responses ---
with open("./JSON_LOUNGE/intent.JSON", "r", encoding="utf-8") as f:
    intentions = json.load(f)["intents"]

with open("./JSON_LOUNGE/intent_response.json", "r", encoding="utf-8") as f:
    response_data = json.load(f)["responses"]

# --- Geo Lookup Function ---
def geo_lookup(ip):
    url = f"https://ipinfo.io/{ip}/json"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return {
            "ip": ip,
            "city": data.get("city", "Unknown"),
            "region": data.get("region", "Unknown"),
            "country": data.get("country", "Unknown"),
            "org": data.get("org", "Unknown ISP"),
            "timezone": data.get("timezone", "Unknown")
        }
    return None

# --- Intent Matcher ---
def waguri_response(user_input: str):
    for intent in intentions:
        tag = intent["tag"]
        for pattern in intent["patterns"]:
            ip_pattern = r"(\d{1,3}(?:\.\d{1,3}){3})"
            regex = pattern.replace("{ip}", ip_pattern)
            match = re.match(regex, user_input.strip().lower())
            if match:
                ip = match.group(1)
                info = geo_lookup(ip)
                if info:
                    info.update({k.lower(): v for k, v in info.items()})
                    templates = response_data[tag]
                    response = random.choice(templates).format(**info)
                    return {"tag": tag, "response": response}
                else:
                    return {"tag": tag, "response": f"Could not trace {ip}."}
    
    # --- Fallback: raw IP detection ---
    fallback_ip = re.search(r"\b(\d{1,3}(?:\.\d{1,3}){3})\b", user_input)
    if fallback_ip:
        ip = fallback_ip.group(1)
        info = geo_lookup(ip)
        if info:
            info.update({k.lower(): v for k, v in info.items()})
            templates = response_data.get("IP_address", [
                "🌙 Tsuki, I caught {ip}: {city}, {country}, via {org}."
            ])
            response = random.choice(templates).format(**info)
            return {"tag": "IP_address", "response": response}

    return {"tag": "unknown", "response": "🌙 Tsuki, I don’t understand that command."}
