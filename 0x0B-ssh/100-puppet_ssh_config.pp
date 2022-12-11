# Setup config file with puppet

exec { 'Config SSH':
  path    => '/usr/bin',
  command => 'echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
