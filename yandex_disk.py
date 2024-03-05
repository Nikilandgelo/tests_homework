import requests

def create_folder_yandex_disk(folder_name, api_key) -> int:
    params = {
        "path": folder_name
    }
    headers = {
        "Authorization": api_key
    }
    response = requests.put("https://cloud-api.yandex.net/v1/disk/resources", params=params, headers=headers)

    return response.status_code

def check_exist_folder(folder_name, api_key) -> int:
    params = {
        "path": folder_name
    }
    headers = {
        "Authorization": api_key
    }
    response = requests.get("https://cloud-api.yandex.net/v1/disk/resources", params=params, headers=headers)
    
    return response.status_code