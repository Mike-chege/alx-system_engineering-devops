# This script configures the web server to work under pressure

$cmd = 'sed -i "s/15/4096/" /etc/default/nginx'
exec { 'fix-nginx':
  command => $cmd,
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart nginx
exec {'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
