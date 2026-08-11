import json
from pathlib import Path
from scene import Scene
from text_processing import process_text
DATABASE_PATH = Path(__file__).parent.parent / "data" / "scenes.json"
def load_database():
    with open(DATABASE_PATH,"r") as file:
        scenes=json.load(file)
        newscenes=[]
        for element in scenes:
            title_words=process_text(element["anime"])
            desc_words=process_text(element["description"])
            scene = Scene(
            element["anime"],
            element["episode"],
            element["timestamp"],
            element["description"],
            title_words,
            desc_words
            )
            newscenes.append(scene)
    return newscenes
def save_database(scenes):
     export=[]
     for element in scenes:
         newelem=element.to_dict()
         export.append(newelem)
     """updates the json with the current database"""    
     with open(DATABASE_PATH,"w") as f:
      json.dump(export,f,indent=4)

def add_scene(scenes):
     """adds a scene from keyboard in the scenes list"""
     anime=input("Anime name=")
     ep=input("Episode name=")
     timestamp=input("Timestamp=")
     description=input("Description=")
     title_words=process_text(anime)
     desc_words=process_text(description)   
     newscene=Scene(
    anime,
    ep,
    timestamp,
    description,
    title_words,
    desc_words
    )
     scenes.append(newscene)
     save_database(scenes)