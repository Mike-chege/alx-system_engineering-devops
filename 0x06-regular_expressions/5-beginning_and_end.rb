#!/usr/bin/env ruby
# Regular expression to match strings h and n
puts ARGV[0].scan(/^h.n$/).join
