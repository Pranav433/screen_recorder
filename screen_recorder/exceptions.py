class ffmpegerror(Exception):
    not_installed_message = "ffmpeg is not installed"
    file_types = ("mp4","flv","mkv","mov","wmv","avi")
    def __init__(self,filename):
        if filename.strip()[-3:].lower() not in self.file_types:
            super().__init__(f"'{filename.strip()[-3:]}' filetype not supported")
        else:
            super().__init__(self.not_installed_message)

class stereomixerror(Exception):
    message = "Stereo Mix is not enabled"
    def __init__(self):
        super().__init__(self.message)

