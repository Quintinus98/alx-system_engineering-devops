# Time to practice configuring your server with Puppet! Just as you
# did before, we’d like you to install and configure an Nginx server
# using Puppet instead of Bash.

exec {'update':
  command  => '/usr/bin/apt-get update',
  provider => 'shell',
}

package {'nginx':
  ensure  => 'installed',
  require => Exec['update'],
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

exec {'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}
