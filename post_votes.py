FILE_NAME_OPEN = "post_votes.csv"
FILE_NAME_WRITE = "post_votes.html"
TITLE = "User's post_votes"


file_open = open(FILE_NAME_OPEN, "r", encoding="utf-8")
file_write = open(FILE_NAME_WRITE, "w", encoding="utf-8")
file_write.write(f'<head><title>{TITLE}</title></head><body>')

number = 0
for line in file_open.readlines():
    reddit_url = line.split(",")[1]
    number = number + 1
    file_write.write(f'{number}  <a href={reddit_url}>{reddit_url}</a><br>')
file_write.write(f'</body>')