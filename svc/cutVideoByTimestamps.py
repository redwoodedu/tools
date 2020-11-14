import os, argparse, datetime, time

parser = argparse.ArgumentParser(description='Cut video based on provided time segments.')
parser.add_argument('input', metavar='input', type=str, help='input video')
parser.add_argument('timestamps', metavar='timefile', type=str, help='timestamps file')
parser.add_argument('--output', '-o', metavar='output', type=str, default='out.mp4', help='output video')

'''
Sample command
ffmpeg -i test.mp4 -vf "select='between(t,1,2)+between(t,4,5)',setpts=N/FRAME_RATE/TB" -af "aselect='between(t,1,2)+between(t,4,5)',asetpts=N/SR/TB" out.mp4
'''

# timestr should like 00:00:01.123,00:00:02.222
def time2sec(timestr):
	parts = timestr.split(',')
	start = parts[0].split('.')
	end = parts[1].split('.')
	ts = time.strptime(start[0], '%H:%M:%S')
	te = time.strptime(end[0], '%H:%M:%S')
	return str(datetime.timedelta(hours=ts.tm_hour,minutes=ts.tm_min,seconds=ts.tm_sec).total_seconds() + float(start[1])/1000) + ',' + str(datetime.timedelta(hours=te.tm_hour,minutes=te.tm_min,seconds=te.tm_sec).total_seconds() + float(end[1])/1000)

def main():
	args = parser.parse_args()
	segments_str = ''
	formats = ['seconds', 'HHMMSSmmm']
	
	with open(args.timestamps) as f:
		lines = f.readlines()
		f = lines[0].strip().split(',')[0]
		if f == formats[1]:
			val = time2sec(lines[1].strip())
		else:
			val = lines[1].strip()
		segments_str = 'between(t,' + val + ')'
		for l in lines[2:]:
			if f == formats[1]:
				val = time2sec(l.strip())
			else:
				val = l.strip()
			segments_str = segments_str + '+between(t,' + val + ')'

	print(segments_str)
	ffmpeg_cmd = 'ffmpeg -i "' + args.input + '" -vf "select=\'' + segments_str + '\',setpts=N/FRAME_RATE/TB" -af "aselect=\'' + segments_str + '\',asetpts=N/SR/TB" "' + args.output + '"'

	print(ffmpeg_cmd)
	os.system(ffmpeg_cmd)


if __name__ == '__main__':
	main()