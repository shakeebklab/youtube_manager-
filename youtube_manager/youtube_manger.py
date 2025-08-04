# I am goign to write a progaram to manage youtube videos i will manage name and time duaration
# the functiosnality will be to add, remove and update the video details
# i will json which convert the data in the form of string to the file and vice versa
# Json has two method dump and load which i am going to use in this program
import json
file_key = 'youtube_file.txt'
def load_videos():
    try:
        with open(file_key, 'r') as file:
            videos = json.load(file)
            return videos
    except FileNotFoundError:
        return []

def helper_function(videos):
    with open(file_key, 'w') as file:
        json.dump(videos, file)
   

def  list_of_videos(videos):
    print("======= List of Videos: =======")
    
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Duration: {video['duration']}")
        helper_function(videos)
   
   



def  add_video(videos):
     name = input("Enter the video name: ")
     duration = input("Enter the video duration: ")
     videos.append({'name': name, 'duration': duration})
     helper_function(videos)
    
     print("Video added successfully!")



def  update_video(videos):
    list_of_videos(videos)
    index = int(input("enter the value which want to update: "))
    if index > 0 and index < len(videos):
        name = input("Enter the video name: ")
        duration = input("Enter the video duration: ")
        videos[index -1] = {'name': name, 'duration': duration}
        helper_function(videos)

        print("Video updated successfully!")
    
    else:
        print("Invalid index, please try again.")




def  delete_video(videos):
      list_of_videos(videos)
      index = int(input("enter the value which want to delete: "))
      if index > 0 and index <= len(videos):
            del videos[index-1]
            helper_function(videos)

            print("Video deleted successfully!")
      
      else:
            print("Invalid index, please try again.")





def main():
  
    while True:
        videos = load_videos()
        print("================ welcome to youtube Maneger =================\n")
        
        print('Enter 1 to list all videos')
        print("Enter 2 to add a video")
        print("Enter 3 to update a video")
        print("Enter 4 to delete a video")

        input_value = input("Enter Your value: ")

        match input_value:
            case "1":
                list_of_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                 delete_video(videos)
            case _:
                print("Invalid input, please try again.")

if __name__ == "__main__":
    main()