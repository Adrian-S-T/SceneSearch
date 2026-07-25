from display import scene_printer
def search_scenes(scenes,keyword):
    """searches for scenes in anime names and desc based on inputted keywords + counts matches"""
    search_words=(keyword.lower()).split()
    results=[]
    for element in scenes:
          text = (element.anime + " " + element.description).lower()
          score=0
          for word in search_words:
             if word in text:
                      score=score+1
          if score>0:
             results.append((element,score))
    return results