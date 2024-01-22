# using Puppet to make changes to our configuration file
file { '~/.ssh/config':
  ensure => file,
  content => "
              HOST *
              PasswordAuthentication no
              IdentityFile ~/.ssh/school
            ",
  mode => '0600',
}
