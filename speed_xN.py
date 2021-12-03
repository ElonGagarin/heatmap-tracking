import subprocess

def change_speed(input_path='1.mp4', 
                    speed='0.10',
                    out_path='input.mp4'):

    command = f'ffmpeg -i {input_path} -vf  "setpts={speed}*PTS" {out_path}'
    subprocess.run(command, shell=True)


if __name__=='__main__':
    change_speed()
