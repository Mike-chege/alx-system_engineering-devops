# using puppet to manage the SSH configuration

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  mode    => '0600',
  content => "# SSH client configuration\n\n" .
             "Host 67.202.31.142\n" .
             "    IdentityFile ~/.ssh/school\n" .
             "    PreferredAuthentications publickey\n" .
             "    PasswordAuthentication no\n",
}
