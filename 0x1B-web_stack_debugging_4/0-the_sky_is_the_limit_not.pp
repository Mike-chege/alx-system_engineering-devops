# This script configures the web server to work under pressure

$cmd = 'sed -i "s/15/4096/" /etc/default/nginx'
exec { 'fix_nginx':
  command => $cmd,
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart nginx
exec {'restart_nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
