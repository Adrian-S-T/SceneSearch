import json
def load_database():
    with open("scenes.json","r") as file:
        scenes=json.load(file)
    return scenes

def scene_printer(scene):
    """prints a scene"""
    print(scene["anime"])
    print(scene["episode"])
    print(scene["timestamp"])
    print(scene["description"])

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
def search_scenes(scenes,keyword):
    """searches for scenes in anime names and desc based on inputted keywords + counts matches"""
    matches=0
    for element in scenes:
          if keyword.lower() in element["description"].lower() or keyword.lower() in element["anime"].lower():
              matches+=1
              scene_printer(element)
    if matches==0:
        print("no matching scenes found")
    else:
        print("Found",matches, "matching scenes")
    return matches
def main():
    scenes=load_database()
    option=-1
    while option!=3:
        print("1:search for a scene")
        print("2:add a scene in the database")
        print("3:quit the program")
        try:
            option=int(input("Please make your choice\n"))
        except:
            print("what you entered is not a valid option")
        if option==1:
            keyword=input("Search:")
            matches=search_scenes(scenes,keyword)
            print("Search finished")
        elif option==2:
                add_scene(scenes)
        elif option>3 or option<1:
                print("The selected option is invalid, please try again")
main()