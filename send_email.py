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

def sendSpotifyPlaylistSongs(songs, receiver, email_size_limit=10 * 1024 * 1024):
    def calculate_message_size(msg):
        serialized_msg = msg.as_string()
        return len(serialized_msg)

    def create_new_message():
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = 'Your Spotify Playlist'
        return msg

    sender = "your_email@example.com"  # Update this with your sender email

    messages = []
    current_msg = create_new_message()
    total_size = 0
    for song in songs:
        song_name = unidecode(song)
        path = f'/home/rudrap/pyJukebox/{song_name}.mp3'
        song_size = os.path.getsize(path)

        if total_size + song_size > email_size_limit:
            messages.append(current_msg)
            current_msg = create_new_message()
            total_size = 0

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(path, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment;filename="{song_name}.mp3"')
        current_msg.attach(part)
        total_size += song_size

    if current_msg.get_payload():
        messages.append(current_msg)

    for idx, msg in enumerate(messages, start=1):
        send_email(msg, receiver)
        print(f"Sent message {idx} with {len(msg.get_payload())} songs.")

    print('All messages sent')
def create_email_and_send(songName,receiver):
    path=f'/home/rudrap/pyJukebox/{songName}.mp3'
    print(determine_mime_type(path))
    audio=encode_audio_files(path)
    message=create_email(audio,sender,receiver,f'{songName}.mp3',path)
    send_email(message,receiver)
    print('Sent successfully')

