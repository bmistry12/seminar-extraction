import sys, re, http.client, urllib.request, urllib.parse, urllib.error, json

from pprint import pprint

def get_url( domain, url ) :

  # Headers are used if you need authentication
  headers = {}

  try:
    conn = http.client.HTTPSConnection( domain )
    conn.request("GET", url, "", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data 
  except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

  # Failed to get data!
  return None


def run(query) :
  isName = False
  query = urllib.parse.quote_plus( query )
  url_data = get_url( 'en.wikipedia.org', '/w/api.php?action=query&list=search&format=json&srsearch=' + query )

  #graceful exit if we have failed.
  if url_data is None :
    print( "Failed to get data ... Can not proceed." )
    sys.exit()

  # http.client socket returns bytes - we convert this to utf-8
  url_data = url_data.decode( "utf-8" ) 

  # Convert the structured json string into a python variable 
  url_data = json.loads( url_data )
  # Pretty print
  #pprint( url_data )
  isName = canBeName(url_data)

  #Now we extract just the titles
  titles = [ i['title'] for i in url_data['query']['search'] ]
  pprint( titles )

  # Make sure we can plug these into urls:
  url_titles = [ urllib.parse.quote_plus(i) for i in titles ]
  #pprint( url_titles )
  return isName

def execute(name):
  query = name
  isName = run(query)
  return isName

def canBeName(data):
  #if it could be a name there will be an entry that includes a 'born' segment
  stringData = str(data)
  bornReg = 'born\s(([0-z]+\,?\s?)+)'
  dobs = re.findall(bornReg, stringData)
  if (dobs != []) :
    return True
  else : 
    return False
