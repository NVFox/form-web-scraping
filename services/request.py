import requests
import csv
import json

class RequestService():
    _url: str
    _api_key: str
    
    def __init__(self, url: str, api_key: str) -> None:
        self._url = url
        self._api_key = api_key
    
    def get_all_route_progress(self):
        routes = []
        
        with open("emails.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                user_routes = self.get_route_progress(row)
                for route in user_routes:
                    route["userEmail"] = row[0]
                
                routes.append(user_routes)
        
        return routes
                
    def get_route_progress(self, email) -> list[dict]:
        return requests.get(self._url, 
                     params={"userEmail": email}, 
                     headers={"Content-Type": "application/json", "x-api-key": self._api_key}).json()
        
    def post_all_traces(self):
        with open("updated.json") as file:
            traces: list = json.load(file)
            for trace in traces:
                self.post_update_traces(trace)
        
    def post_update_traces(self, updated: dict):
        requests.post(self._url,
                      json=updated,
                      headers={"Content-Type": "application/json", "x-api-key": self._api_key})