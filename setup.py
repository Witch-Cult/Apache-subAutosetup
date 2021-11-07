import subprocess

def Cri(cmd):
  subprocess.call(cmd, shell=True);

domain = raw_input("\x1b[1;37mEnter your domain (\x1b[1;36me.g: site.com\x1b[1;37m): \x1b[1;31m")
subName = raw_input("\x1b[1;37mEnter Desired Subdirectory Name \x1b[1;36me.g: panel\x1b[1;37m): \x1b[1;31m")
subDirectory = raw_input("\x1b[1;37mEnter Directory Associated with SubName (\x1b[1;36me.g: /var/www/html/panel\x1b[1;37m): \x1b[1;31m")

outF = open("/etc/apache2/sites-available/"+subName+".conf", "w")
textList = [
'<VirtualHost *:80>',
'  ServerName '+subName+'.'+domain+'',
'  DocumentRoot "'+subDirectory+'"',
'  AllowEncodedSlashes On',
'  php_value upload_max_filesize 100M',
'  php_value post_max_size 100M',
'  <Directory "'+subDirectory+'">',
'    AllowOverride all',
'  </Directory>',
'</VirtualHost>']
for line in textList:
  print >>outF, line
outF.close()

Cri("chmod -R 755 "+subDirectory+"")
Cri("a2ensite "+ subName +"")
Cri("systemctl reload apache2")

Cri('clear')
print("\x1b[1;37mConfig \x1b[1;31mCreated\n\x1b[1;37mPlease Redirect to \x1b[1;35mCloudflare\x1b[1;37m or your domain provider and setup the desired A Record / Subdomain.\nif you already have the subdomain setup (A Record) you can access the following Sub_D")
print("\x1b[1;37mOriginal Domain: \x1b[1;33m"+ domain +"")
print("\x1b[1;37mCreated SUB_CONFIG: \x1b[1;34m"+subName+"")
print("\x1b[1;37mDirectory used in new SUB_CONFIG: \x1b[1;35m"+subDirectory+"")
print("\x1b[1;37mAvailable URL: \x1b[1;36m"+subName+"."+domain+"")
print("\x1b[1;37mConfig Location: \x1b[1;32m/etc/apache2/sites-available/"+subName+".conf\x1b[1;37m")
