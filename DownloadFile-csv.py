from urllib import request

file_url = 'http://download.finance.yahoo.com/d/quotes.csv?s=GOOG&f=sl1d1t1c1ohgv&e=.csv'

def download_file(url):
    response = request.urlopen(url)
    text = response.read()
    str_of_lines = str(text)
    lines = str_of_lines.split('\\n')
    destn_url = 'CSV_file.csv'
    fw = open(destn_url, 'w')
    for line in lines:
        fw.write(line + '\n')
    fw.close()

download_file(file_url)