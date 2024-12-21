from playwright.sync_api import sync_playwright
import json

def send_message(message: str, chat_id: str):

    pw = sync_playwright().start()
    browser =  pw.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()
    page =  context.new_page()
    page.goto(r"https://web.rubika.ir")

    with open('local_storage.json', 'r') as file:
            local_storage = json.load(file)

    # Set localStorage keys and values
    for key, value in local_storage.items():
        page.evaluate(f"localStorage.setItem('{key}', '{value}')")
    #rubika has a difrent key for ech auth and it did not copy so i had to manuly copy and past it
    page.evaluate(f'localStorage.setItem("key", "eyJ2ZXJzaW9uIjoiNiIsImQiOiItLS0tLUJFR0lOIFJTQSBQUklWQVRFIEtFWS0tLS0tXG5NSUlDWEFJQkFBS0JnUUNtUm5ZT25xb0hOczJDS2JuNTkzSUYvVi9HN2VEYWN2TTNSU2RuRVNibWgwL056L2diXG5EUkgxSFJLVXAxdUtQcU9FQnV0a2p2YTVCM2lHVEkvRlRlMXRTdEFUdE81MVh1YXJRcm9qczFzbnZ1Zjd0bUQrXG4xK093L2ExSk54YTlVZ0RZQ0pNa0Q1S1NqbGNrSVFXY2xmRk11RUdZb2ptRFRKZmpPT1BFS3l2RTJ3SURBUUFCXG5Bb0dBU25tQTQyZDVyS1dGUXVuQm5RNlNDZERGRjJyd3JhZVMvSXlDNjQwcEtWUXVFSGM0SDVXcEYycWdLZWtUXG4vVVcxSTZ1ZHYzcXhVNHJmRnZndjVTWFVVOGhVSHZ3NEhwNXhYUlhCL0Y0bzVGM280Z3JScUJnTHZIYUFCRjlHXG5rdStMVUhXK0hpNjFRRElCbGhmb3kwb1VFTTBOK0tYUEhHaDhibituMHcydXNKRUNRUURjbmNSbEpUVDZmL2VzXG5rWCszQjZZcXpIWXhpdVZocm5pWitSdHdrNlVWWU13RFdHSVpyWHdMTTF5alhqVmRVVTdhTTdJTlpCM1hCL1lMXG5KM3Zqb3pMOUFrRUF3UEdFajFZSndoVnN1ZkRnWjRQcjJPT012aG9VMTVibzhCd2NEMjRPdGxvK05jUXJITmt2XG5ONHdEYU0xOGxKR1lHWGtzVmJySERWclhVcDkvRmxrNnR3SkFlbGRIRE93SUtBNEUwLzdQdXprVHJkSTZqUmpBXG5RVjRXWlJSZVloeU9SSCtzUXdLbFRDWUhqdEtKd2RMQmR5RmF2K2hCQ2VvR0hqTzgvc3lEaUdYOUpRSkFaZmQ5XG5zZTZyYTRtOUV5dHN2T2dvSFZCc2tnN2drdXNySWJJSlZsSTRya0JVL2o4MDlhTUY1Qm8zdHd4WjJYNTBYb24rXG5WelJGZkJaVkUxSTliTWN0VXdKQkFJWllLYnhoOVVxWWFLaEZrWDh5ZVppVXd6NWhNZWZ1OGJ6SExVenF4ekNnXG5RMGUyVkNKL0JiRUdOQXBwTU9wTDhUNTJFL0xONzBuNHRXME9IS1N4NEg4PVxuLS0tLS1FTkQgUlNBIFBSSVZBVEUgS0VZLS0tLS0ifQ==")')

    # Reload the page to apply changes
    page.goto(f"https://web.rubika.ir/#c={chat_id}")

    message_holder = page.get_by_placeholder("پیام بنویسید...")
    message_holder.fill(message)
    page.wait_for_timeout(20_000)
    message_holder.press("Enter")
    page.wait_for_timeout(5_000)
    browser.close()
    pw.stop()


if __name__ == "__main__":
     send_message("hello world \n I finally did it", "u0M9dx041320c11ccae5f04e420d7b8f")

#u0M9dx041320c11ccae5f04e420d7b8f
