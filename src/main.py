import json
from database import load_database
from database import save_database
from database import add_scene
from display import scene_printer
from search import search_scenes
from scene import Scene
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
            results=search_scenes(scenes,keyword)
            results.sort(key=lambda result:result[1],reverse=True)
            if len(results)>0:
                 nr=len(results)
                 print("Found",nr,"matching scenes.")
            results=enumerate(results,start=1)
            for index,scene in results:
                 print("Result #",index)
                 print("score =",scene[1])
                 scene_printer(scene[0])
                 print("................................")
            if(len(results)==0):
                 print("No matching scenes found.")
            print("Search finished")
        elif option==2:
                add_scene(scenes)
        elif option>3 or option<1:
                print("The selected option is invalid, please try again")
main()