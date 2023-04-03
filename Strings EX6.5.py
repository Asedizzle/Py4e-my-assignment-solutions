#ATTEMPT 1
text = "X-DSPAM-Confidence:    0.8475"
t=text.find(":")
r = text.split()
x = (r[-1])
w = float(x)
print(w)

#ATTEMPT 2
text = "X-DSPAM-Confidence:    0.8475"
t = text.find(":")
y = text[t+1:]
x = float(y)
print(x)