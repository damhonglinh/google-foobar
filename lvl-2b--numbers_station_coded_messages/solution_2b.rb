class Solution_2b

  def run(l, t)
    i = 0
    while i < l.length do
      j = qualified(l, i, t)
      if j >= 0
        return [i, j]
      end
      i += 1
    end

    return [-1, -1]
  end

  def qualified(l, i, t)
    sum = 0
    j = i

    while j < l.length do
      sum += l[j]
      return j if sum == t
      return -1 if sum > t
      j += 1
    end

    return -1
  end
  
end
