from flask import Flask ,render_template , request , redirect
import requests
import bs4
app = Flask(__name__)


"""

shred url = https://x.com/goalsa/status/1789807775536570403?s=46


"""

def twdownload(url):
  if 'x.com' in url :
    d_url= url.replace('x.com','twitter.com')
  elif 'twitter.com' in url :
    d_url = url
  else:
    return None
  api_url = f"https://twitsave.com/info?url={d_url}"

  response = requests.get(api_url)
  data = bs4.BeautifulSoup(response.text, "html.parser")
  download_button = data.find_all("div", class_="origin-top-right")[0]
  quality_buttons = download_button.find_all("a")
  hql = quality_buttons[0].get("href") # Highest quality video url
  return hql
  





@app.route('/',methods=['POST','GET'])
def home():
  if request.method.lower() == 'get':
    return render_template('index.html')
  if request.method.lower() == 'post':
    surl = request.form.get('url')
    url = twdownload(surl)
    if url:
      return render_template('index.html',Rmode=True,url=url)
    else:
     return render_template('index.html',error='Invalied url | عنوان غير صالح')
@app.route('/url',methods=['POST','GET'])
def index():
  if request.method.lower() == 'get':
    return redirect("/")
  if request.method.lower() == 'post':
    surl = request.form.get('url')
    url = twdownload(surl)
    if url:
      return str(url)
    else:
      return 'error'
  








if __name__ == '__main__':
  app.run(host='0.0.0.0')