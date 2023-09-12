from moviepy.editor import VideoFileClip,concatenate_videoclips 

#minutes that you want in ur video
cuts= [('00:00:18','00:00:30'),('00:01:18','00:01:25'),('00:01:52','00:01:57')]

videoquality="24"
vcodec = "libx264"

title= 'farah w marilli.mp4' #with extention
myVideo= title
saveVideo= title +'.mp4'

# video_editing_func.
def VideoEditor(title,cuts,saveVideo) :
    myVideo= VideoFileClip(title)
    video =[]
    for cut in cuts:
      clips =myVideo.subclip(cut[0],cut[1])
      video.append(clips)
    
    finalOutPut= concatenate_videoclips(video)
    
    #savefile 
    finalOutPut.write_videofile(saveVideo, codec= vcodec,fps=24)

    myVideo.close()
 
VideoEditor(title,cuts,saveVideo) 