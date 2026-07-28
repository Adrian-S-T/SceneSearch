from display import scene_printer
def search_scenes(scenes,keyword):
    """searches for scenes in anime names and desc based on inputted keywords + counts matches"""
    search_words=(keyword.lower()).split()
    results=[]
    for element in scenes:
          name = set(element.anime.lower().split())
          description = set(element.description.lower().split())
          score=0
          for word in search_words:
             if word in name:
                      score=score+3
             if word in description:
                      score=score+1
          if score>0:
             results.append((element,score))
    return results