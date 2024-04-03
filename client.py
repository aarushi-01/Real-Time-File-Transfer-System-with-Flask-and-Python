import requests
import time

def send_file_via_http(local_path, server_url):
    try:
        files = {'file': open(local_path, 'rb')}
        response = requests.post(server_url, files=files)
        if response.status_code == 200:
            print('File transferred successfully:', local_path)
        else:
            print('Error transferring file:', response.text)
    except Exception as e:
        print('Error transferring file:', str(e))

def main():
    server_url = "http://192.171.0.128:5000/uploads"  # Replace with the actual server URL
    local_path = r"C:\Users\Aditi\PycharmProjects\pythonProject\my.txt"  # Replace with the actual local file path

    while True:
        send_file_via_http(local_path, server_url)
        time.sleep(60)  # Sleep for 15 minutes

if __name__ == "__main__":
    main()
