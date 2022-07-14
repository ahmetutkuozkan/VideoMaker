import math
from moviepy.editor import *

def Fibonacci(n):
    fibonacci_numbers.append(0)
    fibonacci_numbers.append(1)
    if(n>=2):
        for i in range(2,n+1):
            fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])

def output(video_value, video_ismi):
    # Import everything needed to edit video clips


    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

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
    video.write_videofile(video_ismi+".mp4",fps=24)


line_number=0

fibonacci_numbers=[]

Fibonacci(1800)




first_one = 397
last_one = 1800

for i in range(last_one+1):
    if(last_one>=i>=first_one):
        video_string=""
        if(len(str(fibonacci_numbers[i]))>45):
            if((len(str(fibonacci_numbers[i]))/45)>int((len(str(fibonacci_numbers[i]))/45))):
                line_number=int((len(str(fibonacci_numbers[i]))/44))+1
            for j in range(line_number):
                video_string+=str(fibonacci_numbers[i])[j*44:44*(j+1)]
                if(j<line_number-1):
                    video_string+="\n"
        else:
            video_string+=str(fibonacci_numbers[i])
        output(video_string,str(i))
        #print(video_string)
        #print(str(len(str(fibonacci_numbers[i])))+" "+str(i))

