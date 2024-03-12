# testing how well our web server setup featuring
# Nginx is doing under pressure

exec { 'update_ulimit_variable':
  command => 'sed -i s/"-n 15"/"-n 4096"/g /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
service {'nginx':
  ensure  => 'running',
  restart => true,
}
