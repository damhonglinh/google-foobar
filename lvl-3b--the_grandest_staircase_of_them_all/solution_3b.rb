class Solution_3b

  def run(n)
    max_col = find_max_col(n)
    arr = find_array_with_max_len(n, max_col)
    puts("arr: #{arr.reverse}".green)

    total_count = process_and_count_on(arr)
  end

  def process_and_count_on(arr)
    last_sum = 0
    total_count = 0

    arr.each_with_index do |a, index|
      b = last_sum
      last_sum += a
      next if index == 0 # skip first number

      count = count_last_two(a, b)
      max_dimension = arr.length - index
      count += count_and_reduce_dimensions(a, b, max_dimension)
      puts("#{[a, b]} - count: #{count} - total_count: #{total_count}".yellow)
      total_count += count
    end

    total_count
  end

  ########

  def count_and_reduce_dimensions(a, b, dimension)
    return 0 if dimension < 2
    total_sub_count = 0

    (2..dimension).reverse_each do |i|
      total_sub_count += count_and_reduce_one_dimension(a, b, i)
    end

    total_sub_count
  end

  def count_and_reduce_one_dimension(a, b, dimension)
    total_sub_count = 0
    loop do
      a += 1
      b -= dimension
      break if a >= b

      total_sub_count += count_last_two(a, b)
      total_sub_count += count_and_reduce_dimensions(a, b, dimension - 1)
    end

    total_sub_count
  end

  ########

  def count_last_two(a, b)
    ((b - a) / 2.0).ceil
  end

  def find_array_with_max_len(n, max_col, base = 1)
    arr = Array.new(max_col){ |i| (i + base) }
    arr_sum = (arr.length / 2.0) * (base + arr.last)
    missing = n - arr_sum
    arr[arr.length - 1] += missing.to_i
    arr.reverse
  end

  def find_max_col(n)
    ((Math.sqrt(8 * n + 1) - 1) / 2).floor
  end

  # def find_max_col_with_base(sum, base = 1)
  #   simplified_base = 2 * base - 1
  #   ((Math.sqrt(8 * sum + simplified_base * simplified_base) - simplified_base) / 2).floor
  # end

end
