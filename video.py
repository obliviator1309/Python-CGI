#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


cap = cv2.VideoCapture(0)


# In[3]:


while True:
    ret , photo = cap.read()
    cv2.imshow("video.png",photo)
    if cv2.waitKey(1) == 13:
        break
        
cv2.destroyAllWindows()
cap.release()


# In[ ]:




