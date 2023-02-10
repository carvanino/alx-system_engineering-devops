# Increases Nginx file descriptor limit


exec { 'Set worker processes to auto':
  command => 'sed -i 2s/4/auto/ /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin/',
}


exec {'Increase limit':
path    => '/usr/local/bin/:/bin/',
command => 'sed -i s/15/4096/g /etc/default/nginx',
}

exec {'restart Nginx':
path    => '/usr/bin',
command => 'sudo service nginx restart',
}
