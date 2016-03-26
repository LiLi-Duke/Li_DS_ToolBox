
# coding: utf-8

# #### Below is to remove the leading & trailing space, convert all to lowercase, and remove any punctuation in a string. This is from Lab1 of edX "Intro to Big Data with Apache Spark"

# In[1]:

import re
import string
print string.punctuation
s = " This, Is goo'D! "
print s.lower().strip()
p = re.compile('[%s]' % re.escape(string.punctuation))
print re.sub(p, '', s.lower().strip())


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



