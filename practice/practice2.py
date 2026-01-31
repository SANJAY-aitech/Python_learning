s="Abc 012..## 10cbA"
cleaned_s = s.replace(" ", "").replace(".", "").replace("#", "").lower()
print(cleaned_s)
print(cleaned_s[::-1] == cleaned_s)  # Check if the cleaned string is a palindrome
  # Reverse the string