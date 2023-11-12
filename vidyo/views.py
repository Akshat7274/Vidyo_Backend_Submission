from django.shortcuts import render
from django.http import JsonResponse
from moviepy.editor import VideoFileClip, ImageSequenceClip
from PIL import Image
import numpy as np
from vidyo.models import ExtractAudio, Watermark

# Create your views here.
def index(request):
    return render(request,'index.html')

def extract(request):
    if request.method=='GET':
        inputfile = dict(request.GET)['input'][0]
        outputfile = dict(request.GET)['output'][0]
        videoclip = VideoFileClip(inputfile)
        audioclip = videoclip.audio
        audioclip.write_audiofile(outputfile)

        add_record = ExtractAudio(
            username = "Current User",
            input = inputfile,
            output = outputfile
        )
        add_record.save()
    return JsonResponse({'status':"Success",'message':"The Audio file has been extracted, and the output is saved to " + outputfile})

def watermark(request):
    if request.method=='GET':
        videofile = dict(request.GET)['videoFile'][0]
        imagefile = dict(request.GET)['imageFile'][0]
        outputfile = dict(request.GET)['outputFile'][0]
        wmSize = (int(dict(request.GET)['wmWid'][0]),int(dict(request.GET)['wmHei'][0]))
        wmPos = (int(dict(request.GET)['wmX'][0]),int(dict(request.GET)['wmY'][0]))

        videoClip = VideoFileClip(videofile)
        wmImage = Image.open(imagefile)
        wmImage = wmImage.resize(wmSize)
        wmImage = wmImage.convert("RGBA")

        frames = []

        for frame in videoClip.iter_frames(fps=videoClip.fps):
            frame_pil = Image.fromarray(frame)
            frame_pil.paste(wmImage,wmPos)
            frames.append(np.array(frame_pil))
            
        wmClip = ImageSequenceClip(frames,fps=videoClip.fps)
        wmClip = wmClip.set_audio(videoClip.audio)
        wmClip.write_videofile(outputfile,codec="libx264",audio_codec="aac")

        add_record = Watermark(
            username = "Current User",
            video = videofile,
            image = imagefile,
            output = outputfile,
            size = str(wmSize),
            position = str(wmPos) 
        )
        add_record.save()
    return JsonResponse({'status':"Success",'message':"The watermarked video has been created, and the output is saved to " + outputfile})