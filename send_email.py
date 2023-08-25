import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
import magic,os
from unidecode import unidecode
from dotenv import load_dotenv
load_dotenv()
sender='rudrapthk0@gmail.com'
password=os.getenv('password')
port=465
def determine_mime_type(path):
    mime=magic.Magic(mime=True)
    return mime.from_file(path)
def encode_audio_files(path):
    with open(path,'rb') as f:
        encoded_audio=f.read()
    return encoded_audio
def create_email(audio,sender,receiver,songName,path):
    msg=MIMEMultipart()
    msg['From']=sender
    msg["To"]=receiver
    msg['Subject']='Here are your songs'
    mime_type=determine_mime_type(path)
    audio_part=MIMEBase('application','octet-stream')
    audio_part.set_payload(audio)
    encoders.encode_base64(audio_part)
    audio_part.add_header('Content-Disposition',f'attachment;filename="{songName}"')
    msg.attach(audio_part)
    return msg
def send_email(message,receiver):
    with smtplib.SMTP_SSL('smtp.gmail.com',port) as server:
        server.login(sender,password)
        server.sendmail(from_addr=sender,to_addrs=receiver,msg=message.as_string())

def sendSpotifyPlaylistSongs(songs,receiver):
    msg=MIMEMultipart()
    msg['From']=sender
    msg['To']=receiver
    msg['Subject']='Your Spotify Playlist'
    for song in songs:
        songName=unidecode(song)
        path=f'/home/rudrap/pyJukebox/{songName}.mp3'
        part=MIMEBase('applicatiion','octet-stream')
        part.set_payload(open(path,'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',f'attachment;filename="{songName}.mp3"')
        msg.attach(part)
        print('message attached')
    send_email(msg,receiver)
    print('Done')
def create_email_and_send(songName,receiver):
    path=f'/home/rudrap/pyJukebox/{songName}.mp3'
    print(determine_mime_type(path))
    audio=encode_audio_files(path)
    message=create_email(audio,sender,receiver,f'{songName}.mp3',path)
    send_email(message,receiver)
    print('Sent successfully')

