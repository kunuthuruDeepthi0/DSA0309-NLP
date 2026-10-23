import re

text = "Hello, my phone number is 9876543210"
print(re.match("Hello", text).group())
result = re.search(r"\d{10}", text)
print(result.group())
