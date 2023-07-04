#!/usr/bin/env ruby
# Matching 10 digit phone number with regular expression
puts ARGV[0].scan(/^\d{10}$/).join
