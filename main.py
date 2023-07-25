from routes import RouteScraper
from services.route import RouteService
from services.request import RequestService
from services.trace import UpdateTraceService, json

def main():    
    post_update_traces()
    
def post_update_traces():
    request_service = RequestService("##", "##")
    request_service.post_all_traces()
    
def get_updated_traces():
    update_trace_service = UpdateTraceService()
    
    with open("updated.json", 'w') as file:
        json.dump(update_trace_service.update_route(), file, indent=4, ensure_ascii=False)
    
def get_route_traces():
    request_service = RequestService("##", "##")
    
    with open("traces.json", 'w') as file:
        json.dump(request_service.get_all_route_progress(), file, indent=4, ensure_ascii=False)

def get_routes():
    routes = get_all_routes(["##link", 
                             "##link"])
    
    with open("routes.json", 'w') as file:
        json.dump(routes, file, indent=4, ensure_ascii=False)

def get_all_routes(urls: list[str]):
    routes = []
    for url in urls:
        routes.extend(get_route_data(url))
    return routes 
    
def get_route_data(url: str):
    route_service = RouteService(url)
    route_scraper = RouteScraper(route_service._driver)
    
    route = route_scraper.get_route()
    routes = route_service.get_final_routes(route, route_scraper.get_story_forms())
    route_service._driver.quit()
    
    return routes

main()