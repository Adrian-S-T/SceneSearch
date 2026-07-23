from display import scene_printer
def search_scenes(scenes,keyword):
    """searches for scenes in anime names and desc based on inputted keywords + counts matches"""
    matches=0
    for element in scenes:
          if keyword.lower() in element.description.lower() or keyword.lower() in element.anime.lower():
              matches+=1
              scene_printer(element)
    if matches==0:
        print("no matching scenes found")
    else:
        print("Found",matches, "matching scenes")
    return matches