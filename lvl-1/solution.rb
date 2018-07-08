class Solution

  def run(input)
    divs = find_divisors(input.length)
    divs.each do |div|
      if qualified(input, div)
        return input.length / div
      end
    end

    nil
  end

  def qualified(input, div)
    offset = 0
    while offset < div do
      return true if qualified_circle(input, div, offset)
      offset += 1
    end

    false
  end

  def qualified_circle(input, div, offset)
    base_str = get_sub_str(input, offset, div + offset)

    i = div + offset
    while i < input.length do
      upper_i = i + div
      sub_str = get_sub_str(input, i, upper_i)

      return false if sub_str != base_str
      i = upper_i
    end

    true
  end

  ###### utils

  def find_divisors(n)
    (1..n).map do |i|
      i if n % i == 0
    end.compact
  end

  def get_sub_str(input, from, to)
    to = [0, to - 1].max
    input[from..to]
  end

  def stub_circle(input, extra_len)
    input + input[0, extra_len]
  end

end
