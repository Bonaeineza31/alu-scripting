#!/usr/bin/env ruby
log = ARGV[0]
matches = log.scan(/from:(\S+).*to:(\S+).*flags:(\S+)/)
matches.each { |sender, receiver, flags| puts "#{sender},#{receiver},#{flags}" }
