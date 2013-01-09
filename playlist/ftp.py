# -*- coding: utf-8 -*-
import sys
import os
import os.path
import threading
import time
import errno

sys.path.append('/home/phuzion/Code/pydj/playlist')
sys.path.append('/home/phuzion/Code/pydj/')
sys.path.append('/home/phuzion/')
from pyftpdlib import ftpserver
from upload import UploadedFile, UnsupportedFormatError, CorruptFileError

from pydj import settings
from django.core.management import setup_environ
setup_environ(settings)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from pydj.playlist.models import FileTooBigError, DuplicateError


BASE_DIR = settings.FTP_BASE_DIR

class G2FTPHandler(ftpserver.FTPHandler):
  
  def __init__(self, conn, server):
    ftpserver.FTPHandler.__init__(self, conn, server)
    
  def on_file_received(self, file):
  
    def handle():
      try:
        User.objects.get(username=self.username).get_profile().uploadSong(UploadedFile(file))
      except UnsupportedFormatError, e:
        self.respond("557 ERROR: file format not supported")
        return
      except CorruptFileError, e:
        self.respond("554 ERROR: file corrupt")
        return
      except FileTooBigError, e:
        self.respond("555 ERROR: file too big. Hi Jormagund!")
        return
      except DuplicateError:
        self.respond("556 ERROR: file an exact duplicate. Search before uploading!")
        return
      finally:
        os.remove(file)
      self.sleeping = False
      
    self.sleeping = True
    threading.Thread(target=handle).start()

class G2Authorizer(ftpserver.DummyAuthorizer):
  def validate_authentication(self, username, password):
    User.objects.update() #avoid THE FTP BUG!
    if not bool(authenticate(username=username, password=password)):
      return False
    try:
      homedir = os.path.join(BASE_DIR, username.lower())
      os.mkdir(homedir)
    except OSError, e:
      if e.errno != errno.EEXIST: #file already exists
        raise e
      
    try:
      self.add_user(username, 'password', homedir, perm='lweadf') #list, write, CWD
    except ftpserver.AuthorizerError:
      pass #already logged in
      
    return True
  
now = lambda: time.strftime("[%Y-%b-%d %H:%M:%S]")
   
def standard_logger(msg):
    f1.write("%s %s\n" %(now(), msg))
    f1.flush()
   
def line_logger(msg):
    f2.write("%s %s\n" %(now(), msg))
    f2.flush()
    
def error_logger(msg):
    f3.write("%s %s\n" %(now(), msg))
    f3.flush()
  
if __name__ == "__main__":
  f1 = open('ftpd.log', 'a')
  f2 = open('ftpd.lines.log', 'a')
  f3 = open('ftpd.error.log', 'a')
  ftpserver.log = standard_logger
  ftpserver.logline = line_logger
  ftpserver.logerror = error_logger
  authorizer = G2Authorizer()
  ftp_handler = G2FTPHandler
  ftp_handler.authorizer = authorizer
  address = ('', 2100)
  ftpd = ftpserver.FTPServer(address, ftp_handler)
  ftpd.serve_forever()

