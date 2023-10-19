# This script makes it possible to login with the holberton user
# And open a file without any error message

$hard_cmd = 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf'
$soft_cmd = 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf'

# Enable high hard file limit
exec { 'hard_limit':
  command => $hard_cmd,
  path    => '/usr/local/bin/:/bin/'
}
# Enable high soft file limit
exec {'soft_limit':
  command => $soft_cmd,
  path    => '/usr/local/bin/:/bin/'
}
