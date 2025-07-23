import re  
pattern = r"[a-z]+ission"
text = '''Ascender AI has a mission to apply AI to the media, and NewsAPI is one of our most valuable resources. Ascender is redefining how users interact with complex information, and the NewsAPI feed is an essential tission showcase for our technologies'''
match = re.search(pattern,text)
print(match)

print("-------------")


# next code
import re  
pattern = r"[a-z]+ission"
text = '''Ascender AI has a mission to apply AI to the media, and NewsAPI is one of our most valuable resources. Ascender is redefining how users interact with complex information, and the NewsAPI feed is an essential tission showcase for our technologies'''
matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])