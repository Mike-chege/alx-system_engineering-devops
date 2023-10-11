# This script finds out why Apache is returning a 500 error
$cmd = 'sed -i s/phpp/php/g /var/www/html/wp-settings.php'
exec { 'fix-wordpress':
  command => $cmd,
  path    => '/usr/local/bin/:/bin/'
}
