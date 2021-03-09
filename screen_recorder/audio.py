import sounddevice as sd
from queue import Queue
from soundfile import SoundFile
from os import mkdir,listdir,getcwd
from .exceptions import stereomixerror
class Audio:
    WAVE_OUTPUT_FILENAME = getcwd()+"/tmp/{}.wav"
    def __init__(self,unique_id):
        self.unique_id = unique_id
        self.device_name = "Stereo Mix (Realtek(R) Audio), MME"
        try:
            self.device = sd.query_devices(self.device_name,'input')
        except ValueError:
            raise stereomixerror()
        self.RATE = self.device.get('default_samplerate')
        self.CHANNELS = self.device.get('max_input_channels')
        self.q = Queue()
    def _callback(self,indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(indata.copy())
    def _record_audio(self):
        with SoundFile(self.WAVE_OUTPUT_FILENAME.format(self.unique_id), mode='x', samplerate=int(self.RATE),
                      channels=self.CHANNELS, subtype=None) as file:
            with sd.InputStream(samplerate=self.RATE, device=self.device_name,
                                channels=self.CHANNELS, callback=self._callback):
                while True:
                    if not self.record:
                        break
                    file.write(self.q.get())

