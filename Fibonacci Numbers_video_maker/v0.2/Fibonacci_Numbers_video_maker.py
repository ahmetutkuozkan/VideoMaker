import math
from moviepy.editor import *
import threading


def Fibonacci(n):
    fibonacci_numbers.append(0)
    fibonacci_numbers.append(1)
    if(n>=2):
        for i in range(2,n+1):

            fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])


def output(video_value, video_name):
    # Import everything needed to edit video clips


    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")
    #clip = clip.resize((1920,1080))
    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])

    # showing video
    video.write_videofile(video_name+".mp4",fps=24)

def output2(video_value,video_value2, video_name):
    # Import everything needed to edit video clips


    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    # showing video
    final_clip = concatenate_videoclips([video,video2])
    final_clip.write_videofile(video_name+".mp4",fps=24)

line_number=0

fibonacci_numbers=[]






#interspace=550
#first_one=2513
#last_one=first_one+interspace

first_one=3615
last_one=3652

Fibonacci(3652)

def main_function(first_one,last_one):
    for i in range(last_one+1):
        if(last_one>=i>=first_one):
            video_string=""
            video_string2=""

            if(len(str(fibonacci_numbers[i]))>44):

                line_number=int((len(str(fibonacci_numbers[i]))//44))

                for j in range(line_number+1):
                    if(j<=12):
                        video_string+=str(fibonacci_numbers[i])[j*44:44*(j+1)]
                        if(j!=12):
                            video_string+="\n"
                    elif(13<=j<=25):
                        video_string2+=str(fibonacci_numbers[i])[j*44:44*(j+1)]
                        if(j!=25):
                            video_string2+="\n"
            else:
                video_string+=str(fibonacci_numbers[i])

            if(line_number<=12):
                output(video_string,str(i))
            elif(13<=line_number<=25):
                output2(video_string,video_string2,str(i))
            #print(video_string)
            #print(str(len(str(fibonacci_numbers[i])))+" "+str(i))


t1=threading.Thread(target=main_function,args=(first_one,last_one))
#t2=threading.Thread(target=main_function,args=(first_one+interspace+1,last_one+interspace+1))




t1.start()
#t2.start()
