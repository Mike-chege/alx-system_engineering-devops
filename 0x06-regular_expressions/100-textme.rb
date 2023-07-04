#!/usr/bin/env ruby
# Getting transactions details (from, to, flags)
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(separator=",")
