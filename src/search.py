from display import scene_printer
def search_scenes(scenes,keyword):
    """searches for scenes in anime names and desc based on inputted keywords + counts matches"""
    matches=0
    search_words=(keyword.lower()).split()
    for element in scenes:
          text = (element.anime + " " + element.description).lower()
          score=0
          for word in search_words:
             if word in text:
                      score=score+1
          if score>0:
             matches+=1
             scene_printer(element)
             print("score:",score)
    if matches==0:
        print("no matching scenes found")
    else:
        print("Found",matches, "matching scenes")
    return matches