# Increases Nginx file descriptor limit

exec {'Increase limit',
path   => 'usr/bin',
command => 'sed -i s/15/4096/g /etc/default/nginx',
}

exec {'restart Nginx',
path  => '/usr/bin',
command => 'sudo service nginx restart',
}
