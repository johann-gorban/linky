# Linky
Linky is Telegram bot for scrapping and storing all URL from your messages

### How to use it
Just write or forward any message or messages to and Linky will extracts all URLs from them. There is no way other people can see your links

Once you send message, you may get all URLs. To do that, use endpoints:
- `/all_links` prints your unique URLs as Telegram message
- `/csv` returns a CSV file contains unique URLs
- `/full_csv` gives you a CSV file with all links

### How to deploy
There are only a few steps to deploy Linky but before doing that **do not forget to create bot** using FatherBot and get token 
1. Clone repo using `git clone https://github.com/johann-gorban/linky`
2. Go into the project dir `cd linky`
3. Open the terminal
4. Install Docker
5. Run `docker build -t linky .`
6. Start the image typing `docker run -d linky`
7. Use it
