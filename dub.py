
# # Python code to convert video to audio
# import moviepy.editor as mp
  
# # Insert Local Video File Path 
# clip = mp.VideoFileClip(r"C:\\Users\\admin\\Desktop\\Dubbing System\\input\\Test.mp4")
  
# # Insert Local Audio File Path
# clip.audio.write_audiofile(r"C:\\Users\\admin\\Desktop\\Dubbing System\\Output")\


import moviepy.editor as mp


def extract(video_path, audio_name, audio_format):
	"""
	Function that extract audio from video
	Assintotic: O(1)
	"""
	video = mp.VideoFileClip(video_path)
	audio = video.audio
	audio.write_audiofile('Output/' + audio_name + '.' + audio_format)

try:
	video_path = 'input/Test.mp4'
	audio_name = input('Audio File Name:')
	audio_option = input('\nChoose a format:\n'
						+ '0 - MP3 (default)\n'
						+ '1 - WAV\n')
	audio_format = 'wav' if audio_option == '1' else 'mp3'

	extract(video_path, audio_name, audio_format)



except Exception as e: print(e)


