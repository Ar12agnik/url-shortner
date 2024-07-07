import random
lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper=[x.upper() for x in lower ]
digits=[x for x in range(10)]
def choose_random(lower,upper,digits,*args, **kwargs):
    l=random.choice(lower)
    u=random.choice(upper)
    d=random.choice(digits)
    final_str=f"{l}{u}{d}"
    return final_str
# for _ in range(100000):
#     already_generated.append(choose_random(lower,upper,digits))
# for a in already_generated:
#     x=already_generated.count(a)from 
#     occurence[a]=x
# more_than_once=0
# for value in occurence.values():
#     if value>1:
#         more_than_once+=1
# c=(more_than_once/100000)*100
# print(f"percentage of similarities {c}%")