base = A - 1
new_sum = (A + B) - 2 * (A - 1)
        = A + B - 2*A + 2
        = -A + B + 2
        = B - A + 2       <---------

count = (sum / 2).ceil - 1     <---------

# def find_max_col(n)
#   ((Math.sqrt(8 * n + 1) - 1) / 2).floor
# end

#########################


### 3  --  1
  1 2
### 4  --  1
  1 3
### 5  --  2
  1 4
  2 3

### 7  --  4
  1 2 4
  1 6
  2 5
  3 4

### 8  --  5
  1 2 5
  1 3 4
  1 7
  2 6
  3 5

### 9  ---  7
  1 2 6
  1 3 5
  1 8
    2 3 4         <---------------
  2 7
  3 6
  4 5

### 10  ---  9
  1 2 3 4         1
  1 2 7           3
  1 3 6
  1 4 5
  1 9             4
    2 3 5         <---------------
  2 8
  3 7
  4 6

### 11  ---  11
  1 2 3 5
  1 2 8
  1 3 7
  1 4 6
  1 10
    2 3 6         <---------------
    2 4 5         <---------------
  2 9
  3 8
  4 7
  5 6

### 13  ---  16 + 1
  1 2 3 7
  1 2 4 6
  1 2 10
  1 3 9
  1 4 8
  1 5 7
  1 12
  2 11
  3 10
  4 9
  5 8
  6 7
    <!-- 2 3 8          -->
    <!-- 2 4 7          -->
    <!-- 2 5 6          -->
    <!-- 3 4 6          -->
      1 3 4 5
      2 3 8           3
      2 4 7
      2 5 6
      3 4 6

### 15  --  16 + 5 + 3 = 24 (est 31)
1 2 3 4 5            1
1 2 3 9              3
1 2 4 8
1 2 5 7
  2 3 4 6                 1
  2 3 10                  4
  2 4 9
  2 5 8
  2 6 7
    3 4 8                       2
    3 5 7
    4 5 6                       1
1 2 12               5
1 3 11
1 4 10
1 5 9
1 6 8
1 14                 7
2 13
3 12
4 11
5 10
6 9
7 8

### 20 --- 26 + 11 + 7 + 3 + 2 = 49 (est 107)
  1 2 3 4 10         3
  1 2 3 5 9
  1 2 3 6 8
    2 3 4 5 6             1
    2 3 4 11              4
    2 3 5 10
    2 3 6 9
    2 3 7 8
    2 3 15                6
    2 4 14
    2 5 13
    2 6 12
    2 7 11
    2 8 10
      3 4 5 8                   2
      3 4 6 7
      3 4 13                    5
      3 5 12
      3 6 11
      3 7 10
      3 8 9
        4 5 11                        3
        4 6 10
        4 7 9
          5 6 9                         2
          5 7 8
  1 2 3 14           6
  1 2 4 13
  1 2 5 12
  1 2 6 11
  1 2 7 10
  1 2 8 9
  1 2 17             8
  1 3 16
  1 4 15
  1 5 14
  1 6 13
  1 7 12
  1 8 11
  1 9 10
  1 19               9
  2 18
  3 17
  4 16
  5 15
  6 14
  7 13
  8 12
  9 11

### ----------------------------------------
  Algo desc:
  arr = array_with_max_length

  last_sum = 0
  total_count = 0
  arr.reverse.each_slice(2) do |a, b|
    b = [b, last_sum].max
    last_sum = a + b
    sub_sum = b - a + 2
    count = (sub_sum / 2).ceil - 1
    total_count += count
  end

  total_count



### 35 --- 107 (not yet, est. 200)
  1 2 3 4 5 6 14        4
  1 2 3 4 5 7 13
  1 2 3 4 5 8 12
  1 2 3 4 5 9 11
    2 3 4 5 6 7 8         1      <---------------
    2 3 4 5 6 15          5      <---------------
    2 3 4 5 7 14
    2 3 4 5 8 13
    2 3 4 5 9 12
    2 3 4 5 10 11
    2 3 4 5 21            8      <---------------
    2 3 4 6 20
    2 3 4 7 19
    2 3 4 8 18
    2 3 4 9 17
    2 3 4 10 16
    2 3 4 11 15
    2 3 4 12 14
    2 3 4 26              11     <---------------
    2 3 5 25
    2 3 6 24
    2 3 7 23
    2 3 8 22
    2 3 9 21
    2 3 10 20
    2 3 11 19
    2 3 12 18
    2 3 13 17
    2 3 14 16
    2 3 30                14     <---------------
    2 4 29
    2 5 28
    2 6 27
    2 7 26
    2 8 25
    2 9 24
    2 10 23
    2 11 22
    2 12 21
    2 13 20
    2 14 19
    2 15 18
    2 16 17
  1 2 3 4 5 20          8
  1 2 3 4 6 19
  1 2 3 4 7 18
  1 2 3 4 8 17
  1 2 3 4 9 16
  1 2 3 4 10 15
  1 2 3 4 11 14
  1 2 3 4 12 13
  1 2 3 4 25             11
  1 2 3 5 24
  1 2 3 6 23
  1 2 3 7 22
  1 2 3 8 21
  1 2 3 9 20
  1 2 3 10 19
  1 2 3 11 18
  1 2 3 12 17
  1 2 3 13 16
  1 2 3 14 15
  1 2 3 29                13
  1 2 4 28
  1 2 5 27
  1 2 6 26
  1 2 7 25
  1 2 8 24
  1 2 9 23
  1 2 10 22
  1 2 11 21
  1 2 12 20
  1 2 13 19
  1 2 14 18
  1 2 15 17
  1 2 32                  15
  1 3 31
  1 4 30
  1 5 29
  1 6 28
  1 7 27
  1 8 26
  1 9 25
  1 10 24
  1 11 23
  1 12 22
  1 13 21
  1 14 20
  1 15 19
  1 16 18
  1 34                    17
  2 33
  3 32
  4 31
  5 30
  6 29
  7 28
  8 27
  9 26
  10 25
  11 24
  12 23
  13 22
  14 21
  15 20
  16 19
  17 18
