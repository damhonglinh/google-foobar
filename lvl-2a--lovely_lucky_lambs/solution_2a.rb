class Solution_2a
  PHI = ((1 + Math.sqrt(5)) / 2)

  def run(total_lambs)
    generous = find_num_with_geo_seq(total_lambs)
    stingy = find_num_with_fibo_sum(total_lambs)

    stingy - generous
  end

  def find_num_with_geo_seq(sum_to_find)
    Math.log2(sum_to_find + 1).floor
  end

  def find_num_with_fibo_sum(sum_to_find)
    num = 0
    while num < 41 do # fibo_sum at 41 is larger than 1 billion
      sum = sum_fibo_at(num + 1)
# puts("n = #{num} ; SUM = #{sum}")
      if sum > sum_to_find
        return num
      end
      num += 1
    end
  end

  ###### utils

  def fibo_at(num)
    result = ((PHI**num) - ((1 - PHI)**num)) / Math.sqrt(5)
    result.floor
  end

  def sum_fibo_at(num)
    fibo_at(num + 2) - 1
  end

end
