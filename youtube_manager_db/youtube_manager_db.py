
import sqlite3

con = sqlite3.connect('manager.db')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    duration TEXT NOT NULL
)
''')


def list_of_videos():
    print("List of videos:\n")
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)
      
    
def add_video():
    name = input("enter a video name: ")
    duration = input("enter a video duration: ")
    cur.execute("INSERT INTO videos (name, duration) VALUES (?,?)",(name, duration))
    con.commit()

    print("Video added successfully!\n")

def update_video():
    new_name = input("Enter new name for the video: ")
    new_duration = input("Enter new duration for the video: ")
    video_id = int(input("Enter the ID of the video to update: "))
    cur.execute("UPDATE videos SET name = ? , duration = ? WHERE id = ?",(new_name, new_duration, video_id))
    con.commit()
    print("Video updated successfully!\n")

def  delete_video():
     video_id = int(input("Enter the ID of the video to update: "))
     cur.execute("DELETE FROM videos WHERE ID  = ? ",(video_id,))
     con.commit()
     print("Video deleted successfully!\n")
 



def main():
  
    while True:
      
        print("================ welcome to youtube Maneger =================")
        
        print('Enter 1 to list all videos')
        print("Enter 2 to add a video")
        print("Enter 3 to update a video")
        print("Enter 4 to delete a video")
        print("Enter 5 to Exit")

        input_value = input("Enter Your value: ")

        match input_value:
            case "1":
                list_of_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                 delete_video()
            case "5":
                break
            case _:
                print("Invalid input, please try again.")
    con.close()
if __name__ == "__main__":
    main()