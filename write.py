with open('write.txt', 'w') as write_line:
    write_line.write('Hey there ninjas, python is awesome')

#junk

with open('write.txt', 'a') as write_file:
    write_file.write('\nI love it s much, I dream in python')

quotes = [ '\nI can resist everything except temptation',
           '\nWe are all in the gutter, but some of us are looking at the stars.',
           '\nAlways forgive your enemies - nothing annoys them so much']

with open('write.txt', 'a') as write_file:
    write_file.writelines(quotes)