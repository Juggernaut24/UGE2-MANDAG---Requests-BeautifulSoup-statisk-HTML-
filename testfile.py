"""response = requests.get(base_url)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

meta_tag = soup.find('meta')
encoding = meta_tag['charset']
print(encoding)
#print(response.content)

print(soup.title.text)"""