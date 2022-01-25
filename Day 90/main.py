import boto3
import pdftotext
all_text = ""
pdf = pdftotext.PDF("file_name.pdf")
for page in pdf:
    all_text = all_text+page
polly_client = boto3.Session(
                aws_access_key_id="AKIA2CDQS5ZKHPVE34PW",
                aws_secret_access_key="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",
                region_name='us-west-2').client('polly')

response = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3',
                Text = all_text,
                Engine = 'neural')

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()

