#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import gym
import rware

env = gym.make("CartPole-v1", render_mode="human")

#env = gym.make("rware-tiny-2ag-v1")
#env = gym.make("rware-small-4ag-v1")
#env = gym.make("rware-medium-6ag-hard-v1")

import gym
#env = gym.make("rware:rware-tiny-2ag-v1")
observation = env.reset()

#done = False
#max_steps = 4000  # Set a maximum number of steps
#step_count = 0
#while not done and step_count < max_steps:
#    action = env.action_space.sample()  # Sample a random action
#    step_result = env.step(action)
#    observation, reward, done, info = step_result[:4]  # Extract first four elements
#    env.render()
#    step_count += 1

#env.close()  # Close the environment after the loop ends


# In[ ]:





# In[ ]:




