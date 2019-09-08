#! /usr/bin/ruby

require 'cgi'
require 'shellwords'

DIR = '/home/nona7/private_html/scrapbox/rebuild-kitashirakawa/secret-links'
BASE = 'https://inside.kmc.gr.jp/~nona7/scrapbox/rebuild-kitashirakawa/secret-links'
cgi = CGI.new

puts 'Content-Type: text/html'
puts ''
puts '<!doctype html><title>maker</title>'

name = cgi.params['name'][0]
uri = cgi.params['uri'][0]

if ! name =~ /^\w+$/
  puts 'name shuoud be \\w+'
  return
end

if system(Shellwords.join(['test', '-d', "#{DIR}/#{name}".shellescape]))
  puts "name: #{name} exist!"
  return
end

puts "name: #{name} ok<br />"

if uri.length == 0
  puts 'input uri'
  return
end

cmd = Shellwords.join(['mkdir', "#{DIR}/#{name}".shellescape])
puts cmd

system(cmd)
File.open("#{DIR}/#{name}/.htaccess".shellescape, 'w') do |f|
  f.write "RedirectMatch ^ #{uri}"
end

puts '<br /><br />'
puts "#{BASE}/#{name}"
