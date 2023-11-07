import whisper
import json
import os
import validators
import moviepy.editor as mp
from mimetypes import guess_type
from sjautils.commands import download_video
from sjautils.web_utils import is_url
from pytube import YouTube

def is_youtube_url(url):
    return ('youtu.be' in url) or ('youtube.com' in url)

def transcribe_path(path, model='base', write_json=False, text_out=True):
    model = whisper.load_model(model)
    text = model.transcribe(path)
    return text

    base, _ = os.path.splitext(path)
    if write_json:
        with open(f'{base}.json', 'w') as f:
            json.dump(text, f)
    if text_out:
        with open(f'{base}.txt', 'w') as f:
            for l in text['text'].split('.'):
                print(l + '.', file=f)

class VideoTranscriber:
    def __init__(self, url_or_path, model='base'):
        self._audio_path = self.extract_audio(url_or_path)
        self._model = whisper.load_model(model)
        self._text = None


    def transcribe(self):
        self._text =  self._model.transcribe(self._audio_path)
        os.remove(self._audio_path)
        return self._text

    def audio_from_vid(self, path):
        base, _ = os.path.splitext(path)
        clip = mp.VideoFileClip(path)
        out = f'{base}.mp3'
        clip.audio.write_audiofile(out)
        return out

    def extract_from_url(self, url):
        if is_youtube_url(url):
            YouTube(url).streams.filter(
                only_audio=True).first().download(filename="audio.mp3")
            return 'audio.mp3'
        else:
            vid_path =  download_video(url)
            return self.audio_from_vid(vid_path)





    def extract_audio(self, what):
        if is_url(what):
            return self.extract_from_url(what)
        elif os.path.exists(what):
            type,_ = guess_type(what)
            if type:
                if type.startswith('video'):
                    return self.audio_from_vid(what)
                elif type.startswith('audio'):
                    return what
        raise Exception(f'no idea how to transcribe {what}')



    def __call__(self, write_json=False, text_out=True):
        base, _ = os.path.splitext(self._audio_path)
        text = self.transcribe()
        if write_json:
            with open(f'{base}.json', 'w') as f:
                json.dump(text, f)
        if text_out:
            with open(f'{base}.txt', 'w') as f:
                for l in text['text'].split('.'):
                    print(l + '.', file=f)




def transcribe(what, model='base', write_json=True, text_out=True):
    transcriber = URLTranscriber()
    args = dict(model=model, write_json=write_json, text_out=text_out)
    if validators.url(what):
        return transcribe_url(what, **args)
    elif os.path.exists(what):
        return transcribe_path(what, **args)


