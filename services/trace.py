import json

class UpdateTraceService():
    _trace_data: list[list[dict]]
    _route_data: list[dict]
    
    def __init__(self) -> None:
        with open("traces.json") as file:
            self._trace_data = json.load(file)
        with open("routes.json") as file:
            self._route_data = json.load(file)
    
    def update_route(self):
        routes = []
        for user_traces in self._trace_data:
            for trace in user_traces:
                for route in self._route_data:
                    if trace["name"] == route["name"]:
                        trace["userStories"] = self.update_user_story(route["userStories"], trace["userStories"])
                        routes.append(trace)
        
        return routes
                    
    def update_user_story(self, route_stories: list[dict], trace_stories: list[dict]):
        stories = []
        for user_story in trace_stories:
            for story in route_stories:
                if user_story["name"] == story["name"] and user_story["endDate"] is not None:
                    user_story["knowledge"] = self.update_knowledge(story["knowledge"])
                    stories.append(user_story)
                    
        return stories
                
    def update_knowledge(self, story_knowledge: list[dict]):
        return [ { "name": knowledge["name"], "completed": True} for knowledge in story_knowledge ]