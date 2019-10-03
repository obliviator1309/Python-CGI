
# coding: utf-8

# In[ ]:


import pyaudio
import socket
import pyttsx3
s = socket.socket()


# In[ ]:


import speech_recognition as sr
mic  =  sr.Microphone()
rec =  sr.Recognizer()


# In[ ]:


speaker = pyttsx3.init()
speaker.say("Hello sir can you tell me your name")
speaker.runAndWait()

y = input()
while True:
    s = socket.socket()
    speaker.say("Hello '{}'. I am vincy how may i help you".format(y))
    speaker.runAndWait()

    text = input()
    s.connect(("192.168.43.206", 1234))
    if "docker"  in text  and "Run" in text:
        speaker.say("What name do you want to give to your container")
        speaker.runAndWait()
        
        text = input()
                
        print(text)
        x = text
                
        cmd = " ansible-playbook  --extra-vars='docker='{}' ' /etc/ansible/playbooks/docker.yml ".format(x)
        
        s.send(cmd.encode())
        speaker.say("Container Launched Successfully.")
        speaker.runAndWait()
        
        
        print(s.recv(1024))
        s.close()
        
       
            
    elif "click"  in text  and "photo" in text:
        cmd = " python36 /var/www/cgi-bin/click.py "
       
        s.send(cmd.encode())
        speaker.say("Your Photo Has been clicked. Thank You")
        speaker.runAndWait()
        
        s.close()
    
        
    elif "start"  in text  and "video" in text:
   
        cmd = " python36 /var/www/cgi-bin/video.py "
        s.send(cmd.encode())
        
        speaker.say("Your Live video has been started. Enjoy it")
        speaker.runAndWait()
        print(s.recv(1024))
        s.close()
        
            
        

    elif "detect"  in text  and "face" in text:
        cmd = " python36 /var/www/cgi-bin/face.py "
        
    elif "launch" in text and "cloud" in text:
        cmd = "ansible-playbook /etc/ansible/playbooks/aws.yml"
        s.send(cmd.encode())
        speaker.say("Your ec2 has been launched. Enjoy it ")
        speaker.runAndWait()
        print(s.recv(1024))
        s.close()
        

    elif "launch"  in text  and "bucket" in text:
        cmd = " ansible-playbook /etc/ansible/playbooks/s3.yml "
        s.send(cmd.encode())
        speaker.say("Your bucket has been launched. Enjoy it")
        speaker.runAndWait()
        print(s.recv(1024))
        s.close()  
    elif "VNC" in text and "portal" in text:
        
        cmd = "firefox http://master.com:6080/vnc.html?host=master.com&port=6080"
        s.send(cmd.encode())
        speaker.say("Your vnc portal is opened. Work Accordingly")
        speaker.runAndWait()
        print(s.recv(1024))
        s.close()
    

    else: 
        
        speaker.say("Sorry I dont Understand.Please Try Again.")
        speaker.runAndWait()
        s.close()
        
        
        
    
    

