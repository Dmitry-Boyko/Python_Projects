# one line comment
=begin
 blah blah
 blah blah
 multi line comment 
=end

#get input from the user
puts "Enter a number: "
num1 = gets.to_f
puts "Enter another number: "
num2 = gets.to_f

# perfom some math:
puts "added: " + (num1 + num2).to_s
puts 'substracted: ' + (num1 - num2).to_s
puts "multiplied: " + (num1 * num2).to_s
puts "divided " + (num1 / num2).to_s
 
=begin
 Constant  are indentifiers whose value cannot be changed
 Constant mus begin with an Upper-case letter 
=end

Three = 3
puts num1.to_s + " plus " + Three.to_s + " = " + (num1 + Three).to_s

# try to change the value of a constant:
Three = 3.0