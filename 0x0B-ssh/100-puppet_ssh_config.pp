# using Puppet to make changes to our configuration file
include stdlib


file_line { 'Use Identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile  ~/.ssh/school',
  replace => true,
}

file_line { 'No password auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}
