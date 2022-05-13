# Вывести каждый символ
import re
result = re.findall(r".", 'Everest is the largest mountain in the World')
print("#1")
print(result)

result = re.findall(r"\w", 'Everest is the largest mountain in the World')
print("#2")
print(result)

result = re.findall(r"\w+", 'Everest is the largest mountain in the World')
print("#3")
print(result)

result = re.findall(r"\w*", 'Everest is the largest mountain in the World')
print("#3")
print(result)

result = re.findall(r"\w+", 'Everest is the largest mountain in the World')
print("#4 все слова")
print(result)
result = re.findall(r"\b[aeiouAEIOU]\w+", 'Google s free service'
                                          ' allows you to instantly translate '
                                          'words, phrases and web pages from English into more '
                                          'than 100 languages ​​and vice versa.')
print("#4 только гласные")
print(result)
result = re.findall(r"\d+", 'Google s free service'
                                          ' allows you to instantly translate '
                                          'words, phrases and web pages from English into more '
                                          'than 100 languages ​​and vice versa.')
print("#4 только число")
print(result)

result = re.findall(r"\[W]", 'Google s free service'
                                          ' allows you to instantly translate '
                                          'words, phrases and web pages from English into more '
                                          'than 100 languages ​​and vice versa.')
print("#4 только число")
print(result)

