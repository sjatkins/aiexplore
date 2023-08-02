import whisper
import json
import os


def transcribe_path(path, model='base', write_json=False, text_out=True):
    model = whisper.load_model(model)
    text = model.transcribe(path)
    base, _ = os.path.splitext(path)
    if write_json:
        with open(f'{base}.json', 'w') as f:
            json.dump(text, f)
    if text_out:
        with open(f'{base}.txt', 'w') as f:
            for l in text['text'].split('.'):
                print(l + '.', file=f)

def transcribe_youtube(what, **kwargs):
    pass

def transcribe_url(what, **kwargs):
    pass

def transcribe(what, model='base', write_json=True, text_out=True):
    pass


