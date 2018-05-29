require 'bigdecimal'
puts(BigDecimal.new('2').power(1000).to_s('20f').gsub(/\.0*/, '').gsub(/ /, '').split(//).map {|i| i.to_i}.sum)
