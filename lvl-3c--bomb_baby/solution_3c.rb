class Solution_3c

  def answer(a_str, b_str)
    a = a_str.to_i
    b = b_str.to_i
    # find_recursively(a, b, 0)
    find_with_loop(a, b).to_s
  rescue
    'impossible'
  end


  def find_recursively(a, b, count)
    return count if a == 1 && b == 1
    raise 'impossible' if a <= 0 || b <= 0 || a == b

    (a > b) ? (a -= b) : (b -= a)
    return find_recursively(a, b, count + 1)
  end

  def find_with_loop(ori_a, ori_b)
    a = ori_a ; b = ori_b ; count = 0

    loop do
      return count if a == 1 && b == 1
      return 'impossible' if a <= 0 || b <= 0 || a == b

      (a > b) ? (a -= b) : (b -= a)
      count += 1
    end
  end

end
