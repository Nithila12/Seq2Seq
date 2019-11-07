
# coding: utf-8

# In[6]:


import pickle
CSV = ""
with open('translation_data.bin', 'rb') as f:
    corpus, source_vocab, target_vocab = pickle.load(f)
    print(len(corpus))


# In[31]:


def i2s(I,p):
    K = ""
    for i in I[:-1]:
        if p[i] in '.!?':
            K += p[i]
        elif p[i]==',':
            pass
        else:
            K += " "+p[i]
    return K.strip()


# In[34]:


CSV = "source sentence, target sentence\n"
for s,t in corpus:
    S = i2s(s,source_vocab)
    T = i2s(t,target_vocab)
    print(S,T)
    CSV += f"{S} , {T}\n"
CSV = CSV.strip()


# In[35]:


with open('F2E.csv','w') as file:
    file.write(CSV)

