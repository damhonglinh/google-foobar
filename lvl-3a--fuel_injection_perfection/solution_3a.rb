class Solution_3a

  def answer(num_str)
    num = num_str.to_i
    find_steps_count(num, 0)
  end

  def base_cases(num)
    if num == 3
      2
    elsif num == 2
      1
    elsif num == 1
      0
    else
      nil
    end
  end

  def find_steps_count(num, current_count = 0)
    if base_result = base_cases(num)
      return current_count + base_result
    end

    if num.even?
      return current_count + 1 + find_steps_count(num / 2, current_count)
    else
      new_num = second_last_digit_is_one?(num) ? (num + 1) : (num - 1)
      return current_count + 1 + find_steps_count(new_num, current_count)
    end
  end

  def second_last_digit_is_one?(num)
    (num >> 1).odd?
  end
end
