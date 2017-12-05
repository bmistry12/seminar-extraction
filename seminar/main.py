import getFileToTag
import seminars
def main() :
  run = True
  id = 301
  while (run) :
    print(id)
    getFileToTag.setID(id)
    getFileToTag.main()
    seminars = Seminars()


    id = id + 1
