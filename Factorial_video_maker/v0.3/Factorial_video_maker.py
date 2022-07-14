from moviepy.editor import *
import threading

def Factorial_numbers(n):
    factorial_numbers_in_function=[]
    factorial_numbers_in_function.append(1)
    factorial_numbers_in_function.append(1)
    if(n>=2):
        for i in range(2,n+1):
            factorial_numbers_in_function.append(factorial_numbers_in_function[i-1]*i)
    return factorial_numbers_in_function

def output(video_value, video_name):
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

def output3(video_value,video_value2,video_value3, video_name):
    # Import everything needed to edit video clips


    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip2.volumex(0.8)
    clip3 = clip3.volumex(0.8)
    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    # showing video
    final_clip = concatenate_videoclips([video,video2,video3])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output4(video_value,video_value2,video_value3,video_value4, video_name):
    # Import everything needed to edit video clips


    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")


    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)


    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)


    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')


    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)


    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])


    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output5(video_value,video_value2,video_value3,video_value4,video_value5, video_name):
    # Import everything needed to edit video clips


    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")


    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)


    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)


    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')


    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)


    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])


    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output6(video_value,video_value2,video_value3,video_value4,video_value5,video_value6, video_name):
    # Import everything needed to edit video clips


    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")


    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)


    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)


    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')


    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)


    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])


    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output7(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7, video_name):
    # Import everything needed to edit video clips


    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")


    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)


    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)


    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')


    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)


    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])


    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output8(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8, video_name):
    # Import everything needed to edit video clips


    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")


    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)


    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)


    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')


    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)


    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])


    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output9(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9, video_name):
    # Import everything needed to edit video clips


    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")


    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)


    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)


    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')


    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)


    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])


    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output10(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10, video_name):
    # Import everything needed to edit video clips


    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")


    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output11(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output12(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output13(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output14(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_value14,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)
    clip14 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)
    clip14 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')
    txt_clip14 = TextClip(str(video_value14), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)
    txt_clip14 = txt_clip14.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])
    video14 = CompositeVideoClip([clip14, txt_clip14])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13,video14])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output15(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_value14,video_value15,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)
    clip14 = clip.subclip(0, 10)
    clip15 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)
    clip14 = clip.volumex(0.8)
    clip15 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')
    txt_clip14 = TextClip(str(video_value14), fontsize = 75, color = 'white')
    txt_clip15 = TextClip(str(video_value15), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)
    txt_clip14 = txt_clip14.set_pos('center').set_duration(10)
    txt_clip15 = txt_clip15.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])
    video14 = CompositeVideoClip([clip14, txt_clip14])
    video15 = CompositeVideoClip([clip15, txt_clip15])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13,video14,video15])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output16(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_value14,video_value15,video_value16,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)
    clip14 = clip.subclip(0, 10)
    clip15 = clip.subclip(0, 10)
    clip16 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)
    clip14 = clip.volumex(0.8)
    clip15 = clip.volumex(0.8)
    clip16 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')
    txt_clip14 = TextClip(str(video_value14), fontsize = 75, color = 'white')
    txt_clip15 = TextClip(str(video_value15), fontsize = 75, color = 'white')
    txt_clip16 = TextClip(str(video_value16), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)
    txt_clip14 = txt_clip14.set_pos('center').set_duration(10)
    txt_clip15 = txt_clip15.set_pos('center').set_duration(10)
    txt_clip16 = txt_clip16.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])
    video14 = CompositeVideoClip([clip14, txt_clip14])
    video15 = CompositeVideoClip([clip15, txt_clip15])
    video16 = CompositeVideoClip([clip16, txt_clip16])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13,video14,video15,video16])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output17(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_value14,video_value15,video_value16,video_value17,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)
    clip14 = clip.subclip(0, 10)
    clip15 = clip.subclip(0, 10)
    clip16 = clip.subclip(0, 10)
    clip17 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)
    clip14 = clip.volumex(0.8)
    clip15 = clip.volumex(0.8)
    clip16 = clip.volumex(0.8)
    clip17 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')
    txt_clip14 = TextClip(str(video_value14), fontsize = 75, color = 'white')
    txt_clip15 = TextClip(str(video_value15), fontsize = 75, color = 'white')
    txt_clip16 = TextClip(str(video_value16), fontsize = 75, color = 'white')
    txt_clip17 = TextClip(str(video_value17), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)
    txt_clip14 = txt_clip14.set_pos('center').set_duration(10)
    txt_clip15 = txt_clip15.set_pos('center').set_duration(10)
    txt_clip16 = txt_clip16.set_pos('center').set_duration(10)
    txt_clip17 = txt_clip17.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])
    video14 = CompositeVideoClip([clip14, txt_clip14])
    video15 = CompositeVideoClip([clip15, txt_clip15])
    video16 = CompositeVideoClip([clip16, txt_clip16])
    video17 = CompositeVideoClip([clip17, txt_clip17])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13,video14,video15,video16,video17])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output18(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_value14,video_value15,video_value16,video_value17,video_value18,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)
    clip14 = clip.subclip(0, 10)
    clip15 = clip.subclip(0, 10)
    clip16 = clip.subclip(0, 10)
    clip17 = clip.subclip(0, 10)
    clip18 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)
    clip14 = clip.volumex(0.8)
    clip15 = clip.volumex(0.8)
    clip16 = clip.volumex(0.8)
    clip17 = clip.volumex(0.8)
    clip18 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')
    txt_clip14 = TextClip(str(video_value14), fontsize = 75, color = 'white')
    txt_clip15 = TextClip(str(video_value15), fontsize = 75, color = 'white')
    txt_clip16 = TextClip(str(video_value16), fontsize = 75, color = 'white')
    txt_clip17 = TextClip(str(video_value17), fontsize = 75, color = 'white')
    txt_clip18 = TextClip(str(video_value18), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)
    txt_clip14 = txt_clip14.set_pos('center').set_duration(10)
    txt_clip15 = txt_clip15.set_pos('center').set_duration(10)
    txt_clip16 = txt_clip16.set_pos('center').set_duration(10)
    txt_clip17 = txt_clip17.set_pos('center').set_duration(10)
    txt_clip18 = txt_clip18.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])
    video14 = CompositeVideoClip([clip14, txt_clip14])
    video15 = CompositeVideoClip([clip15, txt_clip15])
    video16 = CompositeVideoClip([clip16, txt_clip16])
    video17 = CompositeVideoClip([clip17, txt_clip17])
    video18 = CompositeVideoClip([clip18, txt_clip18])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13,video14,video15,video16,video17,video18])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output19(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_value14,video_value15,video_value16,video_value17,video_value18,video_value19,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)
    clip14 = clip.subclip(0, 10)
    clip15 = clip.subclip(0, 10)
    clip16 = clip.subclip(0, 10)
    clip17 = clip.subclip(0, 10)
    clip18 = clip.subclip(0, 10)
    clip19 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)
    clip14 = clip.volumex(0.8)
    clip15 = clip.volumex(0.8)
    clip16 = clip.volumex(0.8)
    clip17 = clip.volumex(0.8)
    clip18 = clip.volumex(0.8)
    clip19 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')
    txt_clip14 = TextClip(str(video_value14), fontsize = 75, color = 'white')
    txt_clip15 = TextClip(str(video_value15), fontsize = 75, color = 'white')
    txt_clip16 = TextClip(str(video_value16), fontsize = 75, color = 'white')
    txt_clip17 = TextClip(str(video_value17), fontsize = 75, color = 'white')
    txt_clip18 = TextClip(str(video_value18), fontsize = 75, color = 'white')
    txt_clip19 = TextClip(str(video_value19), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)
    txt_clip14 = txt_clip14.set_pos('center').set_duration(10)
    txt_clip15 = txt_clip15.set_pos('center').set_duration(10)
    txt_clip16 = txt_clip16.set_pos('center').set_duration(10)
    txt_clip17 = txt_clip17.set_pos('center').set_duration(10)
    txt_clip18 = txt_clip18.set_pos('center').set_duration(10)
    txt_clip19 = txt_clip19.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])
    video14 = CompositeVideoClip([clip14, txt_clip14])
    video15 = CompositeVideoClip([clip15, txt_clip15])
    video16 = CompositeVideoClip([clip16, txt_clip16])
    video17 = CompositeVideoClip([clip17, txt_clip17])
    video18 = CompositeVideoClip([clip18, txt_clip18])
    video19 = CompositeVideoClip([clip19, txt_clip19])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13,video14,video15,video16,video17,video18,video19])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output20(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_value14,video_value15,video_value16,video_value17,video_value18,video_value19,video_value20,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)
    clip14 = clip.subclip(0, 10)
    clip15 = clip.subclip(0, 10)
    clip16 = clip.subclip(0, 10)
    clip17 = clip.subclip(0, 10)
    clip18 = clip.subclip(0, 10)
    clip19 = clip.subclip(0, 10)
    clip20 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)
    clip14 = clip.volumex(0.8)
    clip15 = clip.volumex(0.8)
    clip16 = clip.volumex(0.8)
    clip17 = clip.volumex(0.8)
    clip18 = clip.volumex(0.8)
    clip19 = clip.volumex(0.8)
    clip20 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')
    txt_clip14 = TextClip(str(video_value14), fontsize = 75, color = 'white')
    txt_clip15 = TextClip(str(video_value15), fontsize = 75, color = 'white')
    txt_clip16 = TextClip(str(video_value16), fontsize = 75, color = 'white')
    txt_clip17 = TextClip(str(video_value17), fontsize = 75, color = 'white')
    txt_clip18 = TextClip(str(video_value18), fontsize = 75, color = 'white')
    txt_clip19 = TextClip(str(video_value19), fontsize = 75, color = 'white')
    txt_clip20 = TextClip(str(video_value20), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)
    txt_clip14 = txt_clip14.set_pos('center').set_duration(10)
    txt_clip15 = txt_clip15.set_pos('center').set_duration(10)
    txt_clip16 = txt_clip16.set_pos('center').set_duration(10)
    txt_clip17 = txt_clip17.set_pos('center').set_duration(10)
    txt_clip18 = txt_clip18.set_pos('center').set_duration(10)
    txt_clip19 = txt_clip19.set_pos('center').set_duration(10)
    txt_clip20 = txt_clip20.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])
    video14 = CompositeVideoClip([clip14, txt_clip14])
    video15 = CompositeVideoClip([clip15, txt_clip15])
    video16 = CompositeVideoClip([clip16, txt_clip16])
    video17 = CompositeVideoClip([clip17, txt_clip17])
    video18 = CompositeVideoClip([clip18, txt_clip18])
    video19 = CompositeVideoClip([clip19, txt_clip19])
    video20 = CompositeVideoClip([clip20, txt_clip20])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13,video14,video15,video16,video17,video18,video19,video20])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output21(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_value14,video_value15,video_value16,video_value17,video_value18,video_value19,video_value20,video_value21,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)
    clip14 = clip.subclip(0, 10)
    clip15 = clip.subclip(0, 10)
    clip16 = clip.subclip(0, 10)
    clip17 = clip.subclip(0, 10)
    clip18 = clip.subclip(0, 10)
    clip19 = clip.subclip(0, 10)
    clip20 = clip.subclip(0, 10)
    clip21 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)
    clip14 = clip.volumex(0.8)
    clip15 = clip.volumex(0.8)
    clip16 = clip.volumex(0.8)
    clip17 = clip.volumex(0.8)
    clip18 = clip.volumex(0.8)
    clip19 = clip.volumex(0.8)
    clip20 = clip.volumex(0.8)
    clip21 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')
    txt_clip14 = TextClip(str(video_value14), fontsize = 75, color = 'white')
    txt_clip15 = TextClip(str(video_value15), fontsize = 75, color = 'white')
    txt_clip16 = TextClip(str(video_value16), fontsize = 75, color = 'white')
    txt_clip17 = TextClip(str(video_value17), fontsize = 75, color = 'white')
    txt_clip18 = TextClip(str(video_value18), fontsize = 75, color = 'white')
    txt_clip19 = TextClip(str(video_value19), fontsize = 75, color = 'white')
    txt_clip20 = TextClip(str(video_value20), fontsize = 75, color = 'white')
    txt_clip21 = TextClip(str(video_value21), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)
    txt_clip14 = txt_clip14.set_pos('center').set_duration(10)
    txt_clip15 = txt_clip15.set_pos('center').set_duration(10)
    txt_clip16 = txt_clip16.set_pos('center').set_duration(10)
    txt_clip17 = txt_clip17.set_pos('center').set_duration(10)
    txt_clip18 = txt_clip18.set_pos('center').set_duration(10)
    txt_clip19 = txt_clip19.set_pos('center').set_duration(10)
    txt_clip20 = txt_clip20.set_pos('center').set_duration(10)
    txt_clip21 = txt_clip21.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])
    video14 = CompositeVideoClip([clip14, txt_clip14])
    video15 = CompositeVideoClip([clip15, txt_clip15])
    video16 = CompositeVideoClip([clip16, txt_clip16])
    video17 = CompositeVideoClip([clip17, txt_clip17])
    video18 = CompositeVideoClip([clip18, txt_clip18])
    video19 = CompositeVideoClip([clip19, txt_clip19])
    video20 = CompositeVideoClip([clip20, txt_clip20])
    video21 = CompositeVideoClip([clip21, txt_clip21])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13,video14,video15,video16,video17,video18,video19,video20,video21])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output22(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_value14,video_value15,video_value16,video_value17,video_value18,video_value19,video_value20,video_value21,video_value22,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)
    clip14 = clip.subclip(0, 10)
    clip15 = clip.subclip(0, 10)
    clip16 = clip.subclip(0, 10)
    clip17 = clip.subclip(0, 10)
    clip18 = clip.subclip(0, 10)
    clip19 = clip.subclip(0, 10)
    clip20 = clip.subclip(0, 10)
    clip21 = clip.subclip(0, 10)
    clip22 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)
    clip14 = clip.volumex(0.8)
    clip15 = clip.volumex(0.8)
    clip16 = clip.volumex(0.8)
    clip17 = clip.volumex(0.8)
    clip18 = clip.volumex(0.8)
    clip19 = clip.volumex(0.8)
    clip20 = clip.volumex(0.8)
    clip21 = clip.volumex(0.8)
    clip22 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')
    txt_clip14 = TextClip(str(video_value14), fontsize = 75, color = 'white')
    txt_clip15 = TextClip(str(video_value15), fontsize = 75, color = 'white')
    txt_clip16 = TextClip(str(video_value16), fontsize = 75, color = 'white')
    txt_clip17 = TextClip(str(video_value17), fontsize = 75, color = 'white')
    txt_clip18 = TextClip(str(video_value18), fontsize = 75, color = 'white')
    txt_clip19 = TextClip(str(video_value19), fontsize = 75, color = 'white')
    txt_clip20 = TextClip(str(video_value20), fontsize = 75, color = 'white')
    txt_clip21 = TextClip(str(video_value21), fontsize = 75, color = 'white')
    txt_clip22 = TextClip(str(video_value22), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)
    txt_clip14 = txt_clip14.set_pos('center').set_duration(10)
    txt_clip15 = txt_clip15.set_pos('center').set_duration(10)
    txt_clip16 = txt_clip16.set_pos('center').set_duration(10)
    txt_clip17 = txt_clip17.set_pos('center').set_duration(10)
    txt_clip18 = txt_clip18.set_pos('center').set_duration(10)
    txt_clip19 = txt_clip19.set_pos('center').set_duration(10)
    txt_clip20 = txt_clip20.set_pos('center').set_duration(10)
    txt_clip21 = txt_clip21.set_pos('center').set_duration(10)
    txt_clip22 = txt_clip22.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])
    video14 = CompositeVideoClip([clip14, txt_clip14])
    video15 = CompositeVideoClip([clip15, txt_clip15])
    video16 = CompositeVideoClip([clip16, txt_clip16])
    video17 = CompositeVideoClip([clip17, txt_clip17])
    video18 = CompositeVideoClip([clip18, txt_clip18])
    video19 = CompositeVideoClip([clip19, txt_clip19])
    video20 = CompositeVideoClip([clip20, txt_clip20])
    video21 = CompositeVideoClip([clip21, txt_clip21])
    video22 = CompositeVideoClip([clip22, txt_clip22])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13,video14,video15,video16,video17,video18,video19,video20,video21,video22])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output23(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_value14,video_value15,video_value16,video_value17,video_value18,video_value19,video_value20,video_value21,video_value22,video_value23,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)
    clip14 = clip.subclip(0, 10)
    clip15 = clip.subclip(0, 10)
    clip16 = clip.subclip(0, 10)
    clip17 = clip.subclip(0, 10)
    clip18 = clip.subclip(0, 10)
    clip19 = clip.subclip(0, 10)
    clip20 = clip.subclip(0, 10)
    clip21 = clip.subclip(0, 10)
    clip22 = clip.subclip(0, 10)
    clip23 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)
    clip14 = clip.volumex(0.8)
    clip15 = clip.volumex(0.8)
    clip16 = clip.volumex(0.8)
    clip17 = clip.volumex(0.8)
    clip18 = clip.volumex(0.8)
    clip19 = clip.volumex(0.8)
    clip20 = clip.volumex(0.8)
    clip21 = clip.volumex(0.8)
    clip22 = clip.volumex(0.8)
    clip23 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')
    txt_clip14 = TextClip(str(video_value14), fontsize = 75, color = 'white')
    txt_clip15 = TextClip(str(video_value15), fontsize = 75, color = 'white')
    txt_clip16 = TextClip(str(video_value16), fontsize = 75, color = 'white')
    txt_clip17 = TextClip(str(video_value17), fontsize = 75, color = 'white')
    txt_clip18 = TextClip(str(video_value18), fontsize = 75, color = 'white')
    txt_clip19 = TextClip(str(video_value19), fontsize = 75, color = 'white')
    txt_clip20 = TextClip(str(video_value20), fontsize = 75, color = 'white')
    txt_clip21 = TextClip(str(video_value21), fontsize = 75, color = 'white')
    txt_clip22 = TextClip(str(video_value22), fontsize = 75, color = 'white')
    txt_clip23 = TextClip(str(video_value23), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)
    txt_clip14 = txt_clip14.set_pos('center').set_duration(10)
    txt_clip15 = txt_clip15.set_pos('center').set_duration(10)
    txt_clip16 = txt_clip16.set_pos('center').set_duration(10)
    txt_clip17 = txt_clip17.set_pos('center').set_duration(10)
    txt_clip18 = txt_clip18.set_pos('center').set_duration(10)
    txt_clip19 = txt_clip19.set_pos('center').set_duration(10)
    txt_clip20 = txt_clip20.set_pos('center').set_duration(10)
    txt_clip21 = txt_clip21.set_pos('center').set_duration(10)
    txt_clip22 = txt_clip22.set_pos('center').set_duration(10)
    txt_clip23 = txt_clip23.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])
    video14 = CompositeVideoClip([clip14, txt_clip14])
    video15 = CompositeVideoClip([clip15, txt_clip15])
    video16 = CompositeVideoClip([clip16, txt_clip16])
    video17 = CompositeVideoClip([clip17, txt_clip17])
    video18 = CompositeVideoClip([clip18, txt_clip18])
    video19 = CompositeVideoClip([clip19, txt_clip19])
    video20 = CompositeVideoClip([clip20, txt_clip20])
    video21 = CompositeVideoClip([clip21, txt_clip21])
    video22 = CompositeVideoClip([clip22, txt_clip22])
    video23 = CompositeVideoClip([clip23, txt_clip23])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13,video14,video15,video16,video17,video18,video19,video20,video21,video22,video23])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output24(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_value14,video_value15,video_value16,video_value17,video_value18,video_value19,video_value20,video_value21,video_value22,video_value23,video_value24,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)
    clip14 = clip.subclip(0, 10)
    clip15 = clip.subclip(0, 10)
    clip16 = clip.subclip(0, 10)
    clip17 = clip.subclip(0, 10)
    clip18 = clip.subclip(0, 10)
    clip19 = clip.subclip(0, 10)
    clip20 = clip.subclip(0, 10)
    clip21 = clip.subclip(0, 10)
    clip22 = clip.subclip(0, 10)
    clip23 = clip.subclip(0, 10)
    clip24 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)
    clip14 = clip.volumex(0.8)
    clip15 = clip.volumex(0.8)
    clip16 = clip.volumex(0.8)
    clip17 = clip.volumex(0.8)
    clip18 = clip.volumex(0.8)
    clip19 = clip.volumex(0.8)
    clip20 = clip.volumex(0.8)
    clip21 = clip.volumex(0.8)
    clip22 = clip.volumex(0.8)
    clip23 = clip.volumex(0.8)
    clip24 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')
    txt_clip14 = TextClip(str(video_value14), fontsize = 75, color = 'white')
    txt_clip15 = TextClip(str(video_value15), fontsize = 75, color = 'white')
    txt_clip16 = TextClip(str(video_value16), fontsize = 75, color = 'white')
    txt_clip17 = TextClip(str(video_value17), fontsize = 75, color = 'white')
    txt_clip18 = TextClip(str(video_value18), fontsize = 75, color = 'white')
    txt_clip19 = TextClip(str(video_value19), fontsize = 75, color = 'white')
    txt_clip20 = TextClip(str(video_value20), fontsize = 75, color = 'white')
    txt_clip21 = TextClip(str(video_value21), fontsize = 75, color = 'white')
    txt_clip22 = TextClip(str(video_value22), fontsize = 75, color = 'white')
    txt_clip23 = TextClip(str(video_value23), fontsize = 75, color = 'white')
    txt_clip24 = TextClip(str(video_value24), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)
    txt_clip14 = txt_clip14.set_pos('center').set_duration(10)
    txt_clip15 = txt_clip15.set_pos('center').set_duration(10)
    txt_clip16 = txt_clip16.set_pos('center').set_duration(10)
    txt_clip17 = txt_clip17.set_pos('center').set_duration(10)
    txt_clip18 = txt_clip18.set_pos('center').set_duration(10)
    txt_clip19 = txt_clip19.set_pos('center').set_duration(10)
    txt_clip20 = txt_clip20.set_pos('center').set_duration(10)
    txt_clip21 = txt_clip21.set_pos('center').set_duration(10)
    txt_clip22 = txt_clip22.set_pos('center').set_duration(10)
    txt_clip23 = txt_clip23.set_pos('center').set_duration(10)
    txt_clip24 = txt_clip24.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])
    video14 = CompositeVideoClip([clip14, txt_clip14])
    video15 = CompositeVideoClip([clip15, txt_clip15])
    video16 = CompositeVideoClip([clip16, txt_clip16])
    video17 = CompositeVideoClip([clip17, txt_clip17])
    video18 = CompositeVideoClip([clip18, txt_clip18])
    video19 = CompositeVideoClip([clip19, txt_clip19])
    video20 = CompositeVideoClip([clip20, txt_clip20])
    video21 = CompositeVideoClip([clip21, txt_clip21])
    video22 = CompositeVideoClip([clip22, txt_clip22])
    video23 = CompositeVideoClip([clip23, txt_clip23])
    video24 = CompositeVideoClip([clip24, txt_clip24])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13,video14,video15,video16,video17,video18,video19,video20,video21,video22,video23,video24])
    final_clip.write_videofile(video_name+".mp4",fps=24)

def output25(video_value,video_value2,video_value3,video_value4,video_value5,video_value6,video_value7,video_value8,video_value9,video_value10,video_value11,video_value12,video_value13,video_value14,video_value15,video_value16,video_value17,video_value18,video_value19,video_value20,video_value21,video_value22,video_value23,video_value24,video_value25,video_name):
    # Import everything needed to edit video clips

    # loading video dsa gfg intro video
    clip = VideoFileClip("1080p.mp4")

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)
    clip2 = clip.subclip(0, 10)
    clip3 = clip.subclip(0, 10)
    clip4 = clip.subclip(0, 10)
    clip5 = clip.subclip(0, 10)
    clip6 = clip.subclip(0, 10)
    clip7 = clip.subclip(0, 10)
    clip8 = clip.subclip(0, 10)
    clip9 = clip.subclip(0, 10)
    clip10 = clip.subclip(0, 10)
    clip11 = clip.subclip(0, 10)
    clip12 = clip.subclip(0, 10)
    clip13 = clip.subclip(0, 10)
    clip14 = clip.subclip(0, 10)
    clip15 = clip.subclip(0, 10)
    clip16 = clip.subclip(0, 10)
    clip17 = clip.subclip(0, 10)
    clip18 = clip.subclip(0, 10)
    clip19 = clip.subclip(0, 10)
    clip20 = clip.subclip(0, 10)
    clip21 = clip.subclip(0, 10)
    clip22 = clip.subclip(0, 10)
    clip23 = clip.subclip(0, 10)
    clip24 = clip.subclip(0, 10)
    clip25 = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    clip = clip.volumex(0.8)
    clip2 = clip.volumex(0.8)
    clip3 = clip.volumex(0.8)
    clip4 = clip.volumex(0.8)
    clip5 = clip.volumex(0.8)
    clip6 = clip.volumex(0.8)
    clip7 = clip.volumex(0.8)
    clip8 = clip.volumex(0.8)
    clip9 = clip.volumex(0.8)
    clip10 = clip.volumex(0.8)
    clip11 = clip.volumex(0.8)
    clip12 = clip.volumex(0.8)
    clip13 = clip.volumex(0.8)
    clip14 = clip.volumex(0.8)
    clip15 = clip.volumex(0.8)
    clip16 = clip.volumex(0.8)
    clip17 = clip.volumex(0.8)
    clip18 = clip.volumex(0.8)
    clip19 = clip.volumex(0.8)
    clip20 = clip.volumex(0.8)
    clip21 = clip.volumex(0.8)
    clip22 = clip.volumex(0.8)
    clip23 = clip.volumex(0.8)
    clip24 = clip.volumex(0.8)
    clip25 = clip.volumex(0.8)

    # Generate a text clip
    txt_clip = TextClip(str(video_value), fontsize = 75, color = 'white')
    txt_clip2 = TextClip(str(video_value2), fontsize = 75, color = 'white')
    txt_clip3 = TextClip(str(video_value3), fontsize = 75, color = 'white')
    txt_clip4 = TextClip(str(video_value4), fontsize = 75, color = 'white')
    txt_clip5 = TextClip(str(video_value5), fontsize = 75, color = 'white')
    txt_clip6 = TextClip(str(video_value6), fontsize = 75, color = 'white')
    txt_clip7 = TextClip(str(video_value7), fontsize = 75, color = 'white')
    txt_clip8 = TextClip(str(video_value8), fontsize = 75, color = 'white')
    txt_clip9 = TextClip(str(video_value9), fontsize = 75, color = 'white')
    txt_clip10 = TextClip(str(video_value10), fontsize = 75, color = 'white')
    txt_clip11 = TextClip(str(video_value11), fontsize = 75, color = 'white')
    txt_clip12 = TextClip(str(video_value12), fontsize = 75, color = 'white')
    txt_clip13 = TextClip(str(video_value13), fontsize = 75, color = 'white')
    txt_clip14 = TextClip(str(video_value14), fontsize = 75, color = 'white')
    txt_clip15 = TextClip(str(video_value15), fontsize = 75, color = 'white')
    txt_clip16 = TextClip(str(video_value16), fontsize = 75, color = 'white')
    txt_clip17 = TextClip(str(video_value17), fontsize = 75, color = 'white')
    txt_clip18 = TextClip(str(video_value18), fontsize = 75, color = 'white')
    txt_clip19 = TextClip(str(video_value19), fontsize = 75, color = 'white')
    txt_clip20 = TextClip(str(video_value20), fontsize = 75, color = 'white')
    txt_clip21 = TextClip(str(video_value21), fontsize = 75, color = 'white')
    txt_clip22 = TextClip(str(video_value22), fontsize = 75, color = 'white')
    txt_clip23 = TextClip(str(video_value23), fontsize = 75, color = 'white')
    txt_clip24 = TextClip(str(video_value24), fontsize = 75, color = 'white')
    txt_clip25 = TextClip(str(video_value25), fontsize = 75, color = 'white')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    txt_clip2 = txt_clip2.set_pos('center').set_duration(10)
    txt_clip3 = txt_clip3.set_pos('center').set_duration(10)
    txt_clip4 = txt_clip4.set_pos('center').set_duration(10)
    txt_clip5 = txt_clip5.set_pos('center').set_duration(10)
    txt_clip6 = txt_clip6.set_pos('center').set_duration(10)
    txt_clip7 = txt_clip7.set_pos('center').set_duration(10)
    txt_clip8 = txt_clip8.set_pos('center').set_duration(10)
    txt_clip9 = txt_clip9.set_pos('center').set_duration(10)
    txt_clip10 = txt_clip10.set_pos('center').set_duration(10)
    txt_clip11 = txt_clip11.set_pos('center').set_duration(10)
    txt_clip12 = txt_clip12.set_pos('center').set_duration(10)
    txt_clip13 = txt_clip13.set_pos('center').set_duration(10)
    txt_clip14 = txt_clip14.set_pos('center').set_duration(10)
    txt_clip15 = txt_clip15.set_pos('center').set_duration(10)
    txt_clip16 = txt_clip16.set_pos('center').set_duration(10)
    txt_clip17 = txt_clip17.set_pos('center').set_duration(10)
    txt_clip18 = txt_clip18.set_pos('center').set_duration(10)
    txt_clip19 = txt_clip19.set_pos('center').set_duration(10)
    txt_clip20 = txt_clip20.set_pos('center').set_duration(10)
    txt_clip21 = txt_clip21.set_pos('center').set_duration(10)
    txt_clip22 = txt_clip22.set_pos('center').set_duration(10)
    txt_clip23 = txt_clip23.set_pos('center').set_duration(10)
    txt_clip24 = txt_clip24.set_pos('center').set_duration(10)
    txt_clip25 = txt_clip25.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip

    video = CompositeVideoClip([clip, txt_clip])
    video2 = CompositeVideoClip([clip2, txt_clip2])
    video3 = CompositeVideoClip([clip3, txt_clip3])
    video4 = CompositeVideoClip([clip4, txt_clip4])
    video5 = CompositeVideoClip([clip5, txt_clip5])
    video6 = CompositeVideoClip([clip6, txt_clip6])
    video7 = CompositeVideoClip([clip7, txt_clip7])
    video8 = CompositeVideoClip([clip8, txt_clip8])
    video9 = CompositeVideoClip([clip9, txt_clip9])
    video10 = CompositeVideoClip([clip10, txt_clip10])
    video11 = CompositeVideoClip([clip11, txt_clip11])
    video12 = CompositeVideoClip([clip12, txt_clip12])
    video13 = CompositeVideoClip([clip13, txt_clip13])
    video14 = CompositeVideoClip([clip14, txt_clip14])
    video15 = CompositeVideoClip([clip15, txt_clip15])
    video16 = CompositeVideoClip([clip16, txt_clip16])
    video17 = CompositeVideoClip([clip17, txt_clip17])
    video18 = CompositeVideoClip([clip18, txt_clip18])
    video19 = CompositeVideoClip([clip19, txt_clip19])
    video20 = CompositeVideoClip([clip20, txt_clip20])
    video21 = CompositeVideoClip([clip21, txt_clip21])
    video22 = CompositeVideoClip([clip22, txt_clip22])
    video23 = CompositeVideoClip([clip23, txt_clip23])
    video24 = CompositeVideoClip([clip24, txt_clip24])
    video25 = CompositeVideoClip([clip25, txt_clip25])

    # showing video
    final_clip = concatenate_videoclips([video,video2,video3,video4,video5,video6,video7,video8,video9,video10,video11,video12,video13,video14,video15,video16,video17,video18,video19,video20,video21,video22,video23,video24,video25])
    final_clip.write_videofile(video_name+".mp4",fps=24)


def main_function(first_one,last_one):
    #first_one = 211
    #last_one = 220
    factorial_numbers=[]


    factorial_numbers=factorial_global_deger

    line_number=0
    for i in range(first_one,last_one+1):
        video_string=""
        video_string2=""
        video_string3=""
        video_string4=""
        video_string5=""
        video_string6=""
        video_string7=""
        video_string8=""
        video_string9=""
        video_string10=""
        video_string11=""
        video_string12=""
        video_string13=""
        video_string14=""
        video_string15=""
        video_string16=""
        video_string17=""
        video_string18=""
        video_string19=""
        video_string20=""
        video_string21=""
        video_string22=""
        video_string23=""
        video_string24=""
        video_string25=""


        if(len(str(factorial_numbers[i]))>44):

            line_number=(((len(str(factorial_numbers[i])))//44))

            for j in range(line_number+1):
                if(j<=12):
                    video_string+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=12):
                        video_string+="\n"
                elif(13<=j<=25):
                    video_string2+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=25):
                        video_string2+="\n"
                elif(26<=j<=38):
                    video_string3+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=38):
                        video_string3+="\n"
                elif(39<=j<=51):
                    video_string4+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=51):
                        video_string4+="\n"
                elif(52<=j<=64):
                    video_string5+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=64):
                        video_string5+="\n"
                elif(65<=j<=77):
                    video_string6+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=77):
                        video_string6+="\n"
                elif(78<=j<=90):
                    video_string7+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=90):
                        video_string7+="\n"
                elif(91<=j<=103):
                    video_string8+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=103):
                        video_string8+="\n"
                elif(104<=j<=116):
                    video_string9+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=116):
                        video_string9+="\n"
                elif(117<=j<=129):
                    video_string10+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=129):
                        video_string10+="\n"
                elif(130<=j<=142):
                    video_string11+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=142):
                        video_string11+="\n"
                elif(143<=j<=155):
                    video_string12+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=155):
                        video_string12+="\n"
                elif(156<=j<=168):
                    video_string13+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=168):
                        video_string13+="\n"
                elif(169<=j<=181):
                    video_string14+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=181):
                        video_string14+="\n"
                elif(182<=j<=194):
                    video_string15+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=194):
                        video_string15+="\n"
                elif(195<=j<=207):
                    video_string16+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=207):
                        video_string16+="\n"
                elif(208<=j<=220):
                    video_string17+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=220):
                        video_string17+="\n"
                elif(221<=j<=233):
                    video_string18+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=233):
                        video_string18+="\n"
                elif(234<=j<=246):
                    video_string19+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=246):
                        video_string19+="\n"
                elif(247<=j<=259):
                    video_string20+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=259):
                        video_string20+="\n"
                elif(260<=j<=272):
                    video_string21+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=272):
                        video_string21+="\n"
                elif(273<=j<=285):
                    video_string22+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=285):
                        video_string22+="\n"
                elif(286<=j<=298):
                    video_string23+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=298):
                        video_string23+="\n"
                elif(299<=j<=311):
                    video_string24+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=311):
                        video_string24+="\n"
                elif(312<=j<=324):
                    video_string25+=str(factorial_numbers[i])[j*44:44*(j+1)]
                    if(j!=324):
                        video_string25+="\n"


        else:
            video_string+=str(factorial_numbers[i])

        if(line_number<=12):
            output(video_string,str(i)+"!")
        elif(13<=line_number<=25):
            output2(video_string,video_string2,str(i)+"!")
        elif(26<=line_number<=38):
            output3(video_string,video_string2,video_string3,str(i)+"!")
        elif(39<=line_number<=51):
            output4(video_string,video_string2,video_string3,video_string4,str(i)+"!")
        elif(52<=line_number<=64):
            output5(video_string,video_string2,video_string3,video_string4,video_string5,str(i)+"!")
        elif(65<=line_number<=77):
            output6(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,str(i)+"!")
        elif(78<=line_number<=90):
            output7(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,str(i)+"!")
        elif(91<=line_number<=103):
            output8(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,str(i)+"!")
        elif(104<=line_number<=116):
            output9(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,str(i)+"!")
        elif(117<=line_number<=129):
            output10(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,str(i)+"!")
        elif(130<=line_number<=142):
            output11(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,str(i)+"!")
        elif(143<=line_number<=155):
            output12(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,str(i)+"!")
        elif(156<=line_number<=168):
            output13(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,str(i)+"!")
        elif(169<=line_number<=181):
            output14(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,video_string14,str(i)+"!")
        elif(182<=line_number<=194):
            output15(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,video_string14,video_string15,str(i)+"!")
        elif(195<=line_number<=207):
            output16(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,video_string14,video_string15,video_string16,str(i)+"!")
        elif(208<=line_number<=220):
            output17(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,video_string14,video_string15,video_string16,video_string17,str(i)+"!")
        elif(221<=line_number<=233):
            output18(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,video_string14,video_string15,video_string16,video_string17,video_string18,str(i)+"!")
        elif(234<=line_number<=246):
            output19(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,video_string14,video_string15,video_string16,video_string17,video_string18,video_string19,str(i)+"!")
        elif(247<=line_number<=259):
            output20(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,video_string14,video_string15,video_string16,video_string17,video_string18,video_string19,video_string20,str(i)+"!")
        elif(260<=line_number<=272):
            output21(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,video_string14,video_string15,video_string16,video_string17,video_string18,video_string19,video_string20,video_string21,str(i)+"!")
        elif(273<=line_number<=285):
            output22(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,video_string14,video_string15,video_string16,video_string17,video_string18,video_string19,video_string20,video_string21,video_string22,str(i)+"!")
        elif(286<=line_number<=298):
            output23(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,video_string14,video_string15,video_string16,video_string17,video_string18,video_string19,video_string20,video_string21,video_string22,video_string23,str(i)+"!")
        elif(299<=line_number<=311):
            output24(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,video_string14,video_string15,video_string16,video_string17,video_string18,video_string19,video_string20,video_string21,video_string22,video_string23,video_string24,str(i)+"!")
        elif(312<=line_number<=324):
            output25(video_string,video_string2,video_string3,video_string4,video_string5,video_string6,video_string7,video_string8,video_string9,video_string10,video_string11,video_string12,video_string13,video_string14,video_string15,video_string16,video_string17,video_string18,video_string19,video_string20,video_string21,video_string22,video_string23,video_string24,video_string25,str(i)+"!")



        #print(video_string)
        #print(str(len(str(factorial_numbers[i])))+" "+str(i))

#main_function(487,488)

#interspace=100
#first_one=579
#last_one=first_one+interspace

first_one=3599
last_one=3599

factorial_global_deger = Factorial_numbers(last_one)

t1=threading.Thread(target=main_function,args=(first_one,last_one))
#t2=threading.Thread(target=main_function,args=(first_one+interspace+1,last_one+interspace+1))




t1.start()
#t2.start()


