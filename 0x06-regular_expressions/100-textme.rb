#!/usr/bin/env ruby
results = ARGV[0].scan(/from:([a-zA-Z0-9+]+)\].*?to:([0-9+]+)\].*?flags:([-:0-9]+)\]/)
if results.any?
  puts results.map { |match| match.join(',') }.join("\n")
end
