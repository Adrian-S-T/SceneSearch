import json
def load_database():
    with open("scenes.json","r") as file:
        scenes=json.load(file)
    return scenes
def save_database(scenes):
     """updates the json with the current database"""    
     with open("scenes.json","w") as f:
      json.dump(scenes,f,indent=4)

def add_scene(scenes):
     """adds a scene from keyboard in the scenes list"""
     anime=input("Anime name=")
     ep=input("Episode name=")
     timestamp=input("Timestamp=")
     description=input("Description=")
     new_scene={
          "anime":anime,
          "episode":ep,
          "timestamp":timestamp,
          "description":description,
    }
     scenes.append(new_scene)
     save_database(scenes)