# Fix Apache Internal Server Error, Apaches hosts a Wordpress website
# Using LAMP

exec { ' Fix typo':
path    => '/usr/local/bin/:/bin/',
command => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
}

exec {' Restart Apache2':
path    => '/usr/bin',
command => 'sudo service apache2 restart',
}
