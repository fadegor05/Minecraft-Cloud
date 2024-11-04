import http.client
import json
from typing import List, Dict, Union
from urllib.parse import quote


class ApiClient:
    BASE_URL = "localhost:8000"
    API_KEY = "123"

    def get_paths(self) -> List[str]:
        connection = http.client.HTTPConnection(self.BASE_URL)
        headers = {"Content-Type": "application/json", "Authorization": self.API_KEY}
        connection.request("GET", "/api/v1/paths", headers=headers)

        response = connection.getresponse()

        if response.status != 200:
            raise Exception(f"API request failed with status {response.status}")

        data = response.read().decode("utf-8")
        return json.loads(data)["paths"]

    def post_client_sync(self, instance_name: str, instance_hash: str, instance_hash_tree: Dict) -> Union[Dict, None]:
        connection = http.client.HTTPConnection(self.BASE_URL)
        content = {
            "client_hash": instance_hash,
            "client_hash_tree": instance_hash_tree
        }
        body = json.dumps(content)
        headers = {"Content-Type": "application/json", "Authorization": self.API_KEY}
        connection.request("POST", f"/api/v1/sync/client/{instance_name}", body=body, headers=headers)

        response = connection.getresponse()

        if response.status == 404:
            return None

        if response.status != 200:
            raise Exception(f"API request failed with status {response.status}")

        data = response.read().decode("utf-8")
        return json.loads(data)

    def get_download_file(self, instance_name: str, file_path: str, local_file_path: str):
        connection = http.client.HTTPConnection(self.BASE_URL)
        headers = {"Content-Type": "application/json", "Authorization": self.API_KEY}
        connection.request("GET", quote(f"/api/v1/files/{instance_name}{file_path}"), headers=headers)

        response = connection.getresponse()

        if response.status == 200:
            with open(local_file_path, 'wb') as file:
                while chunk := response.read(1024):
                    file.write(chunk)

        connection.close()
