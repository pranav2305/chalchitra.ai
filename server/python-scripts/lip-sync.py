import replicate
output = replicate.run(
    "devxpy/cog-wav2lip:8d65e3f4f4298520e079198b493c25adfc43c058ffec924f2aefc8010ed25eef",
    input={"face": open("/home/pranav/Downloads/1047162783_Create a comic style image where Tony Stark says __xl-beta-v2-2-2.png", "rb"), "audio": open("/home/pranav/Downloads/WhatsApp Audio 2023-06-10 at 3.24.53 PM.mp3", "rb")},
)
print(output)