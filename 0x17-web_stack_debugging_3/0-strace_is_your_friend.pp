# Using strace, find out why Apache is returning a 500 error
# Once you find the issue, fix it and then automate it using Puppet
file_line { 'replace_class-wp-locale':
  path    => '/var/www/html/wp-settings.php',
  line    => "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );",
  match   => "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );",
  replace => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
}
