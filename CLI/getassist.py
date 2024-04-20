import requests

def send_whatsapp_message(phone_number, message, api_key):
    url = f"https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={message}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
def pinghelp():
    phone_number = "+447548960902"
    message = "Assistance needed at Self Service"
    api_key = "6475318"
    send_whatsapp_message(phone_number, message, api_key)
